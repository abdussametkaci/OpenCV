import cv2

def main():
    resim1 = cv2.imread("feyyaz_yigit.jpg")
    resim2 = cv2.imread("android.jpg")

    a_gri = cv2.cvtColor(resim2, cv2.COLOR_BGR2GRAY) # resmi gri yapar(bunu imread'de ikinciparametreye 0 vererek de yapabilirdik)

    yukseklik, genislik, kanal = resim2.shape

    roundofimage = resim1[0:yukseklik, 0:genislik]
    cv2.imshow("ROI", roundofimage)

    ret, mask = cv2.threshold(a_gri, 30, 255, cv2.THRESH_BINARY) # 30 un ustundeki değere sahip pikselleri 255 değerini atar
    mask_inver = cv2.bitwise_not(mask) # resimdeki renkleri zıt renklendirir (bunu bitleri değiştirerek yapr yani 0'ı 1, 1'i de 0 yaparak)

    #ilk paramete kullanılacak alan ikinci alan mask yapılacak resim
    feyyazarka = cv2.bitwise_and(roundofimage, roundofimage, mask = mask_inver) # bitlerle and işlemi yapar
    cv2.imshow("feyyaz arka", feyyazarka)

    toplam = cv2.add(feyyazarka, resim2)
    cv2.imshow("toplam", toplam)

    resim1[0:yukseklik, 0:genislik] = toplam
    cv2.imshow("asdaf", resim1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()