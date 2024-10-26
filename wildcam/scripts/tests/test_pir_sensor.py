import RPi.GPIO as GPIO
import time


# GPIO pin for the PIR sensor
PIR_PIN = 18


def setup_gpio(pin):
    """
    Set up the GPIO pin for input and event detection.
    """
    try:
        GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
        GPIO.setup(pin, GPIO.IN)  # Set the pin as input
        GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300)  # Detect both motion and no motion
        GPIO.add_event_callback(pin, motion_event_handler)  # Assign callback function
    except RuntimeError as gpio_runtime_error:
        print(f"Runtime error setting up GPIO: {gpio_runtime_error}")
    except Exception as general_error:
        print(f"Unexpected error in GPIO setup: {general_error}")


def motion_event_handler(channel):
    """
    Callback function triggered on PIR sensor events.
    """
    try:
        if GPIO.input(channel):
            print("Motion detected!")
        else:
            print("No motion detected.")
    except RuntimeError as gpio_runtime_error:
        print(f"Runtime error during motion event handling: {gpio_runtime_error}")
    except Exception as general_error:
        print(f"Unexpected error in motion event handling: {general_error}")


def cleanup_gpio():
    """
    Clean up the GPIO settings.
    """
    try:
        GPIO.remove_event_detect(PIR_PIN)  # Remove event detection
        GPIO.cleanup()  # Reset GPIO settings
    except RuntimeError as gpio_runtime_error:
        print(f"Runtime error during GPIO cleanup: {gpio_runtime_error}")
    except Exception as general_error:
        print(f"Unexpected error in GPIO cleanup: {general_error}")
    

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
        cleanup_gpio()
