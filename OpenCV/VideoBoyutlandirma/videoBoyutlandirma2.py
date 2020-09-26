import cv2

def ayarla(kare, yuzde = 75):
    genislik = int(kare.shape[1] * yuzde / 100)
    yukseklik = int(kare.shape[0] * yuzde / 100)
    boyut = (genislik, yukseklik)
    return cv2.resize(kare, boyut, interpolation=cv2.INTER_AREA) # numpy array döndürür

def main():
    kamera = cv2.VideoCapture(0)

    # kamera.set(3, 300) # 3.parametreye 300 değerini gir (3. parametre videonun genişliği)
    # kamera.set(4, 300) # 4. parametre video yüksekliği

    while True:

        ret, kare = kamera.read()
        kare2 = ayarla(kare)
        griVideo = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Kamera", kare)
        cv2.imshow("Gri", griVideo)
        cv2.imshow("Boyutlu", kare2)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()