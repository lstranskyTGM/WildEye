import requests
import serial
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration settings
SERIAL_PORT = "COM3"        # Replace with your serial port
BAUD_RATE = 9600            # Replace with your baud rate
APN = "your_apn_here"       # Replace with your APN
URL = "http://example.com"  # Replace with your URL


def send_at_command(ser: serial.Serial, command: str, timeout: int = 1) -> str:
    """
    Sends an AT command to the SIM7600 modem and returns the response.

    Args:
        ser (serial.Serial): The serial connection to the modem.
        command (str): The AT command to send.
        timeout (int, optional): Time in seconds to wait for a response. Defaults to 2.

    Returns:
        str: The response from the modem.
    """
    ser.write((command + "\r\n").encode())
    time.sleep(timeout)
    response = ser.read(ser.in_waiting or 1).decode(errors="ignore")
    logger.info(f"Command: {command}, Response: {response.strip()}")
    return response


def initialize_modem() -> bool:
    """
    Initializes the SIM7600 modem by configuring it and connecting to the LTE network.
    
    Returns:
        bool: True if the modem is successfully initialized, False otherwise.
    """
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            time.sleep(1)  # Allow some time for initialization

            send_at_command(ser, "AT")
            send_at_command(ser, f'AT+CGDCONT=1,"IP","{APN}"')
            send_at_command(ser, "AT+CGATT=1")
            send_at_command(ser, "AT+CIICR")

            ip_response = send_at_command(ser, "AT+CIFSR")
            if "ERROR" in ip_response:
                raise Exception("Failed to get IP address. Check APN or signal strength.")

            logger.info(f"Connected! IP Address: {ip_response.strip()}")
        return True

    except Exception as e:
        logger.error(f"Error initializing modem: {e}")
        return False


def send_http_request(url: str, timeout: int = 10):
    """
    Sends an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to which the HTTP GET request is sent.
        timeout (int, optional): Time in seconds to wait for a response. Defaults to 10.
    """
    try:
        response = requests.get(url, timeout=timeout)
        logger.info(f"HTTP Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
    except requests.RequestException as e:
        logger.error(f"HTTP Request to {url} failed with exception {type(e).__name__}: {e}")


def main():
    logger.info("Initializing LTE Modem...")
    
    if initialize_modem():
        logger.info("Modem initialized successfully.")
        logger.info("Sending HTTP request...")
        send_http_request(URL, timeout=5)
    else:
        logger.error("Failed to initialize modem.")


if __name__ == "__main__":
    main()
