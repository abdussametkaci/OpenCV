import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk = np.array([90, 50, 50])
yuksek = np.array([130, 255, 255])

while True:

    ret, goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, dusuk, yuksek) # burada goruntuyu verdiğimiz hsv aralığındaki renk değerlerini beyaz diğer renkleri siyah yapacaktır
    # seçtiğimiz aralıkmavi tonları(HSV renk aralıklarına internetten bak)

    resim = cv2.bitwise_and(goruntu, goruntu, mask=mask)# burada mask görüntüsü ile adn lerken siyahlar baskın gelip siyah görünür
    #çünkü siyah bitler 0 dır ve siyah görünür
    #ancak diğer mask da beyaz alan ile and lersek o rengi tespit oluruz ve hsv uzayındaki rengi filtrelemiş oluruz

    cv2.imshow("BGR Goruntu", goruntu)
    cv2.imshow("Mask", mask)
    cv2.imshow("HSV(HUE, STRATION, VALUE)", hsv)
    cv2.imshow("Renk algılama", resim)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()