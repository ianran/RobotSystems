# Ultrasonic.py
# Written Ian Rankin - 2021
#
# A class to handle the Ultrasonic sensor. Mostly a straight port of the ezblock
# class


import picarx_improved as car
import time

import pdb

class Ultrasonic():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Ultrasonic, cls).__new__(cls)

            # init stuff
            cls.trig = car.Pin('D0')
            cls.echo = car.Pin('D1')
            cls.ultra = car.Ultrasonic(cls.trig, cls.echo)


        # end if for lazy initialization
        return cls._instance

    def read(self):
        return self.ultra.read()


if __name__ == '__main__':
    # Test function
    ultra = Ultrasonic()

    while True:
        v = ultra.read()
        print(v)
        time.sleep(0.25)
