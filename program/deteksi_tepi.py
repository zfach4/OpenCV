import cv2
import numpy as np
from scipy import ndimage

def sobel(img):
    im = img.astype('int32')
    gx = ndimage.sobel(im, 1)
    gy = ndimage.sobel(im, 0)

    magnitude = np.hypot(gx, gy)
    magnitude = magnitude*255 / np.max(magnitude)

    cv2.imwrite("sobel.jpg", magnitude)

def prewitt(img):
    im = img.astype('int32')
    gx = ndimage.prewitt(im, 1)
    gy = ndimage.prewitt(im, 0)

    magnitude = np.hypot(gx, gy)
    magnitude = magnitude * 255 / np.max(magnitude)

    cv2.imwrite("prewitt.jpg", magnitude)

def canny(img, th1, th2):
    can = cv2.Canny(img, th1, th2)
    cv2.imwrite("canny.jpg", can)

image = cv2.imread("../image/lenagrayscale.png")
sobel(image)
prewitt(image)
canny(image, 120, 205)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()