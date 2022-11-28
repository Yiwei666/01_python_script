# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:58:20 2021

@author: sun78
"""

# 几何中心用x,y,z三个分坐标的平均值或中位数来估算，边长用分坐标的最大值和最小值范围来估算
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd


for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
        
print("---------------")   

print("请输出需要处理的文件名,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换


xc = []
yc = []
zc = []


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
            xc.append(p3x)
            yc.append(p3y)
            zc.append(p3z)

print("共有原子数：",nn)

# x分坐标

max_x = np.max(xc)     #最大值
min_x = np.min(xc)     #最小值
mean_x = np.mean(xc)   #平均值
median_x = np.median(xc)  #中位数

# y分坐标
max_y = np.max(yc)     #最大值
min_y = np.min(yc)     #最小值
mean_y = np.mean(yc)   #平均值
median_y = np.median(yc)  #中位数

# z分坐标

max_z = np.max(zc)     #最大值
min_z = np.min(zc)     #最小值
mean_z = np.mean(zc)   #平均值
median_z = np.median(zc)  #中位数


print("边长x取值范围为：", min_x,"——",max_x)
print("边长y取值范围为：", min_y,"——",max_y)
print("边长z取值范围为：", min_z,"——",max_z)

print("x边长为：",max_x-min_x)
print("y边长为：",max_y-min_y)
print("z边长为：",max_z-min_z)

print("x中位数为：",median_x)
print("y中位数为：",median_y)
print("z中位数为：",median_z)

print("中位数质心为：",round(median_x,4),round(median_y,4),round(median_z,4))
print("平均数质心为：",round(mean_x,4),round(mean_y,4),round(mean_z,4))



