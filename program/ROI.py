import cv2
cap = cv2.VideoCapture(1)
while True:
    #!open camera
    _, frame = cap.read()
    # print(frame.shape[0], frame.shape[1])
    #ROI
    x1 = 20
    y1 = 10
    x2 = 200
    y2 = 150
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255, 0, 0), 1)
    roi = frame[ y1:y2, x1:x2 ]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('NamaFrame', frame)
    cv2.imshow('Nama ROI', roi)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: #esc key
        break

    #Untuk Save
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite("../image/copy.jpg", roi)

cap.release()
cv2.destroyAllWindows()