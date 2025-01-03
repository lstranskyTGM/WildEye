import time
import logging
from mpu6050 import mpu6050

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class MPU6050Sensor:
    """
    A class to interact with the MPU-6050 sensor for accelerometer, gyroscope, and temperature readings.
    """

    def __init__(self, address=0x68):
        """
        Initialize the MPU6050Sensor instance.

        Args:
            address (int): The I2C address of the MPU-6050 sensor (default: 0x68).
        """
        try:
            self.sensor = mpu6050(address)
            logging.info(f"MPU-6050 initialized at address {hex(address)}.")
        except Exception as error:
            logging.error(f"Error initializing MPU-6050: {error}")
            self.sensor = None

    def read_data(self):
        """
        Read accelerometer, gyroscope, and temperature data from the MPU-6050 sensor.

        Returns:
            dict: A dictionary containing accelerometer, gyroscope, and temperature data.
                  Returns None if reading fails.
        """
        if not self.sensor:
            logging.warning("Sensor not initialized. Please check initialization.")
            return None

        try:
            accel_data = self.sensor.get_accel_data()
            gyro_data = self.sensor.get_gyro_data()
            temp = self.sensor.get_temp()

            return {
                "acceleration": accel_data,
                "gyroscope": gyro_data,
                "temperature": temp,
            }
        except Exception as error:
            logging.error(f"Error reading data from MPU-6050: {error}")
            return None


def display_sensor_data(data):
    """
    Display accelerometer, gyroscope, and temperature data.

    Args:
        data (dict): A dictionary containing accelerometer, gyroscope, and temperature data.
    """
    if data:
        accel = data["acceleration"]
        gyro = data["gyroscope"]
        temp = data["temperature"]

        print(f"Acceleration (g): X={accel['x']:.2f}, Y={accel['y']:.2f}, Z={accel['z']:.2f}")
        print(f"Gyroscope (deg/s): X={gyro['x']:.2f}, Y={gyro['y']:.2f}, Z={gyro['z']:.2f}")
        print(f"Temperature (C): {temp:.2f}")
        print("-" * 40)
    else:
        print("No valid data to display.")


def monitor_mpu6050(sensor):
    """
    Continuously monitor and log data from the MPU-6050 sensor until interrupted.

    Args:
        sensor (MPU6050Sensor): An instance of the MPU6050Sensor class.
    """
    if not sensor.sensor:
        logging.error("Failed to initialize MPU-6050. Exiting...")
        return

    logging.info("MPU-6050 sensor is ready. Reading data...")

    try:
        while True:
            sensor_data = sensor.read_data()
            display_sensor_data(sensor_data)
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt detected. Exiting...")


if __name__ == "__main__":
    # Create an instance of the MPU6050Sensor class
    mpu_sensor = MPU6050Sensor()

    # Start monitoring the sensor
    monitor_mpu6050(mpu_sensor)
