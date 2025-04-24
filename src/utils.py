import cv2
import time

def draw_boxes(frame, detections):
    for d in detections:
        x1, y1, x2, y2 = map(int, d['bbox'])
        label = str(d['class'])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    return frame

class FPSCounter:
    def __init__(self):
        self.prev = time.time()

    def update(self):
        now = time.time()
        fps = 1 / (now - self.prev)
        self.prev = now
        return round(fps, 2)
