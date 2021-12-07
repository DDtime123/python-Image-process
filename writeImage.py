# 写入图像
# 引入系统库，提供获取目录的方法
# 导入PIL库
from PIL import Image
import os,sys

from PIL import Image
import cv2 as cv
import os
 
def PNG_JPG(PngPath):
    img = cv.imread(PngPath, 0)
    w, h = img.shape[::-1]
    infile = PngPath
    outfile = os.path.splitext(infile)[0] + ".jpg"
    img = Image.open(infile)
    img = img.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=70)
            os.remove(PngPath)
        else:
            img.convert('RGB').save(outfile, quality=70)
            os.remove(PngPath)
        return outfile
    except Exception as e:
        print("PNG转换JPG 错误", e)

# Image对象使用save方法存储图像文件
# 将文件转换为JPEG
# sys.argv[1:]是使用 python file.py [args]调用该python模块时的参数[args]
for infile in sys.argv[1:]:
    f,e = os.path.splitext(infile)
    outfile = f + ".png"
    print(outfile)
    if infile != outfile:
        try:
            #img = Image.open("image.png")
            #print(img.size)
            with Image.open(outfile) as im:
                print(im.size)
                im.save(f+'.jpg')
                im.save(f+'.png')
                im.save(f+'.bmp')
        except OSError as e:
            print('cannot convert',str(e))