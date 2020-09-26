import cv2

yuz_casc = cv2.CascadeClassifier(r"haarcascades\haarcascade_frontalface_default.xml")

resim = cv2.imread("bilimInsanlari.jpg")

gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

yuzler = yuz_casc.detectMultiScale(gri_resim, 1.3, 4)#gri resim, resmin buyutulme oranı, resim taranırken her aday dikdörtgenin kaç adet komşusu olması gerektiğini söyluyoruz

print(yuzler)

for (x, y, w, h) in yuzler:
    cv2.rectangle(resim, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Yuz", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
