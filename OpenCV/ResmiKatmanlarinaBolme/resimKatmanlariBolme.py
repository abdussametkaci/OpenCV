import cv2

resim = cv2.imread("robertdowneyjr.jpg")

b, g, r = cv2.split(resim)

cv2.imshow("Orjinal", resim)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

yeni_resim = cv2.merge((b, g, r)) # üç ayr kanaldaki resimleri birleştirir
cv2.imshow("Yeni Resim", yeni_resim)

cv2.waitKey(0)