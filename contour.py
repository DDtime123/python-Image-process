import numpy as np
import cv2

im = cv2.imread('image2.png',cv2.IMREAD_COLOR)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for data in contours:
    print ("The contours have this data %r" %data)
cv2.drawContours(im,contours,-1,(0,255,0),3)
cv2.imshow('output',im)
while True:
    if cv2.waitKey(6) & 0xff == 27:
        break