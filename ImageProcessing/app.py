import numpy as np
import cv2
from matplotlib import pyplot as plt


img_original = cv2.imread("shapes.jpg")
img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_gray2 = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    contour_image = cv2.drawContours(
        img_gray, [approx], 0, 0, 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:

        cv2.putText(img_gray2, "Triangle", (x, y),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
    elif len(approx) == 4:
        cv2.putText(img_gray2, "Rect", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


# # Create a mask of contours and create its inverse mask also
# _, mask = cv2.threshold(contour_image, 10, 255, cv2.THRESH_BINARY)
# mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
# mask_inv = cv2.bitwise_not(mask)
# mask_inv[:, :, 0] = 0
# mask_inv[:, :, 1] = 255
# mask_inv[:, :, 2] = 0
# new_mask = cv2.bitwise_or(mask_inv, mask)

cv2.imshow("Contour", img_gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()
