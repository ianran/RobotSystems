from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


class CameraReader():
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 20

        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))

        time.sleep(0.1)





if __name__ == '__main__':
    reader = CameraReader()

    # capture frames from the camera
    for frame in reader.camera.capture_continuous(reader.rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array      

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([90,150,130])
        upper_blue = np.array([110,255,190])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        #print(mask.shape)
        small_mask = mask[300:350,:]
        ret, small_mask = cv2.threshold(small_mask, 127,255,0)

        #contours = cv2.

        M = cv2.moments(small_mask)
        if M['m00'] == 0:
            cX = None
            cY = None
        else:
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
        #print(M)
        print(cX)
        print(cY)

        cv2.imshow('Frame', small_mask)
        key=cv2.waitKey(1) & 0xFF

        reader.rawCapture.truncate(0)
