# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:26:37 2021

@author: sun78
"""

#将xyz文件中的坐标画为散点图
#先将x,y,z坐标存为浮点型数据列表，然后可直接画图


#import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

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


#string型转float型
#x = [ float( x ) for x in x if x]
#y =[ float( y ) for y in y if y ]
#z =[ float(z ) for z in z if z ]
# 由于使用了float，所以不用转换了

print (x)


fig=plt.figure()
ax=Axes3D(fig)
ax.scatter3D(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()









