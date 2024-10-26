import smbus2
import bme280
import time
import sys


# I2C address for BME280 sensor
BME280_ADDRESS = 0x76


def initialize_bme280(bus):
    """
    Initialize the BME280 sensor by loading the calibration parameters.
    """
    # Load calibration parameters from the sensor
    try:
        calibration_params = bme280.load_calibration_params(bus, BME280_ADDRESS)
        return calibration_params
    except Exception as error:
        print(f"Error initializing BME280: {error}")
        return None  # Return None if initialization fails


def read_bme280(bus, address, calibration_params):
    """
    Read and return sensor data from the BME280 sensor.
    """
    try:
        data = bme280.sample(bus, address, calibration_params)
        return data
    except Exception as error:
        print(f"Error reading BME280 data: {error}")
        return None  # Return None if reading fails
    

def print_sensor_data(data):
    """
    Print temperature, pressure, and humidity data.
    """
    if data:  # Ensure data is not None before printing
        print(f"Data ID: {data.id}")
        print(f"Timestamp: {data.timestamp}")
        print(f"Temperature: {data.temperature:.2f} °C")
        print(f"Pressure: {data.pressure:.2f} hPa")
        print(f"Humidity: {data.humidity:.2f} %")
        print("-" * 40)
    else:
        print("No valid data to display.")


if __name__ == "__main__":
    # Ensure the I2C bus is defined
    i2c_bus = None
    
    try:
        # Initialize I2C bus
        i2c_bus = smbus2.SMBus(1)  # Use 1 for Raspberry Pi Zero 2

        # Initialize the BME280 sensor
        calibration_params = initialize_bme280(i2c_bus)
        
        # Check if initialization was successful
        if calibration_params is None:
            print("Failed to initialize BME280. Exiting.")
            sys.exit()

        # Continuous data reading and printing
        while True:
            sensor_data = read_bme280(i2c_bus, BME280_ADDRESS, calibration_params)
            print_sensor_data(sensor_data)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        # Close the I2C bus if it was opened
        if i2c_bus: 
            i2c_bus.close()
