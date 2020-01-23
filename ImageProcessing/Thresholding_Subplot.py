import cv2 as cv
import numpy as np
import matplotlib as mat
from matplotlib import pyplot as plt

img = cv.imread('gradient.png')
img = cv.resize(img, (480, 480))
_, thresh1 = cv.threshold(img, 200, 255, cv.THRESH_BINARY)
_, thresh2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, thresh3 = cv.threshold(img, 125, 255, cv.THRESH_TRUNC)
_, thresh4 = cv.threshold(img, 125, 255, cv.THRESH_TOZERO)


titles = ['Original', 'Binary', 'Trunc', 'To Zero']
images = [img, thresh1, thresh3, thresh4]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# cv.imshow("Gradient", img)
# cv.imshow("Threshold Binary", thresh1)
# cv.imshow("Threshold Binary Inverse", thresh2)
# cv.imshow("Threshold Trunc", thresh3)
# cv.imshow("Threshold To Zero", thresh4)


# while(True):
#     cv.imshow("Gradient", img)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cv.waitKey(0)
# cv.destroyAllWindows()
