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
import Perception as percep
import Camera
import cv2


# main entry point
if __name__ == '__main__':
    # create motion object
    m = mot.Motion()
    colors = ['red', 'green', 'blue']
    p = percep.Perception(colors)
    box_thresh = [13000, 9000, 11000]

    my_camera = Camera.Camera()
    my_camera.camera_open()

    for i, color in enumerate(colors):
        m.initMove()
        time.sleep(5)
        ################## TODO wait until see block
        while True:
            img = my_camera.frame
            if img is not None:
                frame = img.copy()
                # get box area
                box_area = p.get_box_area(img)
                if box_area is not None:
                    if box_area > box_thresh[i]:
                        print("Cube Detected, Grabbing")
                        break

                cv2.imshow('Frame', frame)
                key = cv2.waitKey(1)
                if key == 27:
                    break


        m.graspHeldCube()

        time.sleep(5)

        m.moveToStorage(color)
        m.openPaws()
        time.sleep(1)
        m.moveAwayStorage(color)
        time.sleep(2.5)

    m.initMove()
    time.sleep(2.5)
