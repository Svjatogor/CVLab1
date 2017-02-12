import os
import subprocess
import sys
from PyQt4 import QtGui, QtCore
import threading
import cv2 as cv
from os.path import expanduser


    def run(self):
        print 'Starting ' + self.name
        window_name = self.image_path.split('/')[-1].split('.')[0]
        cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
        img = cv.imread(self.image_path)
        # set callback to click mouse
        cv.setMouseCallback(window_name, self.my_mouse_callback, img)
        while True:
            cv.imshow(window_name, img)
            key = cv.waitKey(0)
            if key == 27:
                break
        cv.destroyWindow(window_name)
        print self.name + ' Exiting'

    def my_mouse_callback(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            cv.circle(param, (x, y), 100, (0, 0, 255))
        elif event == cv.EVENT_LBUTTONUP:
            cv.circle(param, (x, y), 100, (255, 0, 0))