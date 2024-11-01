import smbus2
import time

# MPU-6050 I2C address
MPU6050_ADDR = 0x68

# MPU-6050 Registers
PWR_MGMT_1 = 0x6B     # Power Management register 1 - to wake up the sensor (from sleep mode)
ACCEL_XOUT_H = 0x3B   # High byte of X-axis accelerometer data
ACCEL_YOUT_H = 0x3D   # High byte of Y-axis accelerometer data
ACCEL_ZOUT_H = 0x3F   # High byte of Z-axis accelerometer data
TEMP_OUT_H = 0x41     # High byte of temperature data
GYRO_XOUT_H = 0x43    # High byte of X-axis gyroscope data
GYRO_YOUT_H = 0x45    # High byte of Y-axis gyroscope data
GYRO_ZOUT_H = 0x47    # High byte of Z-axis gyroscope data


class MPU6050:
    """
    Class to interact with the MPU-6050 sensor using I2C communication.
    
    Attributes:
        bus (smbus2.SMBus): The I2C bus to communicate with the sensor.
        address (int): The I2C address of the sensor (default is 0x68).
    Methods:
        initialize_sensor(): Wakes up the sensor by writing to the power management register.
        read_raw_data(register): Reads raw data (16-bit) from the specified register and combines high and low bytes.
        get_acceleration(): Reads and returns the acceleration data in g (gravity) for X, Y, Z axes.
        get_gyroscope(): Reads and returns the gyroscope data in degrees per second (°/s) for X, Y, Z axes.
        get_temperature(): Reads and returns the temperature in Celsius.
    """
    def __init__(self, bus, address=MPU6050_ADDR):
        """
        Initializes the MPU-6050 sensor with the specified I2C bus and address.
        """
        self.bus = bus
        self.address = address
        self.initialize_sensor()

    def initialize_sensor(self):
        """
        Wakes up the MPU-6050 by writing to the power management register.
        """
        try:
            self.bus.write_byte_data(self.address, PWR_MGMT_1, 0)
            time.sleep(0.1)
        except Exception as error:
            print(f"Error initializing sensor: {error}")

    def read_raw_data(self, register):
        """
        Reads raw data (16-bit) from the specified register and combines high and low bytes.
        """
        try:
            high = self.bus.read_byte_data(self.address, register)
            low = self.bus.read_byte_data(self.address, register + 1)
            value = (high << 8) | low
            if value > 32767:
                value -= 65536
            return value
        except Exception as error:
            print(f"Error reading raw data from register {register}: {error}")
            return 0

    def get_acceleration(self):
        """
        Reads and returns the acceleration data in g (gravity) for X, Y, Z axes.
        """
        ax = self.read_raw_data(ACCEL_XOUT_H) / 16384.0
        ay = self.read_raw_data(ACCEL_YOUT_H) / 16384.0
        az = self.read_raw_data(ACCEL_ZOUT_H) / 16384.0
        return {'ax': ax, 'ay': ay, 'az': az}

    def get_gyroscope(self):
        """
        Reads and returns the gyroscope data in degrees per second (°/s) for X, Y, Z axes.
        """
        gx = self.read_raw_data(GYRO_XOUT_H) / 131.0
        gy = self.read_raw_data(GYRO_YOUT_H) / 131.0
        gz = self.read_raw_data(GYRO_ZOUT_H) / 131.0
        return {'gx': gx, 'gy': gy, 'gz': gz}

    def get_temperature(self):
        """
        Reads and returns the temperature in Celsius.
        """
        temp_raw = self.read_raw_data(TEMP_OUT_H)
        temp = (temp_raw / 340.0) + 36.53
        return temp


if __name__ == "__main__":
    # Ensure the I2C bus is defined
    i2c_bus = None

    try:
        # Initialize I2C bus
        i2c_bus = smbus2.SMBus(1)  # Use 1 for Raspberry Pi Zero 2
            
        # Initialize MPU-6050 sensor
        gyro_sensor = MPU6050(i2c_bus)
            
        while True:
            # Get sensor data
            accel_data = gyro_sensor.get_acceleration()
            gyro_data = gyro_sensor.get_gyroscope()
            temp = gyro_sensor.get_temperature()

            # Display the data
            print("Acceleration (g): X={:.2f}, Y={:.2f}, Z={:.2f}".format(
                accel_data['ax'], accel_data['ay'], accel_data['az']))
            print("Gyroscope (deg/s): X={:.2f}, Y={:.2f}, Z={:.2f}".format(
                gyro_data['gx'], gyro_data['gy'], gyro_data['gz']))
            print("Temperature (C): {:.2f}".format(temp))

            # Wait before next reading
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTest interrupted.")
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        if i2c_bus:
            i2c_bus.close()  # Close the I2C bus
            print("I2C connection closed.")
