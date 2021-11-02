import cv2
import numpy as np

def resize(image, w, h):
    image = cv2.resize(image, (w, h))
    return image
def gausblur(image, blur):
    image = cv2.GaussianBlur(image, (5,5), blur)
    return image
def medblur(image, shift):
    image = cv2.medianBlur(image, shift)
    return image
def avgblur(image, shift):
    image = cv2.blur(image, (shift,shift))
    return image

gambar = cv2.imread("../image/lenasalt.png")
x = resize(gambar, 300, 300)
cv2.imshow("lenaRGB", gambar)
cv2.imshow("Resize", x)

cv2.waitKey(0)
cv2.destroyAllWindows()