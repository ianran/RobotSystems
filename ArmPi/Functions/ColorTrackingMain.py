#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
import threading
from LABConfig import *
from ArmIK.Transform import *
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Board as Board
from CameraCalibration.CalibrationConfig import *

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

# bring in Motion control class
motion = MotionControl(is_stack=False)

__target_color = ('red',)




count = 0
track = False
_stop = False
get_roi = False
center_list = []
first_move = True
__isRunning = False
detect_color = 'None'
action_finish = True
start_pick_up = False
start_count_t1 = True
# Reset variables
def reset():
    global count
    global track
    global _stop
    global get_roi
    global first_move
    global center_list
    global __isRunning
    global detect_color
    global action_finish
    global start_pick_up
    global __target_color
    global start_count_t1

    count = 0
    _stop = False
    track = False
    get_roi = False
    center_list = []
    first_move = True
    __target_color = ()
    detect_color = 'None'
    action_finish = True
    start_pick_up = False
    start_count_t1 = True

# app initialization call
def init():
    print("ColorTracking Init")
    initMove()

# App start playing method call
def start():
    global __isRunning
    global move
    reset()
    move.__isRunning = True
    print("ColorTracking Start")

# app stop gameplay call
def stop():
    global move
    move._stop = True
    move.__isRunning = False
    print("ColorTracking Stop")

# App exit gameplay call
def exit():
    global move
    move._stop = True
    move.__isRunning = False
    print("ColorTracking Exit")


######################################## Start main manipulation code
# Robotic arm move thread
def move():
    motion.run()


######################################## End main manipulation code

# Run child thread
th = threading.Thread(target=move)
th.setDaemon(True)
th.start()



if __name__ == '__main__':
    target_color = ('red', 'green', 'blue')
    my_camera = Camera.Camera()
    my_camera.camera_open()

    perception = ColorPerception(target_color)

    while True:
        img = my_camera.frame
        if img is not None:
            frame = img.copy()
            Frame = perception.perception(frame, start_pick_up=False)
            x,y = perception.get_loc()
            move.set_loc(x,y)
            cv2.imshow('Frame', Frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
    my_camera.camera_close()
    cv2.destroyAllWindows()
