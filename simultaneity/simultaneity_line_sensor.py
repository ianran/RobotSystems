#!/usr/bin/env python3

import sys
import time
sys.path.append('..')

import concurrent.futures
from queue import Queue

from Drive import Drive
from LineController import LineController
from LightSensor import LightSensor

from simultanity_helper import line_sensor_func, line_intepreter_func




def main():
    drive = Drive()
    light_sensor = LightSensor()
    controller = LineController(light_sensor, drive)


    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        eSensor = executor.submit(line_sensor_func, light_sensor, 0.05)
        eInterpreter = executor.submit(line_intepreter_func, controller, 0.05)

    eSensor.result()

if __name__ == '__main__':
    main()
