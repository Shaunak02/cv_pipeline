# 🎥 Computer Vision Pipeline with YOLOv8

A modular video processing pipeline that performs **object detection** on video streams using **YOLOv8** and OpenCV. The pipeline loads a video, detects objects frame-by-frame, annotates them, and saves the output.

---

## 📁 Project Structure

```text
cv_pipeline/
├── input/              # Input videos
├── output/             # Annotated output videos
├── pipeline/           # Core modules
│   ├── loader.py       # Video loading
│   ├── detector.py     # YOLOv8 object detection
│   ├── visualizer.py   # Bounding box and label drawing
│   └── writer.py       # Output video writer
├── main.py             # Pipeline entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- ✅ Modular, readable design
- 🎯 Real-time object detection with YOLOv8 (`ultralytics`)
- 🎞 Frame-by-frame annotation with class labels and confidence
- 💾 Output video saved with bounding boxes

---

## 🔧 Setup

1. **Clone the repo and create a virtual environment**
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
3. **Download YOLOv8 model (optional)**
The model will be downloaded automatically if not present:
   ```bash
   from ultralytics import YOLO
   YOLO('yolov8n.pt')
4. **Place a sample video in /input**
Example: input/sample.mp4

---

## ▶️ Run the Pipeline
   ```bash
   python main.py
   ```
- Output video will be saved to: output/annotated_output.mp4


---


## 📚 Dependencies
- Python 3.8+
- OpenCV
- Ultralytics YOLOv8

Install with:
```bash
pip install ultralytics opencv-python
```
---

## 📌 Notes
- You can swap the model or add tracking (e.g., Deep SORT) easily thanks to the modular layout.
- Tracking and webcam support planned as future extensions.

---

Let me know if you’d like to add:
- A demo GIF or screenshot
- Instructions for webcam or batch mode
- Or a section on optional tracking extension (SORT/Deep SORT)






