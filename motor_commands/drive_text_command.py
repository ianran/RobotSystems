#!/usr/bin/env python3
#

import sys
import time
sys.path.append('..')

from Drive import Drive

if __name__ == '__main__':
    drive = Drive()

    continue_loop = True
    while continue_loop:
        print('maneuvers w - straight, a - left curve, d - right curve, s - backwards')
        print('q - left parallel_park, e - right parallel_park, z - left k-turn, c - right k-turn')
        print('Any other command quits the program.')
        man = input('Enter maneuver: ')

        time_to_run = 1.0

        if man == 'w':
            drive.maneuver(50, 0, time_to_run)
        elif man == 'a':
            drive.maneuver(50, -10, time_to_run)
        elif man == 'd':
            drive.maneuver(50, 10, time_to_run)
        elif man == 's':
            drive.maneuver(-50, 0, time_to_run)
        elif man == 'q':
            drive.parallel_park(True)
        elif man == 'e':
            drive.parallel_park(False)
        elif man == 'z':
            drive.k_turn(True)
        elif man == 'c':
            drive.k_turn(False)
        else:
            continue_loop = False

    print('Quiting')
