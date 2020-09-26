import cv2

video = cv2.VideoCapture("video_insan.avi")
full_body = cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    ret, goruntu = video.read()

    gri_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    insanlar = full_body.detectMultiScale(gri_goruntu, 1.1, 6)

    for (x, y, w, h) in insanlar:
        cv2.rectangle(goruntu, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Insanlar", goruntu)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()