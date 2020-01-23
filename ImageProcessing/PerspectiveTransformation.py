import cv2
import numpy as np
import matplotlib as mat
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # EDGES OF PAPER
    cv2.circle(frame, (155, 117), 5, (0, 0, 255), -1)
    cv2.circle(frame, (457, 103), 5, (0, 0, 255), -1)
    cv2.circle(frame, (50, 475), 5, (0, 0, 255), -1)
    cv2.circle(frame, (565, 455), 5, (0, 0, 255), -1)

    # ORDER MATTERS: TopLeft , TopRight, BottomLeft, BottomRight
    pts1 = np.float32([[155, 117], [457, 103], [50, 475], [565, 455]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    result = cv2.warpPerspective(frame, matrix, (500, 600))

    cv2.imshow("Frame", frame)
    cv2.imshow("Perspective Transformation", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
