#!/usr/bin/env python3
#

import sys
import time
sys.path.append('..')

from Drive import Drive
#from LineController import LineController
from CameraReader import CameraReader
import time

if __name__ == '__main__':
    drive = Drive()
    reader = CameraReader()

    controller = LineController(light_sensor, drive)

    for frame in reader.get_stream():
        reader.set_frame(frame)
        servo_angle = controller.update()

        

    print('Quiting')
