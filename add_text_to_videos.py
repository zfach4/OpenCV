import cv2
import datetime

cap = cv2.VideoCapture(0) #variable untuk pengambilan video menggunakan device default
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cara merubah Size kamera
cap.set(3, 3000)
cap.set(4, 1000)

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read() #variable untuk mulai memuat video
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str (cap.get(3)) + ' Height:' + str (cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame) #mejalankan video dengan kamera

        if cv2.waitKey(1) & 0xFF == ord('q'): #untuk keluar dari loop
           break
    else:
        break

cap.release() #setelah read() video maka harus di release()
cv2.destroyAllWindows()