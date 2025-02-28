import RPi.GPIO as GPIO
from typing import Callable
from .base_module import BaseModule, requires_hardware_setup


class PIRSensor(BaseModule):
    """
    Handles motion detection using a PIR sensor (Grove Digital PIR Motion Sensor).
    
    Attributes:
        pin (int): The GPIO pin where the PIR sensor is connected.
    
    Methods:
        hardware_setup(): Sets up the PIR sensor.
        set_interrupt(callback, bouncetime): Adds an interrupt to detect motion.
        cleanup(): Releases GPIO resources when shutting down.
    """

    def __init__(self, pin=17) -> None:
        """Initializes base attributes."""
        super().__init__()
        self.pin = pin
    
    def hardware_setup(self) -> None:
        """Sets up the PIR sensor."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self._hardware_configured = True
        
    @requires_hardware_setup
    def set_interrupt(self, callback: Callable[[int], None], bouncetime: int = 300) -> None:
        """
        Add an interrupt to detect motion on the specified GPIO pin.
        
        Args:
            callback (Callable[[int], None]): The callback function to execute on motion detection.
            bouncetime (int): Debounce time in milliseconds (default: 300).
        """
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=callback, bouncetime=bouncetime)
        print(f"Motion detection interrupt added on GPIO pin {self.pin}.")

    def cleanup(self) -> None:
        """Cleanup GPIO resources."""
        if GPIO.event_detected(self.pin):
            GPIO.remove_event_detect(self.pin)
        GPIO.cleanup(self.pin)
        self._hardware_configured = False
