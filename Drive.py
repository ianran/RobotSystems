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




class Drive(Object):
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
            cls.steer_servo = car.Servo('P2')

        # return instance
        return cls._instance

    # set motor speed
    @staticmethod
    def set_motor_speed(pwm, speed):
        if speed < 0
            pwm.high()
            pwm.pulse_width_percent(speed)
        else:
            pwm.low()
            pwm.pulse_width_percent(speed)

    def stop():
        Drive.set_motor_speed(self.left_motor, 0)
        Drive.set_motor_speed(self.right_motor, 0)

    # forward setting
    # @param speed - input between -100,100, with 0 being stopped
    # @param angle - the input steering angle (-30, 30) (degrees)
    # @param differential - set to false if differential on
    #                       powered motors is not desired.
    def foward(self, speed, angle, differential=True):
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

            if theta > 0:
                lr_ratio = r / (r + self.width)
                L = speed
                R = speed * lr_ratio
            elif theta < 0:
                rl_ratio = r / (r + self.width)
                R = speed
                L = speed * rl_ratio
        else:
            # no differential
            L = speed
            R = speed

        # set speeds.
        self.steer_servo.angle(angle)
        Drive.set_motor_speed(self.left_motor, L)
        Drive.set_motor_speed(self.right_motor, R)
