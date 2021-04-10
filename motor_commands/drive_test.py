#!/usr/bin/env python3
#

import sys
import time
sys.path.append('..')

from Drive import Drive

if __name__ == '__main__':
    drive = Drive()

    drive.set_speed(0,50)
    time.sleep(1)
    drive.set_speed(50,0)
    time.sleep(1)

    drive.forward(20, -4)

    time.sleep(5)
    drive.stop()
