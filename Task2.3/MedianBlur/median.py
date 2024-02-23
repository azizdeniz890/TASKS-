import cv2 as cv
import matplotlib.pyplot as plt

#cammen
resim1 = cv.imread('cammen.jpg')
mb1 = cv.medianBlur(resim1, 15)

#logo
resim2 = cv.imread('opclogo.jpg')
mb2 = cv.medianBlur(resim2, 15)

plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(cv.cvtColor(resim1, cv.COLOR_BGR2RGB))
plt.title('Orjinal')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(cv.cvtColor(mb1, cv.COLOR_BGR2RGB))
plt.title('Median Blur')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(cv.cvtColor(resim2, cv.COLOR_BGR2RGB))
plt.title('Orjinal')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(cv.cvtColor(mb2, cv.COLOR_BGR2RGB))
plt.title('Median Blur')
plt.axis('off')

plt.tight_layout()

plt.show()




















