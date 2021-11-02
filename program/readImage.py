import cv2

#image = cv2.imread("path/nameImage.format")
image = cv2.imread("E:\PPI\Module Pembelajaran opencv\image\zulfi.jpg")

# cv2.imshow("namaFrame, nameVariable")
cv2.imshow("Percobaan", image)

# agar tidak langsung close
cv2.waitKey(0)

#untuk keluar dari program
cv2.destroyAllWindows()