import cv2 as cv
import numpy as np
import matplotlib as mat
from matplotlib import pyplot as plt

img = cv.imread("girl.jpg", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

# Kernel = Structering Element ; https://youtu.be/7-FZBgrW4RE?t=91
kernel = np.ones((3, 3), np.uint8)
dilation = cv.dilate(mask, kernel, iterations=2)
erosion = cv.erode(mask, kernel, iterations=5)
# First: Erosion , After: Dilation
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=10)
close = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=10)
morph_gradient = cv.morphologyEx(
    mask, cv.MORPH_GRADIENT, kernel, iterations=10)
morph_tophead = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel, iterations=10)

titles = ["Image", "Mask", "Dilation", "Erosion",
          "Opening", "Closing", "Gradient", "Tophead"]

images = [img, mask, dilation, erosion, opening,
          close, morph_gradient, morph_tophead]

for i in range(len(titles)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])

plt.show()
