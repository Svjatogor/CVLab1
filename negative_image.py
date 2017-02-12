import cv2 as cv
import sys


class NegativeImage():
    def __init__(self, image_path):
        self.image_path = image_path
        self.left_press = False
        self.get_negative_roi()
        self.start_point = ()

    def my_mouse_callback(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.left_press = True
            self.start_point = (x, y)
            cv.circle(param, (x, y), 1, (0, 0, 255), 2)
        elif event == cv.EVENT_LBUTTONUP:
            self.left_press = False
            cv.circle(param, (x, y), 1, (0, 0, 255), 2)
        elif event == cv.EVENT_MOUSEMOVE:
            if self.left_press:
                cv.rectangle(param, self.start_point, (x, y), ())

    def get_negative_roi(self):

        window_name = self.image_path.split('/')[-1].split('.')[0]

        print 'Starting process ' + window_name

        cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
        img = cv.imread(self.image_path)
        # set callback to click mouse
        cv.setMouseCallback(window_name, self.my_mouse_callback, img)
        while True:
            cv.imshow(window_name, img)
            key = cv.waitKey(33)
            if key == 27:
                break

        cv.destroyWindow(window_name)
        print 'Process ' + window_name + ' exiting'


if __name__ == '__main__':
    image_path = sys.stdin.readline().rstrip()
    i = NegativeImage(image_path)
