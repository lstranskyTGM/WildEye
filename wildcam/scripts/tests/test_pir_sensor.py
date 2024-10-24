import RPi.GPIO as GPIO
import time


# GPIO pin for the PIR sensor
PIR_PIN = 18


def setup_gpio(pin):
    """
    Set up the GPIO pin for input and event detection.
    """
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(pin, GPIO.IN)  # Set the pin as input
    GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300)  # Detect both motion and no motion
    GPIO.add_event_callback(pin, motion_event_handler)  # Assign callback function


def motion_event_handler(channel):
    """
    Callback function triggered on PIR sensor events.
    """
    if GPIO.input(channel):
        print("Motion detected!")
    else:
        print("No motion detected.")


if __name__ == '__main__':
    try:
        # Set up the GPIO and PIR sensor
        setup_gpio(PIR_PIN)

        # Keep the script running to listen for motion events
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    finally:
        # Clean up GPIO settings
        GPIO.cleanup()
