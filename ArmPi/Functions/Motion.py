# Motion.py
# Written Ian Rankin - June 2021
#
# My rewrite of the previous software that hopefully sucks less.
# Basically gets rid of the logic and just has simple arm movement commands.

import sys
sys.path.append('/home/pi/ArmPi/')

import time

from ArmIK.Transform import *
from ArmIK.ArmMoveIK import *

import HiwonderSDK.Board as Board


#Set the RGB light color of the expansion board to make it consistent with the color to be tracked
def set_rgb(color):
    if color == "red":
        Board.RGB.setPixelColor(0, Board.PixelColor(255, 0, 0))
        Board.RGB.setPixelColor(1, Board.PixelColor(255, 0, 0))
        Board.RGB.show()
    elif color == "green":
        Board.RGB.setPixelColor(0, Board.PixelColor(0, 255, 0))
        Board.RGB.setPixelColor(1, Board.PixelColor(0, 255, 0))
        Board.RGB.show()
    elif color == "blue":
        Board.RGB.setPixelColor(0, Board.PixelColor(0, 0, 255))
        Board.RGB.setPixelColor(1, Board.PixelColor(0, 0, 255))
        Board.RGB.show()
    else:
        Board.RGB.setPixelColor(0, Board.PixelColor(0, 0, 0))
        Board.RGB.setPixelColor(1, Board.PixelColor(0, 0, 0))
        Board.RGB.show()


def setBuzzer(timer):
    Board.setBuzzer(0)
    Board.setBuzzer(1)
    time.sleep(timer)
    Board.setBuzzer(0)


class Motion():

    # constructor
    def __init__(self):
        self.AK = ArmIK()

        self.servo1 = 500

        self.coordinate = {
            'red':   (-15 + 0.5, 12 - 0.5, 1.5),
            'green': (-15 + 0.5, 6 - 0.5,  1.5),
            'blue':  (-15 + 0.5, 0 - 0.5,  1.5),
        }
        self.pre_grasp_loc = (0, 15, 15)
        self.grasp_loc = (0, 20, 15)


    def neutral(self):
        self.AK.setPitchRangeMoving((0, 10, 10), -30, -30, -90, 1500)

    def initMove(self):
        Board.setBusServoPulse(1, self.servo1 - 50, 300)
        Board.setBusServoPulse(2, 500, 500)
        self.neutral()

    def closePaws(self):
        Board.setBusServoPulse(1, self.servo1, 300)

    def openPaws(self):
        Board.setBusServoPulse(1, self.servo1 - 280, 500)  # Paws open

    def setWrist(self, angle):
        Board.setBusServoPulse(2, angle, 500)
    def setWristFlat(self):
        self.setWrist(500)
    def setWrist90(self):
        self.setWrist(120)


    # a test move function (x,y,z) coordinates seem to be in centimeters
    def testMove(self):
        time.sleep(8)
        self.AK.setPitchRangeMoving((0,20,10), -30, -30, -90, 1500)
        time.sleep(2.5)
        self.AK.setPitchRangeMoving((0,20,10), 0,-30,-90,1500)
        time.sleep(2.5)
        self.AK.setPitchRangeMoving((0,20,10), 0,0,0,1500)
        time.sleep(2.5)
        self.AK.setPitchRangeMoving((0,0,0), -30,-30,-90,1500)
        time.sleep(2.5)

    #def moveToGrasp(self):


    ########################## FUNCTIONS FOR ROBOT 2
    def graspHeldCube(self):
        # Move to init location
        self.initMove()
        self.setWrist90()
        self.openPaws()
        time.sleep(2.5)

        # Move to pre-grasp location
        didIt = self.AK.setPitchRangeMoving(self.pre_grasp_loc, 0, -20, 20, 1500)
        #print('I can grasp this cube location: ' + str(didIt))
        time.sleep(2.5)

        didIt = self.AK.setPitchRangeMoving(self.grasp_loc, 0, -20, 20, 1500)
        #print('I can grasp this cube location: ' + str(didIt))
        time.sleep(2.5)

        self.closePaws()


    ######################## FUNCTIONS FOR ROBOT 1

    def passCube_rob2(self):
        self.initMove()
        self.closePaws()
        time.sleep(2.5)

        didIt = self.AK.setPitchRangeMoving(self.pre_grasp_loc, 0, -20, 20, 1500)
        time.sleep(2.5)

    def releaseCube_rob2(self):
        self.openPaws()
        time.sleep(3)

        # move to pre-grasp location
        self.AK.setPitchRangeMoving(self.pre_grasp_loc, 0, -20, 20, 1500)
        time.sleep(2.5)


    ###################### GENERIC FUNCTIONS
    def moveToStorage(self, color='red'):
        self.neutral()
        time.sleep(2.5)
        wrist_angle = getAngle(self.coordinate[color][0], \
                                self.coordinate[color][1], -90)
        self.setWrist(wrist_angle)

        self.AK.setPitchRangeMoving(self.coordinate[color], -90, -90, 0)
        time.sleep(2.5)



# Simple test to make sure my code is working
if __name__ == "__main__":

    m = Motion()

    print('Start init move')
    m.initMove()

    print('Finish init move')
    time.sleep(1.5)
    print('Starting test')
    m.testMove()

    print('Start moving wrist')
    #m.setWrist(500)
    m.setWrist90()
    time.sleep(2.5)
    m.setWristFlat()
    time.sleep(2.5)

    m.closePaws()
    time.sleep(2.5)
    m.openPaws()
    time.sleep(2.5)

    m.graspHeldCube()

    print('Done')
