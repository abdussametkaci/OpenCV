import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("pokemon.jpg")
resim_siyah_beyaz = cv2.imread("pokemon.jpg", 0)
# eğer flags adlı parametreye 0 verirsek rgb'yi kaldırır ve resim siyah beyaz olur, 0 yazmazsak orjinal hali ile kalır
cv2.imshow("Pokemon Resmi", resim)
cv2.imwrite("pokemon_kopya.jpg", resim_siyah_beyaz) # yeni bir dosyada resmimizi kopyalar
#cv2.imshow("Pokemaonnn", resim_siyah_beyaz) // aynıanda farklı resimler de gösterilebilir
cv2.waitKey(0) # herhangi bir tuşu beklemesini söyledik, herhangi bir tuşa basınca pencere kapanır
cv2.destroyAllWindows() #çarpıya basıldığında tüm opencv pencerelerini kapatır
