import cv2

yuz_casc = cv2.CascadeClassifier(r"haarcascades\haarcascade_frontalface_default.xml")
kamera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
kayit = cv2.VideoWriter("kayit.avi", fourcc, 30, (640, 480))

while True:
    ret, goruntu = kamera.read()
    gri_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    yuzler = yuz_casc.detectMultiScale(gri_goruntu, 1.1, 4)#gri resim, resmin buyutulme oranı, resim taranırken her aday dikdörtgenin kaç adet komşusu olması gerektiğini söyluyoruz

    for (x, y, w, h) in yuzler:
        cv2.rectangle(goruntu, (x, y), (x+w, y+h), (255, 0, 0), 2)

    kayit.write(goruntu)

    cv2.imshow("Yuz", goruntu)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()
