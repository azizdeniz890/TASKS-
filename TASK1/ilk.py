#ortam çağrılıyor
import cv2

#resim okuma:
resim = cv2.imread("gus.jpg")

#resim = cv2.imread("gus.jpg",0) siyah beyaz basar

#resim açılıyor
cv2.imshow("resim penceresi",resim)

#resim açıldıktan sonra bekleme kodu
cv2.waitKey(0)

#herhangi bir tuşa basıldığında kapama
cv2.destroyWindow("resim penceresi")
