import cv2

def main():
    kamera = cv2.VideoCapture(0)

    kamera.set(3, 300)  # 3.parametreye 300 değerini gir (3. parametre videonun genişliği)
    kamera.set(4, 300)  # 4. parametre video yüksekliği

    while True:

        ret, kare = kamera.read()

        cv2.imshow("Kamera", kare)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()