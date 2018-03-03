import numpy as np
import cv2
'''
cap = cv2.VideoCapture('ball_test.h264')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.imwrite('camframe2.jpeg',gray)
        break

cap.release()
cv2.destroyAllWindows()

'''
img1 = cv2.imread('camframe2.jpeg')
cv2.imshow('gray',img1)

retval, img2	=	cv2.threshold(img1,80, 100, cv2.THRESH_BINARY_INV)
cv2.imshow('threshold', img2)

colsum = np.sum(img2,axis = 0)
rowsum = np.sum(img2,axis = 1)

cent = np.array([np.argmax(rowsum), np.argmax(colsum)])
print cent

cv2.waitKey(0)
cv2.destroyAllWindows()
