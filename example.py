import cv2
import numpy

from matplotlib.image import imread

array = cv2.imread("image.png")
print(array.shape)
print(array)

a=numpy.array(
[[[255,   0,   0],
  [255, 255, 255],
  [255, 255, 255],
  [187,  41, 160]],

 [[255, 28, 255],
  [255, 255, 255],
  [255, 255, 55],
  [255, 255, 255]],

 [[255, 25, 55],
  [  0,   0,   0],
  [ 90, 255, 173],
  [25, 25, 255]]])

cv2.imwrite('4image.png', a)

rasm = imread("4image.png")
print(rasm*255)

rasm2 = cv2.imread("4image.png")
print(rasm2)