# go_grasp_loc.py
# Written  Ian Rankin - June 2021
#
# Just a helper script to make the robot go home for allignment etc


import Motion as mot
import time



# main entry point
if __name__ == '__main__':
    # create motion object
    m = mot.Motion()
    m.openPaws()
    didIt = m.AK.setPitchRangeMoving(m.grasp_loc, 0, -20, 20, 1500)
    time.sleep(3.5)
