# --------- BACKEND: video_logger.py ---------
import cv2
from datetime import datetime
import os

def record_video_with_metadata(name, location):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"attendance_data/videos/{name}_{timestamp}.avi"

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    frame_count = 0
    max_frames = 100  # approx 5 seconds

    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            frame_count += 1
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Optionally log the video file metadata
    print(f"[INFO] Video saved: {filename} with location: {location}")
