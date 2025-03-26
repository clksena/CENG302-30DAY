import cv2
import numpy as np



img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

cv2.rectangle(img,(200,70),(320,160),(0,0,255),2)
cv2.imshow('dortgen',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
