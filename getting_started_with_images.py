import cv2

img = cv2.imread('lena.jpg', -1) #membaca gambar

print(img) #melihat matriks gambar

cv2.imshow('image', img) #menampilkan gambar dalam sekejap
k = cv2.waitKey(0) #Delay Berapa lama gambar akan muncul

if k == 27:
    cv2.destroyAllWindows() #Membuat gambar dapat terus dilihat sampai di close (dalam delay 0)
elif k == ord('a'):
    cv2.imwrite('lena_copy.png', img) #untuk membuat file lain (copy)
    cv2.destroyAllWindows()