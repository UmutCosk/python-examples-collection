import numpy as np
import cv2
from matplotlib import pyplot as plt


cam = cv2.VideoCapture(0)
template = cv2.imread("zettel.jpg", 0)
x = 100
template = cv2.resize(template, (x, x))

while(True):

    _, frame = cam.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.5)

    for points in zip(*loc[::-1]):
        cv2.rectangle(
            frame, points, (points[0]+x, points[1]+x), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

# img_original = cv2.imread('strasse.jpg')
# img = cv2.imread('strasse.jpg', 0)
# heigth_s, width_s = img.shape
# template = cv2.imread('schild.jpg', 0)
# #template = cv2.resize(template, (85, 85))
# heigth_t, width_t = template.shape
# print(heigth_t)
# print(width_t)
# result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
# loc = np.where(result >= 0.8)

# for point in zip(*loc[::-1]):
#     # cv2.rectangle(img, point, (point[0]+width_t,
#     #                            point[1]+heigth_t), (0, 255, 0), 3)
#     cv2.rectangle(img_original, point, (point[0]+width_t,
#                                         point[1]+heigth_t), (0, 255, 0), 3)


# cv2.imshow("Straße", img_original)
# cv2.imshow("Result", result)

# plt.imshow(img_original)
# plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
