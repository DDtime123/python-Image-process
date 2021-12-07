import cv2
image = cv2.imread('Image-Progcess/image2.png')
image2 = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY, 
    )
image2 = cv2.GaussianBlur(
    image2, 
    ksize=(9,9), 
    sigmaX=8,
    sigmaY=8,
    )
cv2.imwrite('blurred.png', image2)
hello, image2 = cv2.threshold(
    image2,
    thresh=150,
    maxval=255,
    type=cv2.THRESH_BINARY_INV,
    )
cv2.imwrite('thresholded.png', image2)
_,contours, hier = cv2.findContours(
    image2,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
    )
print('Number of contours: {0}'.format(len(contours)))
cv2.drawContours(
    image,
    contours=contours,
    contourIdx=-1,
    color=(0,255,0),
    thickness=2
    )
cv2.imwrite('augmented.png', image)
cv2.imshow('hello', image)
cv2.waitKey(-1)