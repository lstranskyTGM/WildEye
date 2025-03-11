import os
from dotenv import load_dotenv
from hardware.camera_module import CameraModule
from hardware.pir_sensor import PIRSensor
from network.strapi_service import StrapiService
from network.upload_manager import UploadManager
from typing import Literal


class EventHandler:
    """
    Handles system events for the WildCam.
    Processes motion detection, update cycles, and config mode activation.
    
    Attributes:
        _record_type (Literal["image", "video"]): The type of media to record (image or video).
        camera_module (CameraModule): The camera module for capturing media.
        pir_sensor (PIRSensor): The PIR sensor module for motion detection.
        strapi_service (StrapiService): Service for interacting with the Strapi API.
        upload_manager (UploadManager): Manager for uploading files to the server.
    
    Methods:
        set_events(state): Enable or disable all event interrupts based on the state.
        handle_motion_event(): Handle motion detection event and trigger media capture.
        handle_update_cycle(): Handle the update cycle event.
        handle_config_mode(): Handle the configuration mode activation event
    """

    def __init__(self) -> None:
        """Initialize EventHandler with required modules."""
        self._record_type: Literal["image", "video"] = "image"  # Temporary fixed value
        self.camera_module = CameraModule()
        self.pir_sensor = PIRSensor()
        
        # Initialize network services
        load_dotenv()
        api_url = os.getenv("API_URL")
        auth_token = os.getenv("AUTH_TOKEN")
        camera_id = os.getenv("CAMERA_ID")
        
        if not all([api_url, auth_token, camera_id]):
            print("Error: Missing required environment variables.")
        
        self.strapi_service = StrapiService(api_url, auth_token)
        self.upload_manager = UploadManager(self.strapi_service, camera_id)

    def set_events(self, state: bool) -> None:
        """
        Enable or disable all event interrupts based on the state.
        
        Args:
            state (bool): True to enable event interrupts, False to disable.
        """
        if state:
            self.camera_module.hardware_setup()
            self.pir_sensor.hardware_setup()
            self.pir_sensor.set_interrupt(self.handle_motion_event)
        else:
            self.camera_module.cleanup()
            self.pir_sensor.cleanup()

    def handle_motion_event(self, channel: int) -> None:
        """
        Handle motion detection event and trigger media capture.
        
        Args:
            channel (int): The GPIO channel where the event occurred.
        """
        print("Motion detected! Capturing media...")

        if self._record_type == "image":
            file_path = self.camera_module.capture_image()
        elif self._record_type == "video":
            file_path = self.camera_module.record_video(10)
        else:
            print(f"Invalid record_type '{self._record_type}' passed to handle_motion_event.")
            return

        if file_path:
            print(f"{self._record_type.capitalize()} saved at {file_path}")
        else:
            print(f"Error: {self._record_type.capitalize()} capture failed.")

    def handle_update_cycle(self) -> None:
        """Handle the update cycle event."""
        print("Starting update cycle...")
        
        # Upload all pending files
        success = self.upload_manager.upload_files()
        
        if success:
            print("Update cycle completed successfully.")
        else:
            print("Update cycle completed with some failures.")

    # TODO: Implement the following method
    def handle_config_mode(self) -> None:
        """Handle the configuration mode activation event."""
        pass
