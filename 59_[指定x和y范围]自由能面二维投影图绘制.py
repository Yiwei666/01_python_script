# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 19:10:20 2023

@author: sun78
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 设置 DPI，图像清晰度
plt.rcParams['figure.dpi'] = 600

print("""
      请结合具体情况依次修改如下部分代码参数:
          
      data = np.loadtxt('editColvar.txt')
      xmin, xmax =    -5, 36        #  B-Si, -5, 31.5
      ymin, ymax =      -5, 10      #  B-O, -5, 10
      zmin, zmax = -15000, 0        #  筛选z轴数据
      
      offset = -3000                #  填色图在z轴位置
      
      ax.set_xlabel('Z-axis component')
      ax.set_ylabel('B-O coordination number')
      
      """)

# 加载数据
data = np.loadtxt('editColvar.txt')
x = data[:, 0]
y = data[:, 1]
z = data[:, 2] * 4.3597 * 6.022 * 100

# 定义x轴和y轴范围
xmin, xmax = -5, 36  #  B-Si, -5, 31.5
ymin, ymax = -5, 10  #  B-O, -5, 10
zmin, zmax = -15000, 0
offset = -3500       #  填色图在z轴位置

# 根据指定范围筛选数据
idx = (xmin <= x) & (x <= xmax) & (ymin <= y) & (y <= ymax) & (zmin <= z) & (z <= zmax)
x, y, z = x[idx], y[idx], z[idx]

# 创建二维平面图
fig, ax = plt.subplots()

# 定义网格
xi = np.linspace(min(x)-0.5, max(x) + 0.5, 500)              # 图的左侧和右侧与y坐标轴的间距均为0.5
yi = np.linspace(min(y)-0.5, max(y)+0.5, 500)                # 图的上侧和下侧与x坐标轴的间距均为0.5
X, Y = np.meshgrid(xi, yi)

# 插值数据到网格上
Z = griddata((x, y), z, (X, Y), method='linear')

# 绘制投影图
contour = ax.contourf(X, Y, Z, cmap='viridis', levels=40)    # 设置色系 cmap='viridis'

# 添加colorbar
cbar = plt.colorbar(contour)

# 添加标签和标题
ax.set_xlabel('Z-axis component')
ax.set_ylabel('B-O coordination number')
# ax.set_title('Projection Plot')


# 显示图形
plt.show()
