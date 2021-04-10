#!/usr/bin/env python3
#

import sys
sys.path.append('..')
from Drive import Drive

if __name__ == '__main__':
    drive = Drive()

    drive.forward(50, 0)

    time.sleep(5)
    drive.stop()
