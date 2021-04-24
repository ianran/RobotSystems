#!/usr/bin/env python3

import sys
import time
sys.path.append('..')

import concurrent.futures
from queue import Queue

from Drive import Drive
from LineController import LineController
from CameraReader import CameraReader

from simultanity_helper import camera_sensor_func, cam_interpretor_func




def main():
    drive = Drive()
    reader = CameraReader()
    controller = LineController(reader, drive)


    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        eSensor = executor.submit(camera_sensor_func, 0.05)
        eInterpreter = executor.submit(cam_interpretor_func, reader, controller, 0.05)

    eSensor.result()

if __name__ == '__main__':
    main()
