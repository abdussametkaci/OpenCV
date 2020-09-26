import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()

    #nesne tespitiyaparken gri tonlarda uğraşmak daha kolaydır çünkü gride 1 renk kanalı varken renklide 3 kanal vardır
    #nesne tespiti yapılırken elimizdeki nesnein fotosunu videonun tamamını tarayarak tespit etmeye çalışacağız
    #bu kötü bir yol çünkü elimizde nesnenin sadece tek bir açıyla çekilmiş tek bir fotoğrafı var
    gri_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    nesne = cv2.imread("nesne.png", 0)

    h, w = nesne.shape # nesnenin boyutları
    res = cv2.matchTemplate(gri_goruntu, nesne, cv2.TM_CCOEFF_NORMED)


    esik_deger = 0.8
    local = np.where(res > esik_deger)
    # where numpy array'in içindeki her bir değeri karşılaştırı ve içindeki koşula bağlı olarak sağlanan değerler ile bir numpy array döndürür

    for n in zip(*local[::-1]):
        cv2.rectangle(goruntu, n, (n[0]+w, n[1]+h), (0, 255, 0),  2)
        cv2.putText(goruntu, "Anahtarlik", (n[0]+5, n[1]+2), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 1)

    cv2.imshow("Goruntu", goruntu)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()