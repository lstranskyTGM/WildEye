from picamera2 import Picamera2
import time
import os
from datetime import datetime
from .base_module import BaseModule, requires_initialization


class CameraModule(BaseModule):
    """
    Controls camera operations such as capturing photos or recording videos.
    Uses the Waveshare 12076 RPi IR-CUT Camera.
    
    Attributes:
        camera (Picamera2): The camera object for capturing images or recording videos.
        
    Methods:
        initialize(): Initializes the camera module.
        configure_camera(mode): Configures the camera for image or video capture.
        capture_image(): Captures an image and saves it with a timestamp.
        record_video(duration): Records a video and saves it with a timestamp.
        generate_file_path(file_type, base_dir): Generates a file path based on the type.
        cleanup(): Releases camera resources when shutting down.
    """

    def __init__(self) -> None:
        """Initializes base attributes but does not start the camera yet."""
        super().__init__()
        self.camera = None
        
    def initialize(self) -> None:
        """Initialize the camera module."""
        self.camera = Picamera2()
        self._initialized = True

    @requires_initialization
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

    @requires_initialization
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
            file_path = self.generate_file_path("image")
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            #time.sleep(2)
            self.camera.capture_file(file_path)
            self.camera.stop()
            return file_path
        except Exception as e:
            print(f"Error capturing image: {e}")
            return None

    @requires_initialization
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
            file_path = self.generate_file_path("video")
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            #time.sleep(2)
            self.camera.start_recording(file_path)
            time.sleep(duration)
            self.camera.stop_recording()
            self.camera.stop()
            return file_path
        except Exception as e:
            print(f"Error recording video: {e}")
            return None
        
    def generate_file_path(self, file_type: str, base_dir: str = "../media/upload_queue") -> str:
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
            return os.path.join(base_dir, "images", f"image_{timestamp}.jpg")
        elif file_type == "video":
            return os.path.join(base_dir, "videos", f"video_{timestamp}.h264")
        else:
            raise ValueError("Invalid file type. Choose 'image' or 'video'.")
        
    def cleanup(self) -> None:
        """Release camera resources when shutting down."""
        if self.camera:
            self.camera.close()
            self.camera = None
        self._initialized = False
