from picamera2 import Picamera2
import cv2
import time


def initialize_camera(mode="video"):
    """
    Initialize and configure the camera
    """
    picam2 = Picamera2()
    if mode == "image":
        config = picam2.create_still_configuration()  # Configure for still capture
    elif mode == "video":
        config = picam2.create_video_configuration()  # Configure for video capture
    else:
        raise ValueError("Invalid mode. Use 'image' or 'video'.")
    
    picam2.configure(config)
    return picam2


def setup_background_subtractor():
    """
    Initializes the background subtractor with default parameters.
    """
    return cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)


def process_frame(frame, background_subtractor):
    """
    Applies background subtraction to a single frame and processes the mask for noise reduction.
    """
    # Apply background subtraction
    fg_mask = background_subtractor.apply(frame)
    
    # Perform noise reduction using morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
    
    return fg_mask


if __name__ == "__main__":
    # Initialize camera and background subtractor
    picam2 = initialize_camera(mode="video")
    background_subtractor = setup_background_subtractor()
    
    # Start the camera and allow it to warm up
    picam2.start()
    time.sleep(2)
    
    try:
        while True:
            frame = picam2.capture_array()
            
            # Resize frame if necessary for faster processing
            frame_resized = cv2.resize(frame, (640, 480))
            
            # Convert to grayscale (optional, if needed for better contrast)
            gray_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            
            # Process the frame using background subtraction
            fg_mask = process_frame(gray_frame, background_subtractor)

            # Display the original frame and foreground mask
            cv2.imshow('Original Frame', frame_resized)
            cv2.imshow('Foreground Mask', fg_mask)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Clean up resources
        picam2.stop()
        cv2.destroyAllWindows()
