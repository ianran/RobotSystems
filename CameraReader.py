from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array


class CameraReader():
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 20

        self.rawCapture = PiRGBArray(camera, size=(640, 480))

        time.sleep(0.1)





if __name__ == '__main__':
    reader.CameraReader()

    # capture frames from the camera
    for frame in reader.camera.capture_continuous(reader.rawCapture, format="bgr", use_video_port=True):
    	# grab the raw NumPy array representing the image, then initialize the timestamp
    	# and occupied/unoccupied text
    	image = frame.array

        


        reader.rawCapture.truncate(0)
