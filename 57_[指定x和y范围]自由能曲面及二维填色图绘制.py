# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:56:41 2023

@author: sun78
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# 设置 DPI，图像清晰度
# 通常在 100 到 300 DPI 之间选择一个合适的值即可。如果需要更高的分辨率，可以考虑使用矢量格式的图像，如 PDF、SVG 等，它们不受 DPI 的限制，可以随意缩放而不会失去清晰度。
plt.rcParams['figure.dpi'] = 600


print("""
      请结合具体情况依次修改如下部分代码参数:
          
      data = np.loadtxt('editColvar.txt')
      xmin, xmax =    -5, 36        #  B-Si, -5, 31.5
      ymin, ymax =      -5, 10      #  B-O, -5, 10
      zmin, zmax = -15000, 0        #  筛选z轴数据
      
      offset = -3000                #  填色图在z轴位置
      ax.set_zlim(-3000, 0)         # # 设置z轴坐标范围
      
      ax.set_xlabel('B-Si coordination number')   # x轴标题
      ax.set_ylabel('B-O coordination number')    # y轴标题
      ax.set_zlabel('Energy (kJ/mol)')            # z轴标题
      
      """)

# 加载数据
data = np.loadtxt('editColvar.txt')   # 
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]*4.3597*6.022*100

# 定义x轴和y轴范围
xmin, xmax =    -5, 36        #  B-Si, -5, 31.5
ymin, ymax =      -5, 10      #  B-O, -5, 10
zmin, zmax = -15000, 0
offset = -3500                #  填色图在z轴位置


# 根据指定范围筛选数据
idx = (xmin <= x) & (x <= xmax) & (ymin <= y) & (y <= ymax) & (zmin <= z) & (z <= zmax)
x, y, z = x[idx], y[idx], z[idx]

# 创建3D坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
ax.plot_trisurf(x, y, z, cmap='viridis')

# 添加标签和标题
ax.set_xlabel('Z-axis component')
ax.set_ylabel('Mg-O coordination number')
ax.set_zlabel('Energy (kJ/mol)')
ax.set_title('3-dimension contour and surface plot')

# 设置z轴坐标范围
ax.set_zlim(-3500, 0) 


# 定义网格
xi = np.linspace(min(x), max(x)+0.5, 500)
yi = np.linspace(min(y)-0.5, max(y), 500)
X, Y = np.meshgrid(xi, yi)

# 插值数据到网格上
Z = griddata((x, y), z, (X, Y), method='linear')

# 绘制投影图
contour = ax.contourf(X, Y, Z, cmap='viridis', levels=40, offset=offset)

# 添加colorbar
cbar_ax = fig.add_axes([0.88, 0.10, 0.02, 0.7])
fig.colorbar(contour, cax=cbar_ax)

# 显示图形
plt.show()
