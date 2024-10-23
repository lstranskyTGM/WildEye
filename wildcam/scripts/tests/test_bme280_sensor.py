import smbus2
import bme280
import time


# I2C address for BME280 sensor
BME280_ADDRESS = 0x76


def initialize_bme280(bus):
    """
    Initialize the BME280 sensor by loading the calibration parameters.
    """
    # Load calibration parameters from the sensor
    calibration_params = bme280.load_calibration_params(bus, BME280_ADDRESS)
    return calibration_params


def read_bme280(bus, address, calibration_params):
    """
    Read and return sensor data from the BME280 sensor.
    """
    data = bme280.sample(bus, address, calibration_params)
    return data


def print_sensor_data(data):
    """
    Print temperature, pressure, and humidity data.
    """
    print(f"Temperature: {data.temperature:.2f} °C")
    print(f"Pressure: {data.pressure:.2f} hPa")
    print(f"Humidity: {data.humidity:.2f} %")
    print("-" * 40)


if __name__ == "__main__":
    # Ensure the I2C bus is defined
    i2c_bus = None
    
    try:
        # Initialize I2C bus
        i2c_bus = smbus2.SMBus(1)

        # Initialize the BME280 sensor
        calibration_params = initialize_bme280(i2c_bus)

        # Continuous data reading and printing
        while True:
            sensor_data = read_bme280(i2c_bus, BME280_ADDRESS, calibration_params)
            print_sensor_data(sensor_data)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the I2C bus if it was opened
        if i2c_bus: 
            i2c_bus.close()
