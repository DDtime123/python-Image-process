from PIL import Image, ImageDraw
import numpy as np
from math import sqrt

# 加载图片
input_image = Image.open('Image-Progcess/image2.png')
input_pixels = input_image.load()
width, height = input_image.width, input_image.height

# 创建输出图片
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# 转化为灰度图片
intensity = np.zeros((width, height))
for x in range(width):
    for y in range(height):
        intensity[x, y] = sum(input_pixels[x, y]) / 3

# 计算强度与核s之间的卷积
for x in range(1, input_image.width - 1):
    for y in range(1, input_image.height - 1):
        magx = intensity[x + 1, y] - intensity[x - 1, y]
        magy = intensity[x, y + 1] - intensity[x, y - 1]

        # 用黑白绘制大小
        color = int(sqrt(magx**2 + magy**2))
        draw.point((x, y), (color, color, color))
    
output_image.save("edge.png")