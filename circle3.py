import numpy as np
import cv2
from matplotlib import pyplot as plt


def fillHoles(otsuImg):
    # find contours
    __,contours, _ = cv2.findContours(otsuImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # filter out contours by size
    small_cntrs = []
    for con in contours:
        area = cv2.contourArea(con)
        # print(area)
        if area < 1000: # size threshold
            small_cntrs.append(con)
    cv2.drawContours(otsuImg, small_cntrs, -1, 0, -1)

# load the image
img = cv2.imread('Image-Progcess/image2.png')
img_pyr = cv2.pyrMeanShiftFiltering(img, 21, 51)
img_median = cv2.medianBlur(img_pyr, 9)
img_gray = cv2.cvtColor(img_median, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# fill holes of RBC
fillHoles(img_thresh)

# invert the image
img_thresh = cv2.bitwise_not(img_thresh)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(img_thresh,cv2.MORPH_OPEN,kernel, iterations=2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform,0.1*dist_transform.max(),255,0)
# _, sure_fg = cv2.threshold(np.uint8(dist_transform), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]


cv2.imshow('markers2', np.uint8(markers))
cv2.imshow('Final output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()