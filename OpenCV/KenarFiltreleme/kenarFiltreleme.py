import cv2
import numpy as np

resim = cv2.imread("bilimInsanlari.jpg")
#resim = cv2.GaussianBlur(resim, (15, 15), 0)

# laplacian
laplacian = cv2.Laplacian(resim, cv2.CV_64F)
abs_laplacian = cv2.convertScaleAbs(laplacian)

# sobel y
sobel_dikey = cv2.Sobel(resim, cv2.CV_64F, 0, 1, ksize=5)
abs_sobel_y = cv2.convertScaleAbs(sobel_dikey)

#sobel x
sobel_yatay = cv2.Sobel(resim, cv2.CV_64F, 1, 0, ksize=5)
abs_sobel_x = cv2.convertScaleAbs(sobel_yatay)

cv2.imshow("Orjinal Resim", resim)
cv2.imshow("Laplacian", abs_laplacian)
cv2.imshow("Sobel Y", abs_sobel_y)
cv2.imshow("Sobel X", abs_sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""NOT = Ya resmi gausiuan blur ile filtreleyeip sonra kenar filtreleme nesneleri ile işlem yaparsın ya da
filtreleme yapmayıp convertScaleAbs ile kenarları daha  da belirgimleştitrirsin aksi taktirde iyi görüntü
çıkmıyor"""