from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_name='yolov8n.pt'):
        self.model = YOLO(model_name)

    def detect(self, frame):
        results = self.model(frame)[0]
        boxes = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            cls = int(box.cls)
            conf = float(box.conf)
            boxes.append({'bbox': (x1.item(), y1.item(), x2.item(), y2.item()), 'class': cls, 'conf': conf})
        return boxes
