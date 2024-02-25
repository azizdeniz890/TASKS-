import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

r = cv.imread('j.png', 0)

kernel = np.ones((5, 5), np.uint8)

dilation = cv.dilate(r, kernel, iterations=1)

plt.figure()

plt.subplot(1, 2, 1)
plt.imshow(r, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dilation, cmap='gray')
plt.title('Son Hali')
plt.axis('off')

plt.gcf().set_facecolor('red')
cv.imwrite('diloldu.png', dilation)

plt.show()
