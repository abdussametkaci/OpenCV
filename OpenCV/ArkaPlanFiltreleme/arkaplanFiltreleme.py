import cv2
import numpy as np

def main():
    resim = cv2.imread("resim.jpg")

    mask = np.zeros(resim.shape[:2], np.uint8) # (480, 640, 3) değerinin (480, 640) değerini shape[:2] ile aldık

    print(mask.shape)
    print(resim.shape[:2])

    bgdModel = np.zeros((1, 65), dtype=np.float64)
    fgdModel = np.zeros((1, 65), dtype=np.float64)

    rect = (50, 0, 400, 640) # üzerinde çalışılacak alanın koordinatları

    cv2.grabCut(resim, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    #arka planda 0 veya 2 piksellere 0, ön planda 1 veya 3 piksellere 1 değeri atılır
    mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype(np.uint8) # 0 veya 2 ise 0 değerini ata, aksi taktirde 1 değerini ata
    #----------------------------------------------------------------------------------------------
    #resim ve maske 480x640 piksellik olduğu için bu iki matrsi çarpamayız
    #matrislerin çarpılabilmesi için birincinin satırı ile ikincisinin sütunu eşit olmalıdır
    #bunu için de ikinci matrisin transpozesini aldık ve 640,480 lik bir matris oldu
    resim = resim * mask2[:, :, np.newaxis] # transpozesini alıp çarptık

    """np.newaxis aslında diziye yeni bir boyut katar
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) şöyle bir dizimiz olsun
    >>> a[:, np.newaxis]
    array([[0],
           [1],
           [2],
           [3],
           [4],
           [5],
           [6],
           [7],
           [8],
           [9]])
    >>> a[:, np.newaxis].shape
    (10, 1) bu sonuç çıkar
    
    VEYA 
    alttaki gibi kullanılırsa
    >>> a[np.newaxis, :]  # The output has 2 [] pairs!
    array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
    >>> a[np.newaxis, :].shape
    (1, 10)
    
    Birden fazla kullanımda ise;
    
    >>> a[np.newaxis, :, np.newaxis]  # note the 3 [] pairs in the output
    array([[[0],
            [1],
            [2],
            [3],
            [4],
            [5],
            [6],
            [7],
            [8],
            [9]]])
    >>> a[np.newaxis, :, np.newaxis].shape
    (1, 10, 1)
BU ŞEKİLDEDİR
"""
    """
    for x in range(mask2.shape[0]):
        for y in range(mask2.shape[1]):
            print("satır {}, sütun {}, değer = {}".format(x, y, mask2[x, y]))
    """
    cv2.imshow("Resim", resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
