import cv2
import numpy as np
from matplotlib import pyplot as plt
from canny import compute_grayscale
from canny import compute_blur
# 读取图像
#img = cv2.imread('Image-Progcess/image2.png')
img = cv2.imread('Image-Progcess/tiaoxingma2.jpg')
# 灰色图像
img = cv2.medianBlur(img,5)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.uint8)
# 开运算
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

# 闭运算
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
#形态梯度
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
# 画圆
def drawCircle(image):
    # 霍夫圆变换
    circles = cv2.HoughCircles(
    image,
    cv2.HOUGH_GRADIENT,
    1,
    20,
    param1=30,
    param2=50,
    minRadius=10,
    maxRadius=0
    )
    
    # 确保至少找到了一些圆圈
    output = image.copy()
    if circles is not None:
        # 将圆的 (x, y) 坐标和半径转换为整数
        circles = np.round(circles[0, :]).astype("int")
        # 循环 (x, y) 坐标和圆的半径
        for (x, y, r) in circles:
    		# 在输出图像中绘制圆形，然后绘制矩形
            # 对应圆心
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        # 显示输出图像
        cv2.imshow("output", np.hstack([image, output]))
        cv2.waitKey(0)


# 制作内核
#size = np.size(blurred)
#skel = np.zeros(blurred.shape, np.uint8)
#ret, image_edit = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

#kernel = np.ones((5,5),np.uint8)
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
#erosion = cv2.erode(blurred,kernel,iterations = 3)
#dilation = cv2.dilate(erosion,kernel,iterations = 3)

#cv2.imshow("erosion",erosion)
#cv2.imshow("dilation",dilation)
#drawCircle(erosion)
#drawCircle(dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()