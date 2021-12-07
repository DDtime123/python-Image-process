# 使用精细边缘检测检测出来的边缘，使用霍夫圆变换检测出圆
from PIL import Image, ImageDraw
from math import sqrt, pi, cos, sin
from canny import canny_edge_detector
from collections import defaultdict
import cv2
import numpy as np

# 加载图像:
input_image = Image.open('Image-Progcess/image2.png')

# 输出图像:
output_image = Image.new("RGB", input_image.size)
output_image.paste(input_image)
draw_result = ImageDraw.Draw(output_image)
"""
#kernel = np.ones((5,5),np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
open_cv_image = np.array(input_image)
open_cv_image = open_cv_image[:, :, ::-1].copy() 
erosion = cv2.erode(open_cv_image,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 2)
cv2.imshow("erosion",erosion)
cv2.waitKey(0)
cv2.imshow("dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
#img = cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB)

input_image = Image.fromarray(img)
output_image.paste(input_image)
draw_result = ImageDraw.Draw(output_image)
"""
# 监测圆
rmin = 18
rmax = 40
steps = 100
threshold = 0.3

points = []
for r in range(rmin, rmax + 1):
    for t in range(steps):
        points.append((r, int(r * cos(2 * pi * t / steps)), int(r * sin(2 * pi * t / steps))))

acc = defaultdict(int)
for x, y in canny_edge_detector(input_image):
    for r, dx, dy in points:
        a = x - dx
        b = y - dy
        acc[(a, b, r)] += 1

circles = []
for k, v in sorted(acc.items(), key=lambda i: -i[1]):
    x, y, r = k
    if v / steps >= threshold and all((x - xc) ** 2 + (y - yc) ** 2 > rc ** 2 for xc, yc, rc in circles):
        print(v / steps, x, y, r)
        circles.append((x, y, r))

for x, y, r in circles:
    draw_result.ellipse((x-r, y-r, x+r, y+r), outline=(255,0,0,0))

# 保存输出图像
output_image.save("result.png")