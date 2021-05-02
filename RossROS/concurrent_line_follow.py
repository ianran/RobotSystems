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
from Producers import LineSensorProd
import rossros as ros



def line_intepreter_func(loc):
    controller.update(loc=loc)



def main():
    bus = ros.Bus(name='location_bus', initial_message=-1)
    delay = 0.05
    #sensor_prod = ros.Producer(producer_function=line_sensor_func, \
    #                    output_busses=bus, \
    #                    delay=delay, name='sensor_reader')
    #sensor_prod = ros.Timer(bus, delay=0.25, name='sensor_reader')
    sensor_prod = LineSensorProd(bus, delay=0.25)
    controller_cons = ros.Consumer(line_intepreter_func, bus, delay=0.5, name='interpreter')
    #controller_cons = ros.Printer(bus, delay=0.5, name='pri')


    ros.runConcurrently([sensor_prod, controller_cons])


if __name__ == '__main__':
    drive = Drive()
    light_sensor = LightSensor()
    controller = LineController(light_sensor, drive)

    logging.basicConfig(level=logging.INFO)

    main()
