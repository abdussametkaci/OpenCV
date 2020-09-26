import cv2

resim = cv2.imread("robertdowneyjr.jpg")

#0 -> blue; 1->yeşil; 2 -> red
resim[:, :, 1] = 255 # resmin tüm piksellerini mavi yapar, çünkü 1. katman yeşil ve yeşilin baskın olmasını sağlar(en yuksek değer 255);(0, 255) alınabilecek değerler
cv2.imshow("Yeni Resim", resim)

cv2.waitKey(0)