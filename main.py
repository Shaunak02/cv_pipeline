# main.py
from pipeline.loader import VideoLoader
from pipeline.detector import YOLOv8Detector
from pipeline.visualizer import draw_boxes
from pipeline.writer import VideoWriter

def main():
    input_video = "input/pedestrian.mp4"
    output_video = "output/pedestrian_annot.mp4"

    # Initialize modules
    loader = VideoLoader(input_video)
    writer = VideoWriter(output_video, loader.fps, loader.frame_size)
    detector = YOLOv8Detector()

    # Process each frame
    for frame in loader:
        detections = detector.predict(frame)
        annotated_frame = draw_boxes(frame, detections)
        writer.write(annotated_frame)

    # Release resources
    loader.release()
    writer.release()
    print("✅ Video processing complete.")

if __name__ == "__main__":
    main()
