import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

r = cv.imread('closing.png', 0)

kernel = np.ones((5, 5), np.uint8)

closing = cv.morphologyEx(r, cv.MORPH_CLOSE, kernel)

plt.figure()

plt.subplot(1, 2, 1)
plt.imshow(r, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(closing, cmap='gray')
plt.title('Close')
plt.axis('off')

plt.gcf().set_facecolor('yellow')

cv.imwrite('Close.png', closing)

plt.show()
