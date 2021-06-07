#!/usr/bin/python3
# coding=utf8

import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
import threading
from LABConfig import *
import ArmIK.Transform as ArmTransform
import ArmIK.ArmMoveIK as ArmMoveIK
import HiwonderSDK.Board as Board
from CameraCalibration.CalibrationConfig import *
import Perception as percep

"""
1. Robot 1 picks up block from block storage
2. Robot 1 holds block to Robot 2 in workspace
3. Robot 1 waits until block is partially obscured by Robot 2
4. Robot 1 releases block and returns to home position

Grabbed code from Ian
"""

if __name__== '__main__':
    target_color = ('red', 'green', 'blue')
    my_camera = Camera.Camera()
    my_camera.camera_open()

    # create perception object
    p = percep.Perception(target_color)

    while True:
        img = my_camera.frame
        if img is not None:
            frame = img.copy()
            # get box area
            p.get_box_area(img)

            cv2.imshow('Frame', frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
    my_camera.camera_close()
    cv2.destroyAllWindows()



# def move_to_grasp(world_x, world_y):
#     """
#     Move arm to grasp location
#     """
#     # Gripper closed angle
#     servo1 = 500
#     rotation_angle = 0
#     altitude = 5

#     # tuple of xyz, then alpha, alpha1, alpha 2, and finally move time
#     # Given coordinate_data and pitch angle alpha, and the range of pitch angle range alpha1, alpha2, automatically find the solution closest to the given pitch angle and turn to the target position
#     # If there is no solution, return False, otherwise return the servo angle, pitch angle, and running time
#     # Coordinate unit cm, passed in as a tuple, for example (0, 5, 10)
#     # alpha is the given pitch angle
#     # alpha1 and alpha2 are the range of pitch angle
#     # movetime is the rotation time of the steering gear, in ms, if no time is given, it will be calculated automatically
#     ArmMoveIK.ArmIK().setPitchRangeMoving((world_x, world_y, altitude), -90, -90, 0, 20)
#     time.sleep(0.02)

#     Board.setBusServoPulse(1, servo1 - 280, 500)  # Paws open
#     # Calculate the angle that the gripper needs to rotate, from Transform.py
#     servo2_angle = ArmTransform.getAngle(world_x, world_y, rotation_angle)
#     Board.setBusServoPulse(2, servo2_angle, 500)
#     time.sleep(0.8)

# def grasp_object(world_X, world_Y):
#     """
#     Grasp object, lower then raise back up
#     """
#     # Gripper closed angle
#     servo1 = 500
#     low_altitude = 2
#     high_altitude = 12

#     ArmMoveIK.ArmIK().setPitchRangeMoving((world_X, world_Y, low_altitude), -90, -90, 0, 1000)  # lower the altitude
#     time.sleep(2)

#     Board.setBusServoPulse(1, servo1, 500)  # close paws
#     time.sleep(1)

#     Board.setBusServoPulse(2, 500, 500)
#     ArmMoveIK.ArmIK().setPitchRangeMoving((world_X, world_Y, high_altitude), -90, -90, 0, 1000)  # Robotic arm up
#     time.sleep(1)

# def release_object():
#     """
#     Just opens the gripper
#     """
#     servo1 = 500
#     Board.setBusServoPulse(1, servo1 - 200, 500)  # Open the paws and put down the object
#     time.sleep(0.8)

# def move_to_handoff(world_X, world_Y):
#     # TODO check the alpha pitch angle and the altitude
#     altitude = 15
#     ArmMoveIK.ArmIK().setPitchRangeMoving((world_X, world_Y, altitude), -45, -90, 0, 1000)  


