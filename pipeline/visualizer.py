import cv2

def draw_boxes(frame, detections):
    """
    Draws bounding boxes and labels on the frame.
    
    Args:
        frame: The image (BGR) to draw on.
        detections: A list of dicts with 'bbox', 'label', and 'conf'.
    
    Returns:
        Annotated frame with boxes and labels drawn.
    """
    for det in detections:
        x1, y1, x2, y2 = det['bbox']     # Bounding box coordinates
        label = det['label']             # Class name
        conf = det['conf']               # Confidence score

        # Draw rectangle around the object
        cv2.rectangle(frame, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=4)

        # Compose label text: class name + confidence
        text = f"{label} {conf:.2f}"

        # Put label text above the box
        cv2.putText(frame, text, (x1, y1 - 15), 
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                    fontScale=1.5, color=(255, 0, 0), thickness=2)

    return frame
