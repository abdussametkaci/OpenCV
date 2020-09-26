import cv2

resim = cv2.imread("barbara_palvin.jpg")

# rectangle fonksiyonu resimde belirli bir alanı seçmeye yarar
#resmin sol en üst köşesi (0, 0) noktası olarak kabul ederek ikitane noktanın koordinatını verdik
#ilk koordinat sol köşenin koordinatı, ikinci koordinat ise sağ köşenin koordinatı
# sonrasında renk verdik ve diğeinde ise alanın kalınlığını belirledik (0,9) arasında
cv2.rectangle(resim, (50, 150), (100, 300), [0, 0, 255], 2)
cv2.imshow("Barbara Palvin", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()