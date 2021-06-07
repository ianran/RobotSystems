#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
import LABConfig as lbc
import CameraCalibration.CalibrationConfig as cconf
import math
import numpy as np
from ArmIK.Transform import *


class Perception():
    def __init__(self, target_colors, min_box_area=2500, color_range=lbc.color_range, \
                size=(640, 480), square_length=cconf.square_length):
        self.min_box_area = min_box_area
        self.color_range = color_range

        self.size = size
        self.square_length = square_length

        self.target_colors = target_colors

        self.color_list = []
        self.start_count_t1 = True
        self.count = 0

        self.last_x = 0
        self.last_y = 0

        self.range_rgb = {
            'red': (0, 0, 255),
            'blue': (255, 0, 0),
            'green': (0, 255, 0),
            'black': (0, 0, 0),
            'white': (255, 255, 255),
        }

        # smallest contour allowed
        self.contour_cutoff = 300
        self.picked_object = False
        self.held_box_area = 9000
        self.obscure_thresh = 1000

    def preprocess(self, img):
        img_h, img_w = img.shape[:2]
        cv2.line(img, (0, int(img_h / 2)), (img_w, int(img_h / 2)), (0, 0, 200), 1)
        cv2.line(img, (int(img_w / 2), 0), (int(img_w / 2), img_h), (0, 0, 200), 1)

        frame_resize = cv2.resize(img, self.size, interpolation=cv2.INTER_NEAREST)
        frame_gb = cv2.GaussianBlur(frame_resize, (11, 11), 11)

        #If an area is detected with a recognized object, it will continue to detect the area until there is none
        frame_lab = cv2.cvtColor(frame_gb, cv2.COLOR_BGR2LAB)  # Convert image to LAB space
        return frame_lab

    def fill_image(self, image):
        opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, np.ones((6, 6), np.uint8))  # Open operation
        closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, np.ones((6, 6), np.uint8))  # Closed operation
        return closed

    def get_contours(self, image):
        return cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # Find the outline

    def getAreaMaxContour(self, contours):
        contour_area_temp = 0
        contour_area_max = 0
        area_max_contour = None

        for c in contours:  # Traverse all contours
            contour_area_temp = math.fabs(cv2.contourArea(c))  # Calculate the contour area
            if contour_area_temp > contour_area_max:
                contour_area_max = contour_area_temp
                if contour_area_temp > self.contour_cutoff:  # Only accept contours with area larger than 300
                    area_max_contour = c

        return area_max_contour, contour_area_max  # Return the largest contour

    # Perform bit operations on the original image and mask
    def thresh_image(self, image, low_color, high_color):
        return cv2.inRange(image, low_color, high_color)

    def get_larget_contour(self, contours):
        return self.getAreaMaxContour(contours)  # Find the largest contour


    def get_box_area(self, img):
        img_copy = img.copy()
        frame_lab = self.preprocess(img_copy)

        max_area = 0
        areaMaxContour = 0
        color_area_max = None

        for i in self.color_range:
            if i in self.target_colors:
                detect_color = i
                frame_mask = self.thresh_image( frame_lab, \
                                                self.color_range[detect_color][0], \
                                                self.color_range[detect_color][1])
                closed = self.fill_image(frame_mask)
                contours = self.get_contours(closed)
                areaMaxContour, area_max = self.get_larget_contour(contours)

                if areaMaxContour is not None:
                    if area_max > max_area:  # Find the largest area of all of the colors
                        max_area = area_max
                        color_area_max = i
                        areaMaxContour_max = areaMaxContour


        if max_area > self.min_box_area:  # Have found the largest area
            self.held_box_area = max_area
            print('Box Color: ', i)
            print('Max Area: ', max_area)

    def box_is_obscure(self):
        if self.held_box_area < self.obscure_thresh:
            return True
        else:
            return False