import cv2

def main():
    resim1 = cv2.imread("feyyaz_yigit.jpg")
    resim2 = cv2.imread("android.jpg")

    #BGR ı griye çevirir
    a_gri = cv2.cvtColor(resim2, cv2.COLOR_BGR2GRAY) # resmi gri yapar(bunu imread'de ikinciparametreye 0 vererek de yapabilirdik)

    yukseklik, genislik, kanal = resim2.shape
    print(yukseklik, genislik, kanal)

    roundofimage = resim1[0:yukseklik, 0:genislik]
    cv2.imshow("ROI", roundofimage)

    print(a_gri[100, 100])

    ret, mask = cv2.threshold(a_gri, 30, 255, cv2.THRESH_BINARY) # 30 un ustundeki değere sahip pikselleri 255 değerini atar
    print("ret:", ret) #fonksiyondaki ikinci parametrenin değerini basıyor!!!!
    mask_inver = cv2.bitwise_not(mask) # resimdeki renkleri zıt renklendirir (bunu bitleri değiştirerek yapr yani 0'ı 1, 1'i de 0 yaparak)
    cv2.imshow("Ters Mask", mask_inver)

    cv2.imshow("Maskelenmiş Resim", mask)

    cv2.imshow("Feyyaz Yigit", resim1)
    cv2.imshow("Android", a_gri)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()