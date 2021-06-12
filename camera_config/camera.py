from threading import Thread, Lock
import cv2

class CameraStream:

    """
        Threaded class for capturing camera stream quickly in real time, media decoder: FFMPEG

        objective: 
            to capture each frame smoothly without any delay
        
        return:
            return each frame
    """

    def __init__(self, src=0, width=800, height=600):

        """
            constructor function of class CameraStream

            arguments:
                src: type - int/string, source of camera. int if webcam else string if ipcam/ptz/other stream sources, default 0 for webcam
                width: type - int, camera feed width
                height: type - int, camera feed height
            
            return:
                none

        """

        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        (self.isGrabbed, self.frame) = self.stream.read()
        self.isStarted = False
        self.lock = Lock()

    def start(self):

        """
            thread start function of class CameraStream

            arguments:
                none

            return:
                return to self instance

        """

        if self.isStarted:
            print("Camera Reading Thread Already Started!")
            return None
        self.isStarted = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):

        """
            update thread for continuous frame reading of class CameraStream

            arguments:
                none

            return:
                return to self instance

        """

        while self.isStarted:
            (isGrabbed, frame) = self.stream.read()
            self.lock.acquire()
            self.isGrabbed, self.frame = isGrabbed, frame
            self.lock.release()
        if self.isStarted == False:
            return

    def read(self):

        """
            reading thread to return each frame towards driver class/function of class CameraStream

            arguments:
                none

            return: 
                ret: type - bool, if camera stream available return true, return false otherwise
                frame: type - np.array, return numpy array of each frame.
        """

        self.lock.acquire()
        ret = self.isGrabbed
        frame = self.frame.copy()
        self.lock.release()
        return ret, frame

    def stop(self):

        """
            thread stopper of CameraStream

            arguments:
                none
            
            return:
                none

        """

        self.isStarted = False
        self.thread.join()
        self.stream.release()

    def __exit__(self, exc_type, exc_value, traceback):

        """
            destroyer of the thread class of CameraStream
        """
        self.stream.release()