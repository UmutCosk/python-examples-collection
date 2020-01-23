import cv2
import numpy as np
import matplotlib as mat
from matplotlib import pyplot as plt


img = cv2.imread("grid.jpg")
height, width, _ = img.shape

cv2.circle(img, (84, 89), 5, (0, 0, 255), -1)
cv2.circle(img, (446, 89), 5, (0, 0, 255), -1)
cv2.circle(img, (88, 471), 5, (0, 0, 255), -1)

pts1 = np.float32([[84, 89], [446, 89], [88, 471]])

pts2 = np.float32([[0, 89], [446, 89], [150, 471]])


matrix = cv2.getAffineTransform(pts1, pts2)
result = cv2.warpAffine(img, matrix, (width, height))

cv2.imshow("Grid", img)
cv2.imshow("Affine Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
