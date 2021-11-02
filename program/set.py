import cv2
import os

if not os.path.exists("../data"):
    os.makedirs('../data')
    os.makedirs('../data/test')
    os.makedirs('../data/train')

    os.makedirs('../data/test/satu')
    os.makedirs('../data/test/dua')
    os.makedirs('../data/test/tiga')

    os.makedirs('../data/train/satu')
    os.makedirs('../data/train/dua')
    os.makedirs('../data/train/tiga')

#membuka kamera
dirs = "data/train/"
cap = cv2.VideoCapture(1)
i = 0
while True:
    #!open camera
    _, frame = cap.read()

    # ROI
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = int(frame.shape[1] - 10)
    y2 = int(0.5 * frame.shape[1])

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    roi = th[y1:y2, x1:x2]
    # roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(roi, (100, 100))
    # _, roi = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('Gray', gray)
    cv2.imshow('Frame', frame)
    cv2.imshow('ROI', roi)
    interrupt = cv2.waitKey(10)

    if interrupt & 0xFF == 27: #esc key
        break

    #Untuk Save
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite("../image/copy1.jpg", roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite("../" + dirs + "/satu/satu.jpg", roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite("../" + dirs + "/dua/dua.jpg", roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite("../" + dirs + "/tiga/tiga.jpg", roi)
    # if interrupt & 0xFF == ord(str(i)):
    #     cv2.imwrite("../" + dirs + "/satu/" + str(i) + ".jpg", roi)
    #     i += 1

cap.release()
cv2.destroyAllWindows()