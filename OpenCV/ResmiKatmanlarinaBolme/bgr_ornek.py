import cv2

resim = cv2.imread("robertdowneyjr.jpg")

#resim[50, 50] = [255, 255, 255] # resmin 50x50 inci pikselindeki değeri beyaz olarak değiştirdik

for i in range(200):
    resim[50, i] = [255, 255, 255]

bolge = resim[400:500, 200:350] # 100'den 200'e olan yukseklik ve 200'den 350'ye olan genişlikte resmin parçasını al
resim[0:100:, 0:150] = bolge

cv2.imshow("Robert Downey JR", resim)
cv2.imshow("Kesilen Bolge", bolge)

cv2.waitKey(0)
cv2.destroyAllWindows()