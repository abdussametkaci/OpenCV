import cv2
import numpy as np

resim = cv2.imread("santranc.png")

gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
gri_resim = np.float32(gri_resim)
# resim (tek kanallı olmalı ve 32 bit float olmalı), max köşe sayısı, kalite seviyesi, bakılacak min piksel
koseler = cv2.goodFeaturesToTrack(gri_resim, 85, 0.01, 10)
koseler = np.int0(koseler) # numpy array deki tüm değerleri unsigned int yapar

sayi = 0
for kose in koseler:
    x, y = kose.ravel() # dizi deki x, y değerlerini atar
    cv2.circle(resim, (x, y), 5, (255, 0, 0), -1) # sonda -1 dersek nokt yapar
    sayi += 1

cv2.imshow("Resim", resim)
print(sayi)

cv2.waitKey(0)
cv2.destroyAllWindows()