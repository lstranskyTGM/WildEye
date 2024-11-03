from picamera2 import Picamera2
import time


def initialize_camera(mode="image"):
    """
    Initialize and configure the camera
    """
    picam2 = Picamera2()  # Initialize the camera
    if mode == "image":
        config = picam2.create_still_configuration()  # Configure for still capture
    elif mode == "video":
        config = picam2.create_video_configuration()  # Configure for video capture
    else:
        raise ValueError("Invalid mode. Use 'image' or 'video'.")
    
    picam2.configure(config)  # Apply configuration
    return picam2


def capture_image():
    """
    Capture an image using the camera.
    """
    picam2 = None  # Ensure picam2 is defined before the try block
    try:
        picam2 = initialize_camera(mode="image")  # Initialize for still capture
        picam2.start()  # Start the camera
        time.sleep(2)  # Wait for the camera to warm up
        picam2.capture_file("test.jpg")  # Capture and save the image
        print("Image captured successfully!")
    except Exception as error:
        print(f"Error capturing image: {error}")
    finally:
        if picam2:
            picam2.stop()  # Ensure the camera is stopped


def capture_video(duration=5):
    """
    Capture a video using the camera.
    """
    picam2 = None  # Ensure picam2 is defined before the try block
    try:
        picam2 = initialize_camera(mode="video")  # Initialize for video capture
        picam2.start()  # Start the camera
        picam2.start_recording("test.mp4")  # Start recording the video
        time.sleep(duration)  # Record video for the specified duration
        picam2.stop_recording()  # Stop recording the video
        print(f"Video recorded for {duration} seconds.")
    except Exception as error:
        print(f"Error capturing video: {error}")
    finally:
        if picam2:
            picam2.stop()  # Ensure the camera is stopped


if __name__ == '__main__':
    # Test camera image capture and video recording
    print("Capturing image...")
    capture_image()
    
    print("Capturing video...")
    capture_video(duration=5)
