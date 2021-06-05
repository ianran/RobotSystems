# go_home.py
# Written  Ian Rankin - June 2021
#
# Just a helper script to make the robot go home for allignment etc


import Motion as mot
import time



# main entry point
if __name__ == '__main__':
    # create motion object
    m = mot.Motion()
    m.initMove()
    time.sleep(3)
