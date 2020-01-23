import cv2
import numpy as np
import matplotlib as mat
from matplotlib import pyplot as plt


img = cv2.imread('girl.jpg')
# cv2.rectangle(img, (0, 50), (100, 100), (255), -1)
# cv2.circle(img, (50, 50), 25, 127, -1)

b, g, r = cv2.split(img)

titles = ["blue", "green", "red"]
images = [b, g, r]

cv2.imshow("Image", img)

for i in range(len(titles)):
    plt.subplot(2, 2, i+1)
    plt.hist(images[i].ravel(), 256, [0, 256])
    plt.title(titles[i])
    cv2.imshow(titles[i], images[i])


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
