import cv2 as cv
from PyQt4 import QtGui, QtCore

# -*- coding: utf-8 -*-

import cv2
import sys
from PyQt4 import QtGui, QtCore


class MainApp(QtGui.QWidget):
    def __init__(self):
        super(MainApp, self).__init__()
        self.open_btn = QtGui.QPushButton('Open')

        self.init_ui()
        self.setup()

    def init_ui(self):
        # widget settings
        self.setMinimumSize(250, 50)
        # main layout
        main_layout = QtGui.QHBoxLayout()
        main_layout.addWidget(self.open_btn)
        # show
        self.setLayout(main_layout)
        self.setWindowTitle(u'Negative image')
        self.show()

    def setup(self):
        self.open_btn.clicked.connect(self.open_image)

    def open_image(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open image', '/home/', "Image files (*.jpg *.png)")
        if not filename.isEmpty():
            str_filename = filename.toUtf8().data()
            img = cv.imread(str_filename)
            window_name = str_filename.split('/')[-1].split('.')[0]
            cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
            # set callback to click mouse
            cv.setMouseCallback(window_name, self.my_mouse_callback, img)
            while True:
                cv.imshow(window_name, img)

                key = cv.waitKey(33);
                if key == 27:
                    break
            cv.destroyWindow(window_name)

    def my_mouse_callback(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            cv.circle(param, (x, y), 100, (0, 0, 255))
        elif event == cv.EVENT_LBUTTONUP:
            cv.circle(param, (x, y), 100, (255, 0, 0))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qw = MainApp()
    sys.exit(app.exec_())