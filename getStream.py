import os
import cv2
from camera_config.camera import CameraStream

class Stream:
    def __init__(self, source):
        self.video_source = CameraStream(source).start()


    def return_frame(self):
        ret, frame = self.video_source.read()
        while(ret):
            re, jpeg = cv2.imencode('.jpg', frame)
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tostring() + b'\r\n\r\n'
            ret, frame = self.video_source.read()
