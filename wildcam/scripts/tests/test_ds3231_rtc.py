import smbus2
import time
from datetime import datetime
import adafruit_ds3231


# I2C address for the DS3231 RTC
DS3231_ADDRESS = 0x68


def read_time(rtc):
    """
    Read the current time from the DS3231 RTC.
    """
    # Get the current datetime from the RTC
    return rtc.datetime


def set_time(rtc, dt):
    """
    Set the time on the DS3231 RTC.
    """
    # Set the RTC time
    if isinstance(dt, time.struct_time):
        # Set the RTC time to the provided struct_time
        rtc.datetime = dt
    elif isinstance(dt, datetime):
        # Convert datetime to struct_time
        dt = time.struct_time((dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.weekday() + 1, -1, -1))
        rtc.datetime = dt
    else:
        print("Error: Provided time is not in a recognized format.")
        return  # Exit the function
    print("Time set to:", dt)


if __name__ == "__main__":
    # Ensure the I2C bus is defined
    i2c_bus = None
    
    try:
        # Initialize I2C bus
        i2c_bus = smbus2.SMBus(1)  # Use 1 for Raspberry Pi Zero 2
        rtc = adafruit_ds3231.DS3231(i2c_bus)  # Create DS3231 object once
        
        # Optionally set the time (comment this line after setting time once)
        # now = datetime.now()
        # set_time(rtc, now)
        # Example: Year, Month, Day, Hour, Minute, Second, Day of Week, Day of Year, DST Offset (optional)
        # set_time(rtc, (2023, 10, 23, 15, 6, 0, 0, 9, -1))
        # Example: Year, Month, Day, Hour, Minute, Second
        # set_time(rtc, datetime(2023, 10, 23, 15, 6, 0))
        
        while True:
            current_time = read_time(rtc)
            print(f"Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(1)  # Wait for 1 second
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        if i2c_bus:
            i2c_bus.close()  # Close the I2C bus
