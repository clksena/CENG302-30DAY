import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle (gri tonlamalı)
image = cv2.imread('ornek_goruntu.jpg', cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme uygula
equalized = cv2.equalizeHist(image)

# Orijinal ve eşitlenmiş histogramları çiz
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.title('Orijinal Görüntü')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Histogram Eşitlenmiş Görüntü')
plt.imshow(equalized, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Orijinal Histogram')
plt.hist(image.ravel(), bins=256, range=[0, 256], color='black')

plt.subplot(2, 2, 4)
plt.title('Eşitlenmiş Histogram')
plt.hist(equalized.ravel(), bins=256, range=[0, 256], color='black')

plt.tight_layout()
plt.show()