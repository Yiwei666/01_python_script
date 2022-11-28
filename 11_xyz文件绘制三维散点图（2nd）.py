# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:03:51 2021

@author: sun78
"""

#将xyz文件中的坐标画为散点图
#先将x,y,z坐标存为浮点型数据列表，然后可直接画图


#import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d.axes3d import Axes3D

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt  #创建自定义图像


print("请输出需要处理的文件名1,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

x = []
y = []
z = []

pp = 0
nn = 0

with open(na, 'r') as f:
    lines = f.readlines()
    for line in lines:
        pp += 1
        if pp > 2:
            nn += 1
            p3x = float(line.split( )[1]) 
            p3y = float(line.split( )[2])
            p3z = float(line.split( )[3])
            x.append(p3x)
            y.append(p3y)
            z.append(p3z)

#print (x)
#fig=plt.figure()
#ax=Axes3D(fig)
#ax.scatter3D(x,y,z)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#plt.show()


# Creating figure
fig = plt.figure(figsize = (10, 7)) #创建画板, figsize:指定figure的宽和高，单位为英寸；
ax = plt.axes(projection ="3d")
 
# Creating plot
ax.scatter3D(x, y, z, color = "green")
plt.title("simple 3D scatter plot")
 
# show plot
plt.show()