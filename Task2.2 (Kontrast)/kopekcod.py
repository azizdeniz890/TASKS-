import cv2
import numpy as np
import matplotlib.pyplot as plt

#deger ataması
yol = 'kopek.png'
alpha = 2.0
beta = -100

#gri sekle getirme
resim = cv2.imread(yol, cv2.IMREAD_GRAYSCALE)

#genisletme islemi
min_intensity = np.min(resim)
max_intensity = np.max(resim)
gen_resim = np.clip(alpha * resim + beta, 0, 255).astype(np.uint8)

#plt ile gösterim islemi
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(resim, cmap='gray')
plt.title('Orijinal')
plt.axis('off')  

plt.subplot(1, 2, 2)
plt.imshow(gen_resim, cmap='gray')
plt.title('Contrast Stretching(Genişletilmiş Kontrast)')
plt.axis('off')  

plt.tight_layout()
plt.show()

#son kaydetme asaması
cv2.imwrite('kopek_gri.png', resim)
cv2.imwrite('genis_kopek.png', gen_resim)



