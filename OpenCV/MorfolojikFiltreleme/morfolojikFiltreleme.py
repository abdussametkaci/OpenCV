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

    kernel = np.ones((5, 5), np.uint8) # 5x5 piksellik alan için filtrelemeler yapar

    erosion = cv2.erode(mask, kernel, iterations=1)
    diolation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("BGR Goruntu", goruntu)
    cv2.imshow("Mask", mask)
    cv2.imshow("HSV(HUE, STRATION, VALUE)", hsv)
    cv2.imshow("Renk algılama", resim)
    cv2.imshow("erosion", erosion)
    cv2.imshow("diolation", diolation)
    cv2.imshow("opening", opening)
    cv2.imshow("closing", closing)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()