import cv2

kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()

    laplacian = cv2.Laplacian(cv2.GaussianBlur(cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY), (3,3), 0), cv2.CV_64F)
    #abs = cv2.convertScaleAbs(laplacian)

    canny = cv2.Canny(goruntu, 100, 200)

    cv2.imshow("Orjinal", goruntu)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Canny", canny)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()