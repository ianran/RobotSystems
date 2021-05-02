# concurrent_line_follow.py
# Written Ian Rankin - 2021
#
# re-implement the concurrent program using RossROS

import sys

import logging


sys.path.append('..')

from Drive import Drive
from LineController import LineController
from LightSensor import LightSensor
from Producers import LineSensorProd, UltrasonicProd

import rossros as ros


def line_intepreter_func(loc, distance):
    if distance < 15: # 15 centimeters I think
        speed = 0
    else:
        speed = 10

    logging.info('line')
    controller.update(loc=loc, forward_speed=speed)




def main():
    bus = ros.Bus(name='location_bus', initial_message=-1)
    ultra_bus = ros.Bus(name='ultra_bus', initial_message=-1)
    delay = 0.05

    sensor_prod = LineSensorProd(bus, delay=delay)
    ultra_prod = UltrasonicProd(ultra_bus, delay=delay)

    controller_cons = ros.Consumer(line_intepreter_func, [bus, ultra_bus], \
                delay=delay, name='interpreter')


    ros.runConcurrently([sensor_prod, ultra_prod, controller_cons])


if __name__ == '__main__':
    drive = Drive()
    light_sensor = LightSensor()
    controller = LineController(light_sensor, drive)

    logging.basicConfig(level=logging.INFO)

    main()
