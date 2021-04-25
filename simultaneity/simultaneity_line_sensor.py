#!/usr/bin/env python3

import sys
import time

sys.path.append('..')

import concurrent.futures
from queue import Queue

from Drive import Drive
from LineController import LineController
from LightSensor import LightSensor




def line_sensor_func(sensor_bus, line_sensor, time_delay):
    while True:
        pass

def line_intepreter_func(sensor_bus, controller, time_delay):
    frame = None
    while not sensor_bus.empty():
        frame = sensor_bus.get()
        sensor_bus.task_done()

    if frame is not None:
        controller.update(loc=frame)

    time.sleep(time_delay)


def main():
    drive = Drive()
    light_sensor = LightSensor()
    controller = LineController(light_sensor, drive)

    que = Queue()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        eSensor = executor.submit(line_sensor_func, que, light_sensor, 0.05)
        eInterpreter = executor.submit(line_intepreter_func, que, controller, 0.05)

    eSensor.result()

if __name__ == '__main__':
    main()
