import cv2
from src.detector import ObjectDetector
from src.monitor import SceneMonitor
from src.utils import draw_boxes, FPSCounter

# Initialize video capture (using webcam or video file)
cap = cv2.VideoCapture('/app/input/sample.mp4') 

# Check if video is opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Set up the video writer to save the output video to '/app/output'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for .mp4 format
out = cv2.VideoWriter('/app/output/output_video.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# Initialize the detector, monitor, and FPS counter
detector = ObjectDetector()
monitor = SceneMonitor()
fps_counter = FPSCounter()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    detections = detector.detect(frame)

    # Analyze the scene for missing and new objects
    missing, new = monitor.analyze(detections)

    # Draw bounding boxes and labels on the frame
    frame = draw_boxes(frame, detections)

    # Calculate and display FPS
    fps = fps_counter.update()
    cv2.putText(frame, f'FPS: {fps}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    if missing:
        cv2.putText(frame, f'Missing: {missing}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    if new:
        cv2.putText(frame, f'New: {new}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    # Write the processed frame to the output video
    out.write(frame)

# Release the video capture and writer
cap.release()
out.release()


cv2.destroyAllWindows()

print("Processing completed. Output video saved to '/app/output/output_video.mp4'")
