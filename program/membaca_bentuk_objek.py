import cv2
import numpy as np

#! rescale saja default 75 persen 640x320
def rescale_frame (frame, percent=75) :
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

##! port webcam di sesuaikan, nilai 0 untuk internal dan 1 untuk eksternal
cap = cv2.VideoCapture(1)
while True:
    _, frame = cap.read()
    image = rescale_frame(frame, percent=60)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(gray, 10, 250)
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    jumlah = str(len(contours))
    print("Jumlah Objek terdeteksi :", jumlah)
    result_contour = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    ##! tambahan
    for i in range(int(jumlah)):
    ##! Perhatikan jika nilai perimeter =0 maka akan muncul error zero division
        area = cv2.contourArea(contours[i])
        perimeter = cv2.arcLength(contours[0], True)
        TR = (4*np.pi*area)/(perimeter**2)
####? nilai TR ukur sendiri sesuai hasil dari benda dan labeli benda dengan namanya masing-masing
        if TR <= 0.52:
            bentuk = "Segitiga"
        elif TR <= 0.68:
            bentuk = "Persegi Panjang"
        elif TR <= 0.76:
            bentuk = "Persegi"
        else:
            bentuk = "lainnya"
        print("Nilai Thinnes Ratio : ", TR)
        print("Bentuk Benda : ", bentuk)

    cv2.imshow("Result Contours", result_contour)
    cv2.imshow("Kamera", gray)
    cv2.imshow("Canny", edge)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: #key esc
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
