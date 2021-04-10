#!/usr/bin/env python3
# Written Ian Rankin - April 2021
#
# A test of the simulated ez block
# NOTE this file must be called from within this folder.
import sys
sys.path.append('..')
import picarx_improved as car
import time


if __name__ == '__main__':
    car.set_motor_speed(1, 0.5)

    adc = car.get_adc_value()
    print(adc)
    car.forward(75, -15)
    time.sleep(0.5)
    car.forward(50, 15)

    time.sleep(5)
