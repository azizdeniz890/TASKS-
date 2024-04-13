import cv2

resim = cv2.imread("meyve.jpeg")

height = resim.shape[0]
width = resim.shape[1]
#meyve resminin boyutları: 800x600
scale_factor = 0.6
new_height = int(height * scale_factor)
new_width = int(width * scale_factor)

boyutlandirilmis_resim = cv2.resize(resim, (new_width, new_height))

karenin_bir_kenar_uzunlugu = 200

x1 = (new_width - karenin_bir_kenar_uzunlugu) // 2 #int bölmesi
y1 = (new_height - karenin_bir_kenar_uzunlugu) // 2
x2 = x1 + karenin_bir_kenar_uzunlugu
y2 = y1 + karenin_bir_kenar_uzunlugu

cv2.rectangle(boyutlandirilmis_resim, (x1, y1), (x2, y2), (0, 0, 255), 3)  # kırmızı ve 3 kalınlıgında

cv2.imshow("Orijinal", resim)
cv2.imshow("0.6 boyutlandirilmasi ve kare cizimi", boyutlandirilmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()




"""
                                Deneme-4 (kare çizimi)
import cv2

resim = cv2.imread("meyve.jpeg")

height, width, _ = resim.shape #yuk,genislik,katman

karenin_bir_kenar_uzunlugu = 300
#meyve 800x600
x1 = (width - karenin_bir_kenar_uzunlugu) // 2 #int bölmesi
y1 = (height - karenin_bir_kenar_uzunlugu) // 2
x2 = x1 + karenin_bir_kenar_uzunlugu
y2 = y1 + karenin_bir_kenar_uzunlugu

cv2.rectangle(resim, (x1, y1), (x2, y2), (0, 0, 255), 4)#kırmızı ve 4 kalınlıgında

cv2.imshow("Resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
height, width, _ = image.shape

karenin_kenar_uzunlugu = 670

x1 = int((width - kare_kenar_uzunlugu) / 2)
y1 = int((height - kare_kenar_uzunlugu) / 2)
x2 = x1 + kare_kenar_uzunlugu
y2 = y1 + kare_kenar_uzunlugu

cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
"""

"""
                                Deneme-3(kare çizim aşaması)
# cv2.rectangle: 
# Draws a rectangle on an image specified by the top-left corner and bottom-right corner (x, y)-coordinates

# Draw a Rectangle in
image = np.zeros((512,512,3), np.uint8)
cv2.rectangle(image, (100,100), (300,250), (127,50,127), -1)
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
                                Deneme-2 (boyutlandırma)
import cv2

image = cv2.imread("meyve.jpeg")

height = image.shape[0]
width = image.shape[1]

scale_factor = 0.6                          #scale_factor kullanımı 
new_height = int(height * scale_factor)
new_width = int(width * scale_factor)
dimensions = (new_width, new_height)
new_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Original image", image)
cv2.imshow("Resized image", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

"""
                                Deneme-1 (boyutlandırma)
import cv2

image = cv2.imread("meyve.jpeg")

height = 600
width = 600
dimensions = (width, height)
new_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Orijinal", image)
cv2.imshow("Yeniden Boyutlandırılmış", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
