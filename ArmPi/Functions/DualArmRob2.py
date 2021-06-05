# DualArmRob2.py
# Written mainly Ian Rankin - June 2021
#
# The main entry point for robot 2, which grabs the block handed from robot 1.
# This code needs to detect when robot 1 is handing the block to robot 2, and
# grasp the block.
#
#
# Waits until is sees a block in workspace
# Grabs block held by robot 1
# Waits a few seconds for R1 to release
# Place block into storage area






class MotionControl():
    # constructor
    def __init__(self, is_stack=False):
        self.AK = ArmIK()


        self.coordinate = {
            'red':   (-15 + 0.5, 12 - 0.5, 1.5),
            'green': (-15 + 0.5, 6 - 0.5,  1.5),
            'blue':  (-15 + 0.5, 0 - 0.5,  1.5),
        }

        self.is_stake = is_stack
        self.dz = 2.5

        self.z_r = self.coordinate['red'][2]
        self.z_g = self.coordinate['green'][2]
        self.z_b = self.coordinate['blue'][2]
        self.z = self.z_r

        # Gripper closed angle
        self.servo1 = 500
        self.rotation_angle = 0


    def set_loc(self, x, y):
        self.world_x = x
        self.world_y = y

    def initMove(self):
        Board.setBusServoPulse(1, self.servo1 - 50, 300)
        Board.setBusServoPulse(2, 500, 500)
        self.AK.setPitchRangeMoving((0, 10, 10), -30, -30, -90, 1500)

    def check_reachability(self):
        self.action_finish = False
        set_rgb(detect_color)
        setBuzzer(0.1)

        if self.is_stack:
            # Highly cumulative
            self.z = self.z_r
            self.z_r += self.dz
            if self.z == 2 * self.dz + self.coordinate['red'][2]:
                self.z_r = self.coordinate['red'][2]
            if self.z == self.coordinate['red'][2]:
                self.move_square = True
                time.sleep(3)
                self.move_square = False



        result = self.AK.setPitchRangeMoving((self.world_x, self.world_y - 2, 5), -90, -90, 0) # Do not fill in running time parameters, adaptive running time
        if result == False:
            self.unreachable = True
        else:
            self.unreachable = False
        time.sleep(result[2]/1000) # The third item of the return parameter is time
        self.start_pick_up = False
        self.first_move = False
        self.action_finish = True

        return self.unreachable

    def move_to_grasp(self):
        ########## Move arm to grasp location
        set_rgb(detect_color)
        if track: # If it is the tracking stage
            if not self.__isRunning: # Stop and exit flag detection
                continue
            self.AK.setPitchRangeMoving((self.world_x, self.world_y - 2, 5), -90, -90, 0, 20)
            time.sleep(0.02)
            track = False
        if self.start_pick_up: #If the object hasn’t moved for a while, start to grip
            action_finish = False
            if not self.__isRunning: # Stop and exit flag detection
                continue
            Board.setBusServoPulse(1, self.servo1 - 280, 500)  # Paws open
            # Calculate the angle that the gripper needs to rotate
            self.servo2_angle = getAngle(self.world_x, self.world_y, self.rotation_angle)
            Board.setBusServoPulse(2, self.servo2_angle, 500)
            time.sleep(0.8)


    def grasp_object(self):
        ############### Grasp object
        if not self.__isRunning:
            continue
        self.AK.setPitchRangeMoving((self.world_X, self.world_Y, 2), -90, -90, 0, 1000)  # lower the altitude
        time.sleep(2)

        if not self.__isRunning:
            continue
        Board.setBusServoPulse(1, self.servo1, 500)  # close paws
        time.sleep(1)

        if not self.__isRunning:
            continue
        Board.setBusServoPulse(2, 500, 500)
        self.AK.setPitchRangeMoving((self.world_X, self.world_Y, 12), -90, -90, 0, 1000)  # Robotic arm up
        time.sleep(1)

    def move_to_color(self):
        if not self.__isRunning:
            continue
        # Sort and place different colored squares
        result = self.AK.setPitchRangeMoving((
                            self.coordinate[self.detect_color][0], \
                            self.coordinate[self.detect_color][1], 12) \
                            , -90, -90, 0)
        time.sleep(result[2]/1000)

        if not self.__isRunning:
            continue
        self.servo2_angle = getAngle(self.coordinate[self.detect_color][0], \
                                self.coordinate[self.detect_color][1], -90)
        Board.setBusServoPulse(2, self.servo2_angle, 500)
        time.sleep(0.5)

        if not self.__isRunning:
            continue

        if not is_stack:
            self.z = self.coordinate[self.detect_color][2]

        self.AK.setPitchRangeMoving((
                        self.coordinate[self.detect_color][0], \
                        self.coordinate[self.detect_color][1], \
                        self.z + 3), \
                        -90, -90, 0, 500)
        time.sleep(0.5)

    def release_object(self):
        if not self.__isRunning:
            continue
        self.AK.setPitchRangeMoving((self.coordinate[self.detect_color][0],\
                                    self.coordinate[self.detect_color][1],\
                                    self.z), \
                                    -90, -90, 0, 1000)
        time.sleep(0.8)

        if not self.__isRunning:
            continue
        Board.setBusServoPulse(1, self.servo1 - 200, 500)  # Open the paws and put down the object
        time.sleep(0.8)

        if not __isRunning:
            continue
        AK.setPitchRangeMoving((\
                self.coordinate[self.detect_color][0], \
                self.coordinate[self.detect_color][1], 12), \
                -90, -90, 0, 800)
        time.sleep(0.8)

    def reset_to_initial(self):
        self.initMove()
        time.sleep(1.5)

        self.detect_color = 'None'
        self.first_move = True
        self.get_roi = False
        self.action_finish = True
        self.start_pick_up = False
        set_rgb(detect_color)


    # Waits until is sees a block in workspace
    # Grabs block held by robot 1
    # Waits a few seconds for R1 to release
    # Place block into storage area
    def run(self):
        # Run in thread continously.

        while True:
            if self.__isRunning:
                if self.first_move and self.start_pick_up:
                    reachable = self.check_reachability()

                elif not self.first_move and not self.unreachable: # Not the first time an object has been detected
                    self.move_to_grasp()
                    self.grasp_object()
                    self.move_to_color()
                    self.release_object()
                else:
                    time.sleep(0.01)
            else:
                if self._stop:
                    self._stop = False
                    Board.setBusServoPulse(1, servo1 - 70, 300)
                    time.sleep(0.5)
                    Board.setBusServoPulse(2, 500, 500)
                    self.AK.setPitchRangeMoving((0, 10, 10), -30, -30, -90, 1500)
                    time.sleep(1.5)
                time.sleep(0.01)





# main entry point
if __name__ == '__main__':
    pass
    # do stuff
