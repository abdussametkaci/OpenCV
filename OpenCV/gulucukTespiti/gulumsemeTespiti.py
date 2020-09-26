import cv2

kamera = cv2.VideoCapture(0)

yuz_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gulumseme_casc = cv2.CascadeClassifier("haarcascade_smile.xml")

while True:
    ret, goruntu = kamera.read()

    gri_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    yuzler = yuz_casc.detectMultiScale(gri_goruntu, 1.1, 4)

    for (x, y, w, h) in yuzler:
        cv2.rectangle(goruntu, (x, y), (x+w, y+h), (255, 0, 0), 2)

        agiz_bolgesi = goruntu[y:y+h, x:x+w]
        gri_agiz_bolgesi = cv2.cvtColor(agiz_bolgesi, cv2.COLOR_BGR2GRAY)
        gulumsemeler = gulumseme_casc.detectMultiScale(gri_agiz_bolgesi, 3.5, 15)

        for (ax, ay, aw, ah) in gulumsemeler:
            cv2.rectangle(agiz_bolgesi, (ax, ay), (ax+aw,ay+ah), (0, 255, 0), 2)

    cv2.imshow("Gulumseme", goruntu)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.read()
cv2.destroyAllWindows()