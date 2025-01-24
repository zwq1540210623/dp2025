import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

print(cv2.__version__)

# opencv 默认是以 BGR通道顺序 打开的
img = cv2.imread("code\python\enpei\dog.jpg")
print(type(img))
print(img.shape)
# print(img)

# BGR-->RGB，在matplotlib显示
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.imshow(img)
# 关闭坐标轴显示
# plt.axis('off')

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# matplotlib 是以 RGB通道顺序 显示的
# plt.imshow(rgb_img)


img_gray = cv2.imread("code\python\enpei\dog.jpg", cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)
# plt.imshow(img_gray)

axes[0].imshow(img)
axes[1].imshow(rgb_img)
axes[2].imshow(img_gray, "gray")


plt.show()

