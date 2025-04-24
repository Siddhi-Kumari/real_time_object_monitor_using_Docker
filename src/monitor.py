class SceneMonitor:
    def __init__(self):
        self.previous_objects = set()

    def analyze(self, detections):
        current_objects = set([d['class'] for d in detections])
        missing = self.previous_objects - current_objects
        new = current_objects - self.previous_objects
        self.previous_objects = current_objects
        return missing, new
