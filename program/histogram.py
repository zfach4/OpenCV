import cv2
from matplotlib import pyplot as plt

image = cv2.imread("../image/baboon.jpg", 0)
ret,th = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)

# plt.hist(image.ravel(), 256, [0, 256])
# plt.show()

cv2.imshow("FrameBaboon", image)
cv2.imshow("Frame Lena Biner", th)
cv2.waitKey(0)
cv2.destroyAllWindows()