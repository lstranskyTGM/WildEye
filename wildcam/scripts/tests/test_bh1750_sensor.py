import smbus2
import bh1750
import time


def read_light():
    """
    Read and print light intensity from the BH1750 sensor.
    """
    try:
        # Read light intensity in lux
        lux = light_sensor.luminance(bh1750.BH1750.ONCE_HIRES_1)
        print(f"Light Intensity: {lux:.2f} lx")
    except Exception as e:
        print(f"Error reading BH1750 sensor: {e}")


if __name__ == "__main__":
    # Ensure the I2C bus is defined
    i2c_bus = None

    try:
        # Initialize I2C bus
        bus = smbus2.SMBus(1)

        # Initialize the BH1750 sensor
        light_sensor = bh1750.BH1750(bus)

        while True:
            read_light()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    finally:
        # Close the I2C bus if it was opened
        if i2c_bus: 
            i2c_bus.close()
