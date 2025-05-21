from ultralytics import YOLO
import numpy as np

class YOLOv8Detector:
    def __init__(self, model_path='yolov8n.pt'):
        # Load the YOLOv8 model (default: smallest pre-trained model)
        self.model = YOLO(model_path)

    def predict(self, frame):
        # Run inference on the frame using YOLO
        results = self.model(frame)[0]

        # Extract detection results: bounding boxes, confidences, and class IDs
        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)  # Bounding box
            conf = float(box.conf[0])                               # Confidence score
            cls_id = int(box.cls[0])                                # Class ID
            label = self.model.names[cls_id]                        # Class name (label)

            detections.append({
                'bbox': (x1, y1, x2, y2),
                'conf': conf,
                'label': label
            })

        return detections
