import cv2 as cv
import numpy as np


def nothing(x):
    pass


cap = cv.VideoCapture(0)
cv.namedWindow("Tracking")
cv.createTrackbar("Lower Hue", "Tracking", 0, 255, nothing)
cv.createTrackbar("Lower Saturation", "Tracking", 0, 255, nothing)
cv.createTrackbar("Lower Value", "Tracking", 0, 255, nothing)
cv.createTrackbar("Higher Hue", "Tracking", 255, 255, nothing)
cv.createTrackbar("Higher Saturation", "Tracking", 255, 255, nothing)
cv.createTrackbar("Higher Value", "Tracking", 255, 255, nothing)


while(True):
    #frame = cv.imread('smarties.jpg')
    _, frame = cap.read()
    frame = cv.resize(frame, (680, 680))

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_hue = cv.getTrackbarPos("Lower Hue", "Tracking")
    lower_saturation = cv.getTrackbarPos("Lower Saturation", "Tracking")
    lower_value = cv.getTrackbarPos("Lower Value", "Tracking")

    higher_hue = cv.getTrackbarPos("Higher Hue", "Tracking")
    higher_value = cv.getTrackbarPos("Higher Value", "Tracking")
    higher_saturation = cv.getTrackbarPos("Higher Saturation", "Tracking")

    lower_blue_range = np.array([lower_hue, lower_saturation, lower_value])
    upper_blue_range = np.array([higher_hue, higher_saturation, higher_value])

    mask = cv.inRange(hsv, lower_blue_range, upper_blue_range)

    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Frame', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', result)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
