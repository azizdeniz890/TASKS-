import cv2 as cv
import numpy as np

yol="mkus.jpg"
kus=cv.imread(yol)

esik=(70, 170, 165)#opencv bgr
b,g,r= cv.split(kus)

filtre= (b > esik[0]) & (g> esik[1]) & (r > esik[2])
b = np.where(filtre,0,b)
g = np.where(filtre,0,g)
r = np.where(filtre,0,r)

yenikus= cv.merge((b,g,r))

cv.imshow("sonuc", yenikus)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("yenimkus.jpg",yenikus)

"""
yol = "mkus.jpg"
re = cv.imread(yol)

yukseklik, genislik, _ = re.shape #yuk,gen,katman

for yuky in range(yukseklik):
    for genx in range(genislik):
        b,g,r= re[yuky,genx]
        if b> 70 and g > 170 and r> 165:
            re[yuky, genx] = [0,0,0]
"""

