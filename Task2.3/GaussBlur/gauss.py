import cv2 as cv
import matplotlib.pyplot as plt

resim = cv.imread('logo.png')
#blur
blur = cv.GaussianBlur(resim, (15, 15), 0)  

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(resim, cv.COLOR_BGR2RGB))
plt.title('Orjinal')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv.cvtColor(blur, cv.COLOR_BGR2RGB))
plt.title('GaussianBlur')
plt.axis('off')

cv.imwrite('logogaus.jpg', blur)

plt.show()
