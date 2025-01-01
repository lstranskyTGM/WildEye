import RPi.GPIO as GPIO
import time

# GPIO pin for the PIR sensor
PIR_PIN = 18


def configure_gpio(pin):
    """
    Configure the GPIO pin for the PIR sensor.

    Args:
        pin (int): The GPIO pin number to configure.
    """
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(pin, GPIO.IN)  # Set the pin as input
    print(f"Configured GPIO pin {pin} as input.")


def add_motion_interrupt(pin, callback, bouncetime=300):
    """
    Add an interrupt to detect motion on the specified GPIO pin.

    Args:
        pin (int): The GPIO pin number to monitor.
        callback (function): The callback function to execute on motion detection.
        bouncetime (int): Debounce time in milliseconds (default: 300).
    """
    try:
        GPIO.add_event_detect(pin, GPIO.RISING, callback=callback, bouncetime=bouncetime)
        print(f"Motion detection interrupt added on GPIO pin {pin}.")
    except Exception as error:
        print(f"Error adding interrupt on GPIO pin {pin}: {error}")


def cleanup_gpio():
    """
    Clean up the GPIO settings.
    """
    try:
        GPIO.cleanup()
        print("GPIO settings cleaned up.")
    except Exception as error:
        print(f"Error during GPIO cleanup: {error}")


def motion_detected(channel):
    """
    Callback function triggered when motion is detected.

    Args:
        channel (int): The GPIO channel where the event occurred.
    """
    print("Motion detected!")


def monitor_motion(pin):
    """
    Monitor motion events on the specified GPIO pin until interrupted.

    Args:
        pin (int): The GPIO pin number to monitor.
    """
    try:
        configure_gpio(pin)
        add_motion_interrupt(pin, motion_detected)

        print("PIR Sensor is ready. Waiting for motion...")
        while True:
            time.sleep(1)  # Keep the script running to listen for interrupts

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting...")

    finally:
        cleanup_gpio()


if __name__ == "__main__":
    monitor_motion(PIR_PIN)
