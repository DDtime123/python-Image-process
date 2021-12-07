# 导入所需库
import numpy as np
import imutils
import cv2
# 转换为灰度图像
image = cv2.imread('Image-Progcess/tiaoxingma2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 使用Scharr算子的边缘检测方法
ddepth = cv2.CV_32F if imutils.is_cv2() else cv2.CV_32F
gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)
gradient = cv2.subtract(gradX,gradY)
gradient = cv2.convertScaleAbs(gradient)
#去除噪声
## 模糊和阈值化处理
blurred = cv2.blur(gradient,(9, 9))
(_, thresh) = cv2.threshold(blurred, 231, 255, cv2.THRESH_BINARY)
## 形态学处理
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)
# 确定检测轮廓，画出检测框
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
 
rect = cv2.minAreaRect(c)
box = cv2.boxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
box = np.int0(box)
 
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()