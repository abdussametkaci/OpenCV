import cv2

resim = cv2.imread("barbara_palvin.jpg")

#Resmi Uzatma
#ustten alttan sağdan soldan 100 piksellik alan açtık
uzatilan_resim = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_REPLICATE)

#Resmi Aynalama
aynalanan_resim = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_REFLECT)

#Resmi Tekrar etme
tekrarlanan_resim = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_WRAP)

#Resmin Etrafını Sarma
#sarılan kısma mavi değerini verdik(default siyah)
sarilan_resim = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value =[255, 0, 0])

cv2.imshow("Orjinal", resim)
cv2.imshow("Uzatilan", uzatilan_resim)
cv2.imshow("Aynalanan", aynalanan_resim)
cv2.imshow("Tekrarlanan", tekrarlanan_resim)
cv2.imshow("Sarilan", sarilan_resim)

cv2.waitKey(0)