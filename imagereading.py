import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

cv2.waitKey(10000)
cv2.destroyAllWindows()
