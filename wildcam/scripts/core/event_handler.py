from hardware.camera_module import CameraModule
from hardware.pir_sensor import PIRSensor
from typing import Literal


class EventHandler:
    """
    Handles system events for the WildCam.
    Processes motion detection, update cycles, and config mode activation.
    """

    def __init__(self) -> None:
        """Initialize EventHandler with required modules."""
        self._record_type: Literal["image", "video"] = "image"  # Temporary fixed value
        self.camera = CameraModule()
        self.pir_sensor = PIRSensor()

    def set_interrupts(self, state: bool) -> None:
        """Enable or disable motion detection interrupts."""
        if state:
            self.pir_sensor.set_interrupt(self.handle_motion_event)
        else:
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

    # TODO: Implement methods for update cycles and configuration mode activation
    # def handle_update_cycle(self):
    #     pass

    # def handle_config_mode(self):
    #     pass
