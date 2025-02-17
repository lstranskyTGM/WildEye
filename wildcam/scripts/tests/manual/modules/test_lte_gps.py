# Modified version of GPS.py originally provided by Waveshare
# Original source: https://files.waveshare.com/upload/4/4e/SIM7600G-H-4G-HAT-B-Demo.zip

# !/usr/bin/python3

import serial
import time

# Configure the serial port
ser = serial.Serial(
    port="/dev/ttyUSB2",  # Replace with your port
    baudrate=115200,
    timeout=1
)
# ser.flushInput()  # Flush the input buffer


def send_at(command, expected_response="OK", timeout=1):
    """
    Send an AT command to the modem and check for the expected response.

    Args:
        command (str): The AT command to send.
        expected_response (str): The expected response from the modem.
        timeout (int): Time in seconds to wait for a response.

    Returns:
        str: The response from the modem if received; otherwise, an empty string.
    """
    ser.write((command + "\r\n").encode())  # Send command
    time.sleep(timeout)  # Wait for response
    if ser.in_waiting:
        response = ser.read(ser.in_waiting).decode().strip()  # Read response
        print(f"Command: {command}, Response: {response}")
        return response
    else:
        print(f"Command: {command}, No response received.")
        return ""


def start_gps():
    """
    Start the GPS session if it is not already running.
    """
    gps_status = send_at('AT+CGPS?', '+CGPS:', 1)
    if '+CGPS: 0' in gps_status:  # If GPS is not running, start it
        send_at('AT+CGPS=1', 'OK', 1)  # Start GPS session
        print("GPS session started.")
    else:
        print("GPS is already running.")


def stop_gps():
    """
    Stop the GPS session to save power.
    """
    send_at('AT+CGPS=0', 'OK', 1)
    print("GPS session stopped.")


def get_gps_data():
    """
    Retrieve raw GPS data from the modem.

    Returns:
        str: Raw GPS data if available; otherwise, None.
    """
    gps_data = send_at('AT+CGPSINFO', '+CGPSINFO:', 1)

    if '+CGPSINFO:' in gps_data:
        gps_info = gps_data.split(':')[1].strip()

        if ',,,,,,' in gps_info:  # No fix available
            print("GPS is not ready. No fix available.")
            return None

        print(f"Raw GPS Data: {gps_info}")
        return gps_info
    else:
        print("No valid GPS data received.")
        return None


def monitor_gps():
    """
    Continuously monitor GPS data until a fix is acquired.
    
    Returns:
        str: The raw GPS data once a fix is acquired.
    """
    print("Starting GPS session...")
    start_gps()

    try:
        while True:
            print("\nChecking for GPS fix...")
            gps_data = get_gps_data()
            if gps_data:
                print(f"GPS Fix Acquired: {gps_data}")
                return gps_data  # Exit loop once a fix is acquired
            time.sleep(2)  # Wait before checking again

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting...")

    finally:
        stop_gps()
        ser.close()


if __name__ == "__main__":
    monitor_gps()
