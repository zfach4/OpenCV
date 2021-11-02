import cv2

cap = cv2.VideoCapture(0); #variable untuk pengambilan video menggunakan device default
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) #merekam video

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read() #variable untuk mulai memuat video
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #merubah warna camera menjadi gray
        cv2.imshow('frame', gray) #mejalankan video dengan kamera

        if cv2.waitKey(1) & 0xFF == ord('q'): #untuk keluar dari loop
           break

cap.release() #setelah read() video maka harus di release()
out.release()
cv2.destroyAllWindows()