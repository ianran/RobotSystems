# LineController.py
# Written Ian Rankin - April 2021
#
# A function given a LineInterpreter class and drive, makes the robot follow a
# line.
# The controller is a PID controller as they are simple and easy to implement
# and ubiqiqitous controller when a different controller isn't obvious

from LineInterpreter import LineInterpreter
import time

class LineController():
    def __init__(self, line_intepreter, drive):
        self.line = line_intepreter
        self.drive = drive

        self.int_accum = 0
        self.last_error = None
        self.last_time = None
        self.setpoint = 0 # just in case this needs to be modified for what ever reason

        self.default_angle = -15

        self.kp = 0
        self.ki = 0
        self.kd = 0



    # Update
    # This method calls the needed functions to get the location of the line
    # and sets the drive to that location. It also returns the output servo
    # angle because it was requested.
    #
    # @return - output servo angle
    def update(self):
        loc = self.line.get()
        cur_time = time.time()


        if loc is None:
            self.int_accum = 0
            self.last_error = None
            output = self.default_angle
        else:
            if self.last_error is None:
                self.last_error = self.setpoint - loc
                self.last_time = cur_time

            err = self.setpoint - loc
            dt = cur_time - self.last_time

            # handle integral term
            int_accum += err * dt
            derv = (err - self.last_error) / dt

            # PID controller
            output = self.kp*err + self.ki*int_accum + self.kd*derv

            self.last_error = err

        # squash output to bounds
        if output > 30:
            output = 30
        elif output < -30:
            output = -30

        self.last_time = cur_time
        self.drive.forward(30, output)
        return output
