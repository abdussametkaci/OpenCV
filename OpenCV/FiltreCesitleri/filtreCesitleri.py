import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk = np.array([90, 50, 50])
yuksek = np.array([130, 255, 255])

while True:

    ret, goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, dusuk, yuksek)

    resim = cv2.bitwise_and(goruntu, goruntu, mask=mask)

    # Smoothed
    kernel = np.ones((15, 15), dtype=np.float32) / 225
    smoothed = cv2.filter2D(resim, -1, kernel)

    # Gauision Blur
    blur = cv2.GaussianBlur(resim, (15, 15), 0)

    # Median
    median = cv2.medianBlur(resim, 15)

    # bilateral
    bilateral = cv2.bilateralFilter(resim, 15,75, 75)

    cv2.imshow("BGR Goruntu", goruntu)
    cv2.imshow("Mask", mask)
    cv2.imshow("Gauision Blur", blur)
    cv2.imshow("Renk Algilama", resim)
    cv2.imshow("Smoothed", smoothed)
    cv2.imshow("Median", median)
    cv2.imshow("Bilateral", bilateral)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()