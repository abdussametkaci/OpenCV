import cv2

resim = cv2.imread("kemalsunal.jpg")

print(resim) #resmin matrisini basar
print(type(resim))
print(resim.size) # resimdeki piksel sayısı(tüm katmanların toplamını verir)
print(resim.shape) # resmin boyutlarını ve kaç katmandan(channel-renk kanalı) oluştuğunu söyler (BGR 3 katmandır gri resim 1 katmandır)
#NOT=openCV'de görüntü işleme mantığında RGB değil BGR dır!!!
print(337*600*3)
print(resim.dtype) # resmin veri tipi
cv2.imshow("Kemal Sunal", resim)
"""
resim2 = cv2.imread("kemalsunal.jpg", 0)
cv2.imshow("Kemal Sunal", resim2)
print(resim2) # her bir pikselin rengini basar ve o da tek boyutludur renkli resimdeki gibi üçlü değildir
"""

# item fonkisyonu verdiğimiz piksel ve katman değerindeki rengin değerini basar
print(resim.item(100, 100, 0)) # Blue değeri
print(resim.item(100, 100, 1)) # Green değeri
print(resim.item(100, 100, 2)) # Red değeri
# NOT = gri bir resim kullanılırsa eğer katman değeri verilmez çünkü zaten tek renk kanalı kullanılmış olur
cv2.waitKey(0)
cv2.destroyAllWindows()