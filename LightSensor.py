# LightSensor.py
# Written Ian Rankin - April 2021
#
# A class to handle LightSensors from the picar



import picarx_improved as car
from LineInterpreter import LineInterpreter
import time
from math import sqrt
from statistics import mean, variance

from threading import Lock

class LightSensor(LineInterpreter):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LightSensor, cls).__new__(cls)

            # init stuff
            cls.A0 = car.ADC('A0')
            cls.A1 = car.ADC('A1')
            cls.A2 = car.ADC('A2')
            cls.lock = Lock()

            cls._instance.calibrate(1.0)
            cls.light_transitions = True
            cls.std_away = 4


        # end if for lazy initialization
        return cls._instance

    def calibrate(self, time=1.0):
        vals_0 = []
        vals_1 = []
        vals_2 = []

        iterations = int(1.0/0.02)

        for i in range(iterations):
            vals = self.read()
            vals_0.append(vals[0])
            vals_1.append(vals[1])
            vals_2.append(vals[2])

        self.mean = [mean(vals_0), mean(vals_1), mean(vals_2)]
        self.std = [variance(vals_0), variance(vals_1), variance(vals_2)]
        self.std = [sqrt(s) for s in self.std]


    # read
    # This function pulls the ADC objects and returns the calibrated values
    #
    # @return - returns the analog values for the light sensor.
    def read(self):
        self.lock.acquire()
        val_0 = self.A0.read()
        val_1 = self.A1.read()
        val_2 = self.A2.read()
        self.lock.release()

        return [val_0, val_1, val_2]

    def read_transition(self):
        vals = self.read()


        for i in range(3):
            if self.std[i] < 1:
                self.std[i] = 1
            vals[i] = (vals[i] - self.mean[i]) / self.std[i]

        if self.light_transitions:
            return [v > self.std_away for v in vals]
        else:
            return [v < self.std_away for v in vals]






    # get
    # @override
    # This function overrides LineInterpreter
    #
    # @return - [-1, 1] output of where line is, or None if the line is not detected.
    def get(self):
        trans = self.read_transition()

        sum = 0
        total = 0
        for i in range(3):
            if trans[i]:
                sum += i+1
                total += 1

        if sum == 0:
            return None
        mean = sum/total
        return mean - 2














#
