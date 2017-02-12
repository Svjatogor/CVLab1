import cv2 as cv
import sys


def my_mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(param, (x, y), 100, (0, 0, 255))
    elif event == cv.EVENT_LBUTTONUP:
        cv.circle(param, (x, y), 100, (255, 0, 0))

image_path = sys.stdin.readline().rstrip()
window_name = image_path.split('/')[-1].split('.')[0]

print 'Starting process ' + window_name

cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
img = cv.imread(image_path)
# set callback to click mouse
cv.setMouseCallback(window_name, my_mouse_callback, img)
while True:
    cv.imshow(window_name, img)
    key = cv.waitKey(33)
    if key == 27:
        break

cv.destroyWindow(window_name)
print 'Process ' + window_name + ' exiting'


