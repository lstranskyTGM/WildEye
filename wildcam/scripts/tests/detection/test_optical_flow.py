import cv2
import numpy as np


def initialize_camera(index=0):
    """Initialize the camera for video capture."""
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise Exception("Could not open video device")
    return cap


def detect_features(frame_gray, max_corners=100, quality_level=0.3, min_distance=7, block_size=7):
    """Detect good features to track in a grayscale frame using Shi-Tomasi corner detection."""
    feature_params = dict(maxCorners=max_corners, qualityLevel=quality_level,
                          minDistance=min_distance, blockSize=block_size)
    return cv2.goodFeaturesToTrack(frame_gray, mask=None, **feature_params)


def calculate_optical_flow(old_gray, frame_gray, p0, win_size=(15, 15), max_level=2, criteria_eps=0.03,
                           criteria_count=10):
    """Calculate optical flow using Lucas-Kanade method."""
    lk_params = dict(winSize=win_size, maxLevel=max_level,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, criteria_count, criteria_eps))
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    return p1, st, err


def draw_tracks(frame, mask, good_old, good_new):
    """Draws the tracks of detected points from previous position to new position."""
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask.copy(), (a, b), (c, d), color[i].tolist())
        frame = cv2.circle(frame.copy(), (a, b), 5, color[i].tolist(), -1)
    return mask


def main():
    cap = initialize_camera()

    # Get frame dimensions
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('optical_flow_output.avi', fourcc, 20.0, (frame_width, frame_height))

    # Create some random colors for visualization
    global color
    color = np.random.randint(0, 255, (100, 3))

    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    if not ret:
        raise Exception("Failed to capture initial frame")

    old_gray = cv2.cvtColor(old_frame.copy(), cv2.COLOR_BGR2GRAY)
    p0 = detect_features(old_gray)

    # Create a mask image for drawing purposes
    mask = np.zeros_like(old_frame)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

        # Calculate optical flow
        p1, st, err = calculate_optical_flow(old_gray.copy(), frame_gray.copy(), p0)

        # Select good points
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Draw the tracks
        mask = draw_tracks(frame.copy(), mask.copy(), good_old.copy(), good_new.copy())

        img = cv2.add(frame.copy(), mask.copy())

        # Write the frame into the file
        out.write(img)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

        # Update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
