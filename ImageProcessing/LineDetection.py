import numpy as np
import cv2
from matplotlib import pyplot as plt

video = cv2.VideoCapture("road_car_view.mp4")

while True:
    ret, frame = video.read()
    if not ret:
        video = cv2.VideoCapture("road_car_view.mp4")
        continue

    frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([18, 94, 140])
    up_yellow = np.array([48, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, up_yellow)
    edges = cv2.Canny(mask, 50, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50,
                            maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", edges)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
# img = cv2.imread("lines.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 75, 100)

# lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30,
#                         maxLineGap=200, minLineLength=30)

# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

# # cv2.HoughLinesP()


# cv2.imshow("Lines", img)
# cv2.imshow("Edges", edges)


# cv2.waitKey(0)
# cv2.destroyAllWindows()
