#!/usr/bin/env python3
#

import sys
import time
sys.path.append('..')

from Drive import Drive
from LightSensor import LightSensor
from LineController import LineController
import time

if __name__ == '__main__':
    drive = Drive()
    light_sensor = LightSensor()

    controller = LineController(light_sensor, drive)

    while True:
        servo_angle = controller.update()
        print(servo_angle)
        time.sleep(0.05)

    print('Quiting')
