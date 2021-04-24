#!/usr/bin/env python3

import concurrent.futures
from queue import Queue

from Drive import Drive
from LineController import LineController
from CameraReader import CameraReader



# camera_sensor_func
# Since the for loop is needed from the reader get_stream slightly different
# than the line sensor reader
# @param sensor_bus - the bus to send output camera frames to the interpretor
def camera_sensor_func(sensor_bus, reader_stream, time_delay):
    for frame in reader_stream:
        # publish sensor data
        sensor_bus.put(frame)
        time.sleep(time_delay)

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

def cam_interpretor_func(sensor_bus, reader, controller, time_delay):
    while True:
        # Pull all of the frames out of the queue
        frame = None
        while not sensor_bus.empty():
            frame = sensor_bus.get()
            sensor_bus.task_done()

        if frame is not None:
            reader.set_frame(frame)
            controller.update()

        time.sleep(time_delay)
