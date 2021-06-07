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


import Motion as mot
import time



# main entry point
if __name__ == '__main__':
    # create motion object
    m = mot.Motion()

    colors = ['red', 'green', 'blue']

    for color in colors:
        m.initMove()
        m.openPaws()
        time.sleep(2.5)

        m.moveToStorage(color)
        m.closePaws()
        time.sleep(2.5)
        m.moveAwayStorage(color)

        m.neutral()
        time.sleep(2.5)

        m.passCube_rob2()

        ############## TODO wait for other robot to block
        time.sleep(1000)

        m.releaseCube_rob2()

    m.initMove()
    time.sleep(2.5)
