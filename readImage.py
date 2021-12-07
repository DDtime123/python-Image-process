# 导入PIL库
from PIL import Image
# 使用 Image 类读取图像
img = Image.open("Image-Progcess/image.png")
# 查看图像的信息
print(img.format,img.size,img.mode)
# 显示图像
img.show()

