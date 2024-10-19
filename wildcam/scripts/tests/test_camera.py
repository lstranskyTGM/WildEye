from picamera2 import Picamera2
import time


def test_camera_image():
    """Capture an image using the camera."""
    picam2 = Picamera2()  # Initialize the camera
    config = picam2.create_still_configuration()  # Configure for still capture
    picam2.configure(config)  # Apply configuration
    picam2.start()  # Start the camera
    time.sleep(2)  # Wait to allow the camera to start up
    picam2.capture_file("test.jpg")  # Capture and save the image
    picam2.stop()  # Stop the camera

def test_camera_video():
    """Capture a video using the camera."""
    picam2 = Picamera2()  # Initialize the camera
    config = picam2.create_video_configuration()  # Configure for video capture
    picam2.configure(config)  # Apply configuration
    picam2.start()  # Start the camera
    picam2.start_recording("test.mp4")  # Start recording the video
    time.sleep(5)  # Record video for 5 second
    picam2.stop_recording()  # Stop recording the video
    picam2.stop()  # Stop the camera


if __name__ == '__main__':
    test_camera_image()
    test_camera_video()
