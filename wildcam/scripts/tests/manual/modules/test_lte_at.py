# Modified version of AT.py originally provided by Waveshare
# Original source: https://files.waveshare.com/upload/4/4e/SIM7600G-H-4G-HAT-B-Demo.zip

#!/usr/bin/python3

import serial
import time

# Configure the serial port
ser = serial.Serial(
    port="/dev/ttyUSB2",  # Replace with your port
    baudrate=115200,
    timeout=1
)
#ser.flushInput()  # Flush the input buffer


def send_at(command, expected_response="OK", timeout=1):
    """
    Send an AT command and check for the expected response.
    """
    rec_buff = ''
    ser.write((command + "\r\n").encode())
    time.sleep(timeout)
    
    if ser.in_waiting:
        time.sleep(0.01)
        rec_buff = ser.read(ser.in_waiting)
        
    response = rec_buff.decode().strip()
    
    if expected_response not in response:
        print(f"{command} ERROR")
        print(f"{command} back:\t{response}")
        return False
    else:
        print(response)
        return True

def main():
    """
    Main function to interact with the modem using AT commands.
    """
    # Open the serial port if it is not already open
    if not ser.is_open:
        ser.open()
    try:
        while True:
            command_input = input("Please input the AT command (exit to quit): ")
            
            if command_input.lower() == 'exit':
                break
            
            # Send the AT command
            send_at(command_input)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ser.close()
        
if __name__ == "__main__":
    main()
