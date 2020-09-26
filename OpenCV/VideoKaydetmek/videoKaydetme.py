import cv2

def main():

    kamera = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*"XVID") # video formatı belirleme (avi istedik)

    kayit = cv2.VideoWriter("kayit.avi", fourcc, 30, (640, 480)) # kayit.avi doys adi oluşuracak, format, 30 fps istediğimizi söyledik, piksel boyutu belirtik
    kayit_horizontal = cv2.VideoWriter("kayit_horizontal.avi", fourcc, 30, (640, 480))
    kayit_vertical = cv2.VideoWriter("kayit_vertical.avi", fourcc, 30, (640, 480))
    kayit_both = cv2.VideoWriter("kayit_both.avi", fourcc, 30, (640, 480))
    while True:
        ret, goruntu = kamera.read()

        horizontal_video = cv2.flip(goruntu, 0) # flip görüntüyü döndürmeye yarar, 0 dikey olarak döndürür
        vertical_video = cv2.flip(goruntu, 1) # 1 yatay olarak döndürür
        both_video = cv2.flip(goruntu, -1) # -1 ise hem yatay hem de dikey olarak dödürür
        if ret == True:
            kayit.write(goruntu)
            kayit_horizontal.write(horizontal_video)
            kayit_vertical.write(vertical_video)
            kayit_both.write(both_video)

        cv2.imshow("Goruntu", goruntu)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()