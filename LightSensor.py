# LightSensor.py
# Written Ian Rankin - April 2021
#
# A class to handle LightSensors from the picar



import picarx_improved as car
from LineInterpreter import LineInterpreter

class LightSensor(LineInterpreter):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LightSensor, cls).__new__(cls)

            # init stuff
            cls.A0 = car.ADC('A0')
            cls.A1 = car.ADC('A1')
            cls.A2 = car.ADC('A2')

        # end if for lazy initialization
        return cls._instance



    # read
    # This function pulls the ADC objects and returns the calibrated values
    #
    # @return - returns the analog values for the light sensor.
    def read(self):
        val_0 = self.A0.read()
        val_1 = self.A1.read()
        val_2 = self.A2.read()


    # get
    # @override
    # This function overrides LineInterpreter
    #
    # @return - [-1, 1] output of where line is, or None if the line is not detected.
    def get(self):
        return None
