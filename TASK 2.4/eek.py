import cv2
import matplotlib.pyplot as plt

i = cv2.imread('ek.jpeg')

############

scale_factor = 0.6

re = cv2.resize(i, None, fx=scale_factor, fy=scale_factor)

############

(h, w) = re.shape[:2]
center = (w // 2, h // 2)

square_size = 100

x1 = center[0] - square_size // 2
y1 = center[1] - square_size // 2
x2 = center[0] + square_size // 2
y2 = center[1] + square_size // 2

cv2.rectangle(re, (x1, y1), (x2, y2), (0, 255, 0), 2)

############

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
plt.title('Orijinal')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(re, cv2.COLOR_BGR2RGB))
plt.title('Kare')
plt.axis('off')
plt.show()
