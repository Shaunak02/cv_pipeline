import cv2

class VideoWriter:
    def __init__(self, output_path, fps, frame_size):
        """
        Initializes the video writer with output path, FPS, and frame size.
        
        Args:
            output_path (str): Path to save the annotated video.
            fps (float): Frames per second (from input video).
            frame_size (tuple): (width, height) of video frames.
        """
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 format
        self.writer = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    def write(self, frame):
        """
        Writes a single annotated frame to the output video.
        
        Args:
            frame: Annotated image frame (BGR).
        """
        self.writer.write(frame)

    def release(self):
        """
        Releases the video writer resource.
        """
        self.writer.release()
