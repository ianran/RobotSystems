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
    light_sensor = LightSensor()

    #controller = LineController(light_sensor, drive)





    while True:
        brightness = light_sensor.read()
        print(brightness)
        time.sleep(0.5)

    print('Quiting')
