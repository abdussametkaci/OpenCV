import cv2
import numpy as np

def main():
    resim = cv2.imread("android.jpg")
    resim2 = np.zeros((400, 400, 3), dtype="uint8")
    cv2.rectangle(resim2, (100, 300), (300, 100), (255, 255, 255), 3)
    cv2.imshow("numpy resim", resim2)
    print(resim2)

    iki_kat_buyuk = cv2.pyrUp(resim)
    iki_kat_kucuk = cv2.pyrDown(resim)

    print(resim.shape)
    print(iki_kat_buyuk.shape)
    print(iki_kat_kucuk.shape)

    cv2.imshow("orjinal", resim)
    cv2.imshow("iki kat buyuk resim", iki_kat_buyuk)
    cv2.imshow("iki kat kucuk resim", iki_kat_kucuk)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()