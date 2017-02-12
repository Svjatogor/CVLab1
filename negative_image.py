import cv2 as cv
import sys
import copy


class NegativeImage:
    def __init__(self, image_path):
        self.image_path = image_path
        self.left_press = False
        self.start_point = ()
        self.window_name = self.image_path.split('/')[-1].split('.')[0]
        self.img = cv.imread(self.image_path)
        self.origin = copy.copy(self.img)
        self.neg_image = copy.copy(self.img)

    def my_mouse_callback(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.left_press = True
            self.start_point = (x, y)
        elif event == cv.EVENT_LBUTTONUP:
            self.left_press = False
        elif event == cv.EVENT_MOUSEMOVE:
            if self.left_press:
                self.img = copy.copy(self.origin)
                cv.rectangle(self.img, self.start_point, (x, y), (255, 153, 0))

    def get_negative_roi(self):
        cv.namedWindow(self.window_name, cv.WINDOW_AUTOSIZE)
        # set callback to click mouse
        cv.setMouseCallback(self.window_name, self.my_mouse_callback)
        while True:
            cv.imshow(self.window_name, self.img)
            key = cv.waitKey(33)
            if key == 27:
                break

        cv.destroyWindow(self.window_name)
        print 'Process ' + self.window_name + ' exiting'


if __name__ == '__main__':
    image_path = sys.stdin.readline().rstrip()
    i = NegativeImage(image_path)
    i.get_negative_roi()
