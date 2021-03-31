import cv2

class Stream:
    def __init__(self, source):
        self.video_source = cv2.VideoCapture(source)

    def return_frame(self):
        ret, frame = self.video_source.read()
        while(ret):
            ret, frame = self.video_source.read()
            re, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tostring() + b'\r\n\r\n')