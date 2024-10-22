import smbus2
import time
import bh1750


def read_light():
    """Read and print light intensity from the BH1750 sensor."""
    try:
        # Read light intensity in lux
        lux = light_sensor.luminance(bh1750.BH1750.ONCE_HIRES_1)
        print(f"Light Intensity: {lux:.2f} lx")
    except Exception as e:
        print(f"Error reading BH1750 sensor: {e}")


if __name__ == "__main__":
    # Initialize I2C bus
    bus = smbus2.SMBus(1)

    # Initialize the BH1750 sensor
    light_sensor = bh1750.BH1750(bus)

    while True:
        read_light()
        time.sleep(1)
