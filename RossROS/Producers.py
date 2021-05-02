# Producers.py
# Written Ian Rankin - 2021
#
# producers classes

from LightSensor import LightSensor
from Ultrasonic import Ultrasonic

import rossros as ros

class LineSensorProd(ros.Producer):
    def __init__(self, bus, delay):
        super().__init__(
            self.line_sensor_func,
            bus,
            delay=delay,
            termination_busses=ros.default_termination_bus,
            name='light_prod')

        self.line_sensor = LightSensor()


    def line_sensor_func(self):
        loc = self.line_sensor.get()
        return loc #self.line_sensor.get()


class UltrasonicProd(ros.Producer):
    def __init__(self, bus, delay):
        super().__init__(
            self.ultra_func,
            bus,
            delay=delay,
            termination_busses=ros.default_termination_bus,
            name='ultrasonic_prod')

        self.ultra = Ultrasonic()


    def ultra_func(self):
        inches = self.ultra.read()
        return inches
