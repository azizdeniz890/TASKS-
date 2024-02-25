import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

r = cv.imread('opening.png', 0)

kernel = np.ones((5, 5), np.uint8)

opening = cv.morphologyEx(r, cv.MORPH_OPEN, kernel)

plt.figure()

plt.subplot(1, 2, 1)
plt.imshow(r, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(opening, cmap='gray')
plt.title('Open')
plt.axis('off')

plt.gcf().set_facecolor('red')  

cv.imwrite('openoldu.png', opening)

plt.show()
