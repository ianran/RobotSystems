# Drive.py
# Written Ian Rankin - April 2021
#
# A class for to handle the picar drive.
# Setup as a Singleton class so it can be init multiple times with the same class
#
# Example:
#
# drive = Drive()
# drive2 = Drive()
#
# drive and drive2 are the same object


import picarx_improved as car
import math
import time


class Drive(object):
    _instance = None
    # constructor as singleton class
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Drive, cls).__new__(cls)

            # init code here
            cls.length = 9.5 # cm
            cls.width = 11.7 # cm

            cls.max_steer = 30 # degrees

            cls.left_motor = car.PWM('P13')
            cls.right_motor = car.PWM('P12')
            cls.left_dir = car.Pin("D4")
            cls.right_dir = car.Pin("D5")
            cls.steer_calib = -17
            cls.steer_servo = car.Servo(car.PWM('P2'))

        # return instance
        return cls._instance

    # set motor speed
    # @param L - the left motor speed (-100, 0, 100)
    # @param R - the right motor speed (-100, 0, 100)
    def set_speed(self, L, R):
        if L > 0:
            self.left_dir.high()
            self.left_motor.pulse_width_percent(L)
        else:
            self.left_dir.low()
            self.left_motor.pulse_width_percent(L)

        if R < 0:
            self.right_dir.high()
            self.right_motor.pulse_width_percent(R)
        else:
            self.right_dir.low()
            self.right_motor.pulse_width_percent(R)


    def stop(self):
        self.set_speed(0,0)

    def set_steer(self, angle):
        self.steer_servo.angle(angle + self.steer_calib)

    # forward setting
    # @param speed - input between -100,100, with 0 being stopped
    # @param angle - the input steering angle (-30, 30) (degrees)
    # @param differential - set to false if differential on
    #                       powered motors is not desired.
    def forward(self, speed, angle, differential=True):
        if speed > 100:
            speed = 100
        elif speed < -100:
            speed = -100

        if angle > self.max_steer:
            angle = 30
        elif angle < -self.max_steer:
            angle = -30

        theta = angle * math.pi / 180.0
        if differential:
            # radius of to the center of the circle
            r = self.length / math.cos(abs(theta))

            if theta < 0:
                lr_ratio = r / (r + self.width)
                L = speed
                R = speed * lr_ratio
            elif theta > 0:
                rl_ratio = r / (r + self.width)
                R = speed
                L = speed * rl_ratio
            else:
                L = R = speed
        else:
            # no differential
            L = speed
            R = speed

        # set speeds.
        self.set_steer(angle)
        self.set_speed(L, R)


    # @param speed - speed
    # @param angle - angle to turn + value is right, - value is left.
    # @param time - the time to run the maneuver
    def maneuver(self, speed, angle, time_run):
        #print('speed: ' + str(speed), + ' angle: ' + str(angle) + ' time: ' + str(time_run))
        print('angle')
        print(angle)
        self.forward(speed, angle)
        time.sleep(time_run)

    def parallel_park(self, left):
        park_time = 0.7

        turn_angle = 20
        if left:
            turn_angle = -turn_angle

        self.maneuver(-0.3, turn_angle, park_time)
        self.maneuver(-0.3, -turn_angle, park_time)
        self.maneuver(0.3, 0, park_time/2)

    def k_turn(self, left):
        turn_angle = 20
        turn_time = 0.6

        if left:
            turn_angle = -turn_angle

        self.maneuver(0.3, turn_angle, turn_time)
        self.maneuver(-0.3, -turn_angle, turn_time)
        self.maneuver(0.3, 0, 0.05)
