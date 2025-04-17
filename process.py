import cv2

# Görüntüyü yükle
image = cv2.imread('ornek_resim.jpg')

# Görüntüyü gri tona çevir
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntüyü bulanıklaştır
blurred_image = cv2.GaussianBlur(gray_image, (7, 7), 0)

# Görüntüleri göster
cv2.imshow('Orijinal', image)
cv2.imshow('Gri Tonlama', gray_image)
cv2.imshow('Bulanık', blurred_image)

# Bir tuşa basılana kadar bekle ve ardından pencereleri kapat
cv2.waitKey(0)
cv2.destroyAllWindows()