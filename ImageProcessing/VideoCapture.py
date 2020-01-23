import cv2 as cv
import numpy as nu

print("Hello World")

cap = cv.VideoCapture(0)


while(True):
    ret, frame = cap.read()
    h = cap.get(3)
    print(h)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
