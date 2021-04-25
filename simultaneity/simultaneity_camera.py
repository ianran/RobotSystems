#!/usr/bin/env python3

import sys
import time

sys.path.append('..')

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



def main():
    drive = Drive()
    reader = CameraReader()
    controller = LineController(reader, drive)

    que = Queue()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        eSensor = executor.submit(camera_sensor_func, que, reader.get_stream(), 0.05)
        eInterpreter = executor.submit(cam_interpretor_func, que, reader, controller, 0.05)

    eSensor.result()

if __name__ == '__main__':
    main()
