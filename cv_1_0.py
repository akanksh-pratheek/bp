import time
start_time = time.time()
import numpy as np
import cv2

cap = cv2.VideoCapture('ball_test.avi')
centroid = np.zeros((430,430))

fcount = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray2 = gray[50:480,90:520]
        retval,bw	= cv2.threshold(gray2,80, 100, cv2.THRESH_BINARY_INV)
        colsum = np.sum(bw,axis = 0)
        rowsum = np.sum(bw,axis = 1)
        cent = np.array([np.argmax(rowsum), np.argmax(colsum)])
        print cent
        centroid[cent[0],cent[1]] = 255
        cv2.imshow('frame',centroid)
        fcount = fcount + 1

    else:
        break

cap.release()
cv2.destroyAllWindows()
cv2.imwrite('cent.jpeg',centroid)

print("--- %s seconds ---" % (time.time() - start_time))


'''
    centroid[cent[0],cent[1]] = 255
    cv2.imshow('frame',centroid)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.imwrite('camframe2.jpeg',gray2)
        break



cv2.imshow(centroid)
cv2.imwrite('cent.jpeg',centroid)

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

'''
