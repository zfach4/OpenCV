import cv2

image = cv2.imread("../image/baboon.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,biner = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Frame Lena Gray", gray)
cv2.imshow("Frame Lena Biner", biner)
cv2.waitKey(0)
cv2.destroyAllWindows()