import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread('ein.jpg',0)
#histogram eşitleme
einhe = cv2.equalizeHist(resim)

fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)

fig.add_subplot(1,2,1)
plt.imshow(resim, cmap='gray')


fig.add_subplot(1,2,2)
plt.imshow(einhe, cmap='gray')

plt.show(block=True) 
#çıktı kaydetme
cv2.imwrite('ein_he_olmus_hali.png', einhe)


