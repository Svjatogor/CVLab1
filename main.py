# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import threading
import cv2 as cv
from os.path import expanduser


class MainApp(QtGui.QWidget):
    def __init__(self):
        super(MainApp, self).__init__()
        self.open_btn = QtGui.QPushButton('Open')

        # threads param
        self.last_thread_id = 0
        self.thread_lock = threading.Lock()

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
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open image', expanduser("~"), "Image files (*.jpg *.png)")
        if not filename.isEmpty():
            str_filename = filename.toUtf8().data()
            # create thread
            self.last_thread_id += 1
            t = ImageTransformThread(self.last_thread_id, str(self.last_thread_id), str_filename, self.thread_lock)
            t.start()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qw = MainApp()
    sys.exit(app.exec_())