import smbus2
import bme280
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class BME280Sensor:
    """
    A class to interact with the BME280 sensor for temperature, pressure, and humidity readings.
    """

    def __init__(self, bus_number=1, address=0x76):
        """
        Initialize the BME280Sensor instance.

        Args:
            bus_number (int): The I2C bus number (default: 1 for Raspberry Pi).
            address (int): The I2C address of the BME280 sensor (default: 0x76).
        """
        self.bus_number = bus_number
        self.address = address
        self.bus = None
        self.calibration_params = None

    def initialize(self):
        """
        Initialize the I2C bus and load calibration parameters for the BME280 sensor.
        """
        try:
            self.bus = smbus2.SMBus(self.bus_number)
            self.calibration_params = bme280.load_calibration_params(self.bus, self.address)
            logging.info(f"BME280 initialized at address {hex(self.address)}.")
        except Exception as error:
            logging.error(f"Error initializing BME280: {error}")
            self.calibration_params = None

    def read_data(self):
        """
        Read temperature, pressure, and humidity data from the BME280 sensor.

        Returns:
            dict: A dictionary containing temperature, pressure, and humidity data.
                  Returns None if reading fails.
        """
        if not self.calibration_params:
            logging.warning("Sensor not initialized. Please initialize first.")
            return None

        try:
            data = bme280.sample(self.bus, self.address, self.calibration_params)
            return {
                "timestamp": data.timestamp,
                "temperature": data.temperature,
                "pressure": data.pressure,
                "humidity": data.humidity,
            }
        except Exception as error:
            logging.error(f"Error reading data from BME280: {error}")
            return None

    def cleanup(self):
        """
        Clean up the I2C bus connection.
        """
        try:
            if self.bus:
                self.bus.close()
                logging.info("I2C connection closed.")
        except Exception as error:
            logging.error(f"Error during cleanup: {error}")


def display_sensor_data(data):
    """
    Display temperature, pressure, and humidity data.

    Args:
        data (dict): A dictionary containing temperature, pressure, and humidity data.
    """
    if data:
        print(f"Timestamp: {data['timestamp']}")
        print(f"Temperature: {data['temperature']:.2f} °C")
        print(f"Pressure: {data['pressure']:.2f} hPa")
        print(f"Humidity: {data['humidity']:.2f} %")
        print("-" * 40)
    else:
        print("No valid data to display.")


def monitor_bme280(sensor):
    """
    Continuously monitor and log data from the BME280 sensor until interrupted.

    Args:
        sensor (BME280Sensor): An instance of the BME280Sensor class.
    """
    try:
        sensor.initialize()

        if not sensor.calibration_params:
            logging.error("Failed to initialize BME280. Exiting...")
            return

        logging.info("BME280 sensor is ready. Reading data...")

        while True:
            sensor_data = sensor.read_data()
            display_sensor_data(sensor_data)
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt detected. Exiting...")

    finally:
        sensor.cleanup()


if __name__ == "__main__":
    # Create an instance of the BME280Sensor class
    bme_sensor = BME280Sensor()

    # Start monitoring the sensor
    monitor_bme280(bme_sensor)
