import time
import board
import busio
import adafruit_bme280


def init_bme280():
    """Initialize I2C bus and BME280 sensor."""
    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the BME280 sensor
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

    # Optionally, set sea-level pressure for accurate altitude readings
    # bme280.sea_level_pressure = 1013.25

    return bme280


def read_bme280(bme280):
    """Read and print sensor data from the BME280 sensor."""
    # Print sensor readings
    print(f"Temperature: {bme280.temperature:.2f} °C")
    print(f"Humidity: {bme280.humidity:.2f} %")
    print(f"Pressure: {bme280.pressure:.2f} hPa")
    print(f"Altitude: {bme280.altitude:.2f} meters")
    print("-" * 40)


if __name__ == '__main__':
    # Initialize the BME280 sensor
    bme280 = init_bme280()

    # Continuously read and print sensor data
    while True:
        read_bme280(bme280)
        time.sleep(1)
