# Motion.py
# Written Ian Rankin - June 2021
#
# My rewrite of the previous software that hopefully sucks less.
# Basically gets rid of the logic and just has simple arm movement commands.

import Time

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

    def initMove(self):
        Board.setBusServoPulse(1, self.servo1 - 50, 300)
        Board.setBusServoPulse(2, 500, 500)
        self.AK.setPitchRangeMoving((0, 10, 10), -30, -30, -90, 1500)





# Simple test to make sure my code is working
if __name__ == "__main__":

    m = Motion()

    print('Start init move')
    m.initMove()

    print('Finish init move')
    time.sleep(5000)
    print('Done')
