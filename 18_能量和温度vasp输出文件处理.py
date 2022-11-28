# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:23:37 2021

@author: sun78
"""

#主要是用来处理vasp输出的Temperature和Energy文件
#       Time(fs)   Energy(ev)
#       0.000000  296.935000

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd


# 列出当前路径的所有文件名

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)  

print("请输出需要处理的文件名,ener格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

x1 = [] #Time(fs)
y1 = [] #Energy(ev)

pp = 0
nn = 0

with open(na, 'r') as f:
    lines = f.readlines()
    for line in lines:
        pp += 1
        if pp == 1:
            title1 = line.split( )[0] #Time(fs)
            title2 = line.split( )[1] #Time(fs)
 
        if pp > 1:
            nn += 1

            p3x1 = float(line.split( )[0])          
            p3y1 = float(line.split( )[1])

            x1.append(p3x1)
            y1.append(p3y1)


# xlim():设置x坐标轴范围
# ylim():设置y坐标轴范围
# xlabel():设置x坐标轴名称
# ylabel():设置y坐标轴名称
# xticks():设置x轴刻度
# yticks():设置y轴刻度


#创建figure窗口，figsize设置窗口的大小
plt.figure(num=3, figsize=(8, 5))

#画曲线1
plt.subplot(111) # 子图绘制，两行一列第一个图     
plt.plot(x1,y1,color='red') #Temp[K]

max1 = np.max(y1)     #最大值
min1 = np.min(y1)     #最小值

#设置坐标轴范围
plt.xlim(0, x1[-1])  # x轴范围
print ("x轴范围：",x1[0],x1[-1])


if max1-min1 > 100:
    plt.ylim(min1-1000,max1+500) # y轴范围
    print ("y轴范围：min1,max1",min1,max1)
else:
    plt.ylim(min1-1,max1+1)
    print ("y轴范围：min1,max1",min1,max1)


#设置坐标轴名称
plt.xlabel(title1)  #Step Nr.
plt.ylabel(title2)  #Temp[K]



plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)

plt.show()