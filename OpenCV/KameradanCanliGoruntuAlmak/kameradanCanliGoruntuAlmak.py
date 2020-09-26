import cv2

kamera = cv2.VideoCapture(0) # 0 -> Bu bilgisayardaki kamera, 1 -> USB ile bağlanan kemara, veya yol verirsek o yoldaki video dosyasını açar

while True:
    ret, kare = kamera.read()

    cv2.rectangle(kare, (0, 0), (100, 100), (255, 0, 0), 3)

    bolge = kare[0:200, 0:200]

    print(kare)
    print("ret:", ret) # kameranın açık olupolmadığını söyler (açıksa true değerini döndürür)

    cv2.imshow("Video", kare)
    cv2.imshow("Bolge", bolge)

    """cv2.waitKey() foknsiyonu tuşa basılan karakterin ascii sayısını döndürür örneğin esc tuşuna basarsan 27 döner gibi.
    alttaki if statement'ında yaptığımız şey ise basılan tuşun ascii sayısı ile 0xFF sayısı yani 255 ile (bu 8 tane 1 demektir, bitwise olarak)
    ve bunu and'leyerek basılan tuşun q olup olmadığına baktık. ord() fonksiyonu da parametre olarak verilen karakterin
    ascii kodunu döndürür"""

    """İstersek kodu:
    if cv2çwaitKey(25) == ord("q"):
        break
    olarak da yazabilrdik, sadece 8 biti kesin olarak kontrol etmek istedik"""

    if cv2.waitKey(25) & 0xFF == ord("q"): # q ya basınılınca video durdurulur ve 25 ms de bir foto çekilir
        break

kamera.release()
cv2.destroyAllWindows()

