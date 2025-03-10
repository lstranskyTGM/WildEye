from picamera2 import Picamera2
import time
import os
from datetime import datetime
from .base_module import BaseModule, requires_hardware_setup


class CameraModule(BaseModule):
    """
    Controls camera operations such as capturing photos or recording videos.
    Uses the Waveshare 12076 RPi IR-CUT Camera.
    
    Attributes:
        camera (Picamera2): The camera object for capturing images or recording videos.
        
    Methods:
        hardware_setup(): Sets up the camera module.
        configure_camera(mode): Configures the camera for image or video capture.
        capture_image(): Captures an image and saves it with a timestamp.
        _record_video(duration): Records a video and saves it with a timestamp.
        generate_file_path(file_type, base_dir): Generates a file path based on the type.
        cleanup(): Releases camera resources when shutting down.
    """

    def __init__(self) -> None:
        """Initializes base attributes."""
        super().__init__()
        self.camera = None
        
    def hardware_setup(self) -> None:
        """Sets up the camera module."""
        self.camera = Picamera2()
        self._hardware_configured = True

    @requires_hardware_setup
    def configure_camera(self, mode: str) -> None:
        """
        Configures the camera for the specified mode.

        Args:
            mode (str): The mode to configure the camera for (image or video).
        """
        if mode == "image":
            self.config = self.camera.create_still_configuration()
        elif mode == "video":
            self.config = self.camera.create_video_configuration()
        else:
            raise ValueError("Invalid mode. Choose 'image' or 'video'.")
        self.camera.configure(self.config)

    @requires_hardware_setup
    def capture_image(self) -> str | None:
        """
        Capture an image and save it to the specified file path.

        Args:
            file_path (str): The file path where the image will be saved.
        
        Returns:
            str | None: The full file path if successful, otherwise None.
        """
        try:
            self.configure_camera("image")
            self.camera.start()
            file_path = self._generate_file_path("image")
            #time.sleep(2)
            self.camera.capture_file(file_path)
            return file_path
        except Exception as e:
            print(f"Error capturing image: {e}")
            return None
        finally:
            if self.camera:
                self.camera.stop()

    @requires_hardware_setup
    def record_video(self, duration: int = 5) -> str | None:
        """
        Record a video and save it to the specified file path.

        Args:
            file_path (str): The file path where the video will be saved.
            duration (int): Duration of the video in seconds.
        
        Returns:
            str | None: The full file path if successful, otherwise None.
        """
        try:
            self.configure_camera("video")
            self.camera.start()
            file_path = self._generate_file_path("video")
            #time.sleep(2)
            self.camera.start_recording(file_path)
            time.sleep(duration)
            self.camera.stop_recording()
            return file_path
        except Exception as e:
            print(f"Error recording video: {e}")
            return None
        finally:
            if self.camera:
                self.camera.stop()
        
    def _generate_file_path(self, file_type: str, base_dir: str = "media/upload_queue") -> str:
        """
        Generate a full file path for the specified file type.
        
        Args:
            file_type (str): The type of file to generate a name for (image or video).
            base_dir (str): The base directory where the file will be saved.
            
        Returns:
            str: The full file path for the specified file type.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if file_type == "image":
            file_path = os.path.join(base_dir, "images", f"image_{timestamp}.jpg")
        elif file_type == "video":
            file_path = os.path.join(base_dir, "videos", f"video_{timestamp}.h264")
        else:
            raise ValueError("Invalid file type. Choose 'image' or 'video'.")
        
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")
            
        return file_path

    def cleanup(self) -> None:
        """Release camera resources when shutting down."""
        if self.camera:
            self.camera.close()
            self.camera = None
        self._hardware_configured = False
