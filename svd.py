# 导入模块
import requests
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 分配并打开图像
#url = 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210401173418/Webp-compressed.jpg'
#response = requests.get(url, stream=True)

#with open('image.png', 'wb') as f:
#	f.write(response.content)

img = cv2.imread('image3.png')

# 将图像转换为灰度以加快速度
# 计算。
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 计算SVD
u, s, v = np.linalg.svd(gray_image, full_matrices=False)

# 检查矩阵的形状
print(f'u.shape:{u.shape},s.shape:{s.shape},v.shape:{v.shape}')

# 导入模块
import seaborn as sns 

var_explained = np.round(s**2/np.sum(s**2), decimals=6)
 
# 方差解释顶部奇异向量
print(f'variance Explained by Top 20 singular values:\n{var_explained[0:20]}')
 
sns.barplot(x=list(range(1, 21)),
            y=var_explained[0:20], color="dodgerblue")
 
plt.title('Variance Explained Graph')
plt.xlabel('Singular Vector', fontsize=16)
plt.ylabel('Variance Explained', fontsize=16)
plt.tight_layout()
plt.show()

# 用不同数量的组件绘制图像
comps = [3648, 10, 20, 30, 50, 100]
plt.figure(figsize=(12, 6))
 
for i in range(len(comps)):
    low_rank = u[:, :comps[i]] @ np.diag(s[:comps[i]]) @ v[:comps[i], :]
     
    if(i == 0):
        plt.subplot(2, 3, i+1),
        plt.imshow(low_rank, cmap='gray'),
        plt.title(f'Actual Image with n_components = {comps[i]}')
     
    else:
        plt.subplot(2, 3, i+1),
        plt.imshow(low_rank, cmap='gray'),
        plt.title(f'n_components = {comps[i]}')