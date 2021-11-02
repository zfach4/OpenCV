import cv2

image = cv2.imread("../image/zulfi.jpg", 0)
print("size image original:", image.shape) #untuk melihat size image

ratio = 120 #skala yang ingin kalian masukkan
width = round(image.shape[1] * ratio/100)
height = round(image.shape[0])
dimention = (width, height)

resize = cv2.resize(image, dimention, interpolation=cv2.INTER_AREA)
print("size image resize:", resize.shape)

cv2.imshow("Frame Image Original", image)
cv2.imshow("Frame Image Resize", resize)

cv2.waitKey(0)
cv2.destroyAllWindows()