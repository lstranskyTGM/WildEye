from hardware.camera_module import CameraModule
from hardware.pir_sensor import PIRSensor
from typing import Literal


class EventHandler:
    """
    Handles system events for the WildCam.
    Processes motion detection, update cycles, and config mode activation.
    
    Attributes:
        _record_type (Literal["image", "video"]): The type of media to record (image or video).
        camera (CameraModule): The camera module for capturing media.
        pir_sensor (PIRSensor): The PIR sensor module for motion detection.
    
    Methods:
        set_interrupts(state): Enable or disable motion detection interrupts.
        handle_motion_event(): Handle motion detection event and trigger media capture.
        handle_update_cycle(): Handle the update cycle event.
        handle_config_mode(): Handle the configuration mode activation event
    """

    def __init__(self) -> None:
        """Initialize EventHandler with required modules."""
        self._record_type: Literal["image", "video"] = "image"  # Temporary fixed value
        self.camera = CameraModule()
        self.pir_sensor = PIRSensor()

    def set_interrupts(self, state: bool) -> None:
        """
        Enable or disable motion detection interrupts.
        
        Args:
            state (bool): True to enable interrupts, False to disable.
        """
        if state:
            self.camera.hardware_setup()
            self.pir_sensor.hardware_setup()
            self.pir_sensor.set_interrupt(self.handle_motion_event)
        else:
            self.camera.cleanup()
            self.pir_sensor.cleanup()

    def handle_motion_event(self, channel: int) -> None:
        """
        Handle motion detection event and trigger media capture.
        
        Args:
            channel (int): The GPIO channel where the event occurred.
        """
        print("Motion detected! Capturing media...")

        if self._record_type == "image":
            file_path = self.camera.capture_image()
        elif self._record_type == "video":
            file_path = self.camera.record_video(10)
        else:
            print(f"Invalid record_type '{self._record_type}' passed to handle_motion_event.")
            return

        if file_path:
            print(f"{self._record_type.capitalize()} saved at {file_path}")
        else:
            print(f"Error: {self._record_type.capitalize()} capture failed.")

    # TODO: Implement the following methods
    def handle_update_cycle(self) -> None:
        """Handle the update cycle event."""
        pass

    def handle_config_mode(self) -> None:
        """Handle the configuration mode activation event."""
        pass
