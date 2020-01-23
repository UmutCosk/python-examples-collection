import cv2 as cv
import numpy as np


img = cv.imread('sudoku.png')
img = cv.resize(img, (480, 480))
img = gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
thresh2 = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 4)
thresh3 = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 4)


cv.imshow("Sudoku", img)
cv.imshow("Threshold Binary", thresh1)
cv.imshow("Adaptive Threshold Binary MEAN", thresh2)
cv.imshow("Adaptive Threshold Binary GAUSS", thresh3)

cv.waitKey(0)


# while(True):
#     cv.imshow("Gradient", img)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

cv.destroyAllWindows()
