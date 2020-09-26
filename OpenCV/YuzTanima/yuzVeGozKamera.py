import cv2

yuz_casc = cv2.CascadeClassifier(r"haarcascades\haarcascade_frontalface_default.xml")
goz_casc= cv2.CascadeClassifier(r"haarcascades\haarcascade_eye.xml")
kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()
    gri_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    yuzler = yuz_casc.detectMultiScale(gri_goruntu, 1.1, 4)#gri resim, resmin buyutulme oranı, resim taranırken her aday dikdörtgenin kaç adet komşusu olması gerektiğini söyluyoruz

    for (x, y, w, h) in yuzler:
        cv2.rectangle(goruntu, (x, y), (x+w, y+h), (255, 0, 0), 2)
        yuz_bolgesi = goruntu[y:y+h, x:x+w]
        gri_yuz_bolgesi = cv2.cvtColor(yuz_bolgesi, cv2.COLOR_BGR2GRAY)
        gozler = goz_casc.detectMultiScale(gri_yuz_bolgesi, 1.1, 4)
        for (ex, ey, ew, eh) in gozler:
            cv2.rectangle(yuz_bolgesi, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow("Yuz", goruntu)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()