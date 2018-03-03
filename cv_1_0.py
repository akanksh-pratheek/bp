import numpy as np
import cv2
img1 = cv2.imread('bnp1.jpeg',0)
cv2.imshow('gray',img1)

retval, img2	=	cv2.threshold(img1,100, 100, cv2.THRESH_BINARY_INV)
cv2.imshow('threshold', img2)

colsum = np.sum(img2,axis = 0)
rowsum = np.sum(img2,axis = 1)

cent = np.array([np.argmax(rowsum), np.argmax(colsum)])
print cent

cv2.waitKey(0)
cv2.destroyAllWindows()  
