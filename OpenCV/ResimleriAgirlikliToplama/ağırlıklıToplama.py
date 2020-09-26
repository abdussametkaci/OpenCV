import cv2

def main():
    resim1 = cv2.imread("resim1.jpg")
    resim2 = cv2.imread("resim2.jpg")

    yazi1 = """
    Resim1 Değerleri
    Yükseklik   Genişlik    Kanal Sayısıs
      {}          {}           {}
    """.format(resim1.shape[0], resim1.shape[1], resim1.shape[2])

    yazi2 = """
    Resim2 Değerleri
    Yükseklik   Genişlik    Kanal Sayısıs
       {}         {}           {}
    """.format(resim2.shape[0], resim2.shape[1], resim2.shape[2])

    print(yazi1)
    print(yazi2)

    print(resim1[150, 150])
    print(resim2[150, 150])
    print(resim1[150, 150] + resim2[150, 150])#her katman ayrı ayrı olarak toplanmıştır, eğer 255 igeçerse mod 256 sı alınıp değer döndürülür
    print(cv2.add(resim1[150, 150], resim2[150, 150]))#burda da toplanır ancak eğer 255 i geçerse max doygunluğa ulaştığı için 255 olarak döner

    toplam = cv2.add(resim1, resim2)
    agirlikli_toplam = cv2.addWeighted(resim1, 0.2, resim2, 0.8, 0)
    #resimlere belirli bir ağırlık verilerek birleştirme yapar
    #ağırlık toplamları 1 olmalıdır

    cv2.imshow("resim1", resim1)
    cv2.imshow("resim2", resim2)
    cv2.imshow("toplam", toplam)
    cv2.imshow("agirlikli", agirlikli_toplam)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
