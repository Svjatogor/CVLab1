# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from os.path import expanduser
import os
import subprocess
import sys


class MainApp(QtGui.QWidget):
    def __init__(self):
        super(MainApp, self).__init__()
        self.open_btn = QtGui.QPushButton('Open')

        # subprocess param
        self.pipes = []
        self.negative_image_process = os.path.join(os.path.dirname(__file__), "./negative_image.py")

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
            # create subprocess
            command = [sys.executable, self.negative_image_process]
            pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
            self.pipes.append(pipe)
            pipe.stdin.write(str_filename)
            pipe.stdin.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qw = MainApp()
    sys.exit(app.exec_())