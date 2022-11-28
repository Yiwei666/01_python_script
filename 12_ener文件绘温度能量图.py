# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:36:03 2021

@author: sun78
"""
# 绘制cp2k从头算输出的ener文件
#关注一下文件的数据结构特点，尤其是首行数据和第二行数据
#       #     Step Nr.          Time[fs]        Kin.[a.u.]          Temp[K]            Pot.[a.u.]        Cons Qty[a.u.]        UsedTime[s]
#              0            0.000000         2.660124888      2500.000000000     -3606.954359876     -3601.634110099         0.000000000
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

x1 = [] #Step Nr.
x2 = [] #Time[fs]
y1 = [] #Kin.[a.u.]
y2 = [] #Temp[K]
y3 = [] #Pot.[a.u.]
y4 = [] #Cons Qty[a.u.]
y5 = [] #UsedTime[s] 

pp = 0
nn = 0

with open(na, 'r') as f:
    lines = f.readlines()
    for line in lines:
        pp += 1
        if pp == 1:
            title1 = line.split( )[1] #Step Nr.
            title2 = line.split( )[3] #Time[fs]
            title3 = line.split( )[4] #Kin.[a.u.]
            title4 = line.split( )[5] #Temp[K]
            title5 = line.split( )[6] #Pot.[a.u.]
            title6 = line.split( )[7] #Cons Qty[a.u.]
            title7 = line.split( )[9] #UsedTime[s] 
        if pp > 1:
            nn += 1

            p3x1 = float(line.split( )[0])
            p3x2 = float(line.split( )[1])
            
            p3y1 = float(line.split( )[2])
            p3y2 = float(line.split( )[3])
            p3y3 = float(line.split( )[4])
            p3y4 = float(line.split( )[5])
            p3y5 = float(line.split( )[6])

            x1.append(p3x1)
            x2.append(p3x2)
            y1.append(p3y1)
            y2.append(p3y2)
            y3.append(p3y3)
            y4.append(p3y4)
            y5.append(p3y5)

# xlim():设置x坐标轴范围
# ylim():设置y坐标轴范围
# xlabel():设置x坐标轴名称
# ylabel():设置y坐标轴名称
# xticks():设置x轴刻度
# yticks():设置y轴刻度


#创建figure窗口，figsize设置窗口的大小
plt.figure(num=3, figsize=(8, 5))

#画曲线1
plt.subplot(211) # 子图绘制，两行一列第一个图     
plt.plot(x1,y2,color='red') #Temp[K]

max1 = np.max(y2)     #最大值
min1 = np.min(y2)     #最小值

#设置坐标轴范围
plt.xlim(0, x1[-1])  # x轴范围
plt.ylim(min1-1000,max1+500) # y轴范围

#设置坐标轴名称
plt.xlabel(title1)  #Step Nr.
plt.ylabel(title4)  #Temp[K]





#画曲线2
plt.subplot(212)  
plt.plot(x2,y3,color='blue', linewidth=1.0, linestyle='-') #Pot.[a.u.]

#设置坐标轴范围
plt.xlim(0, x2[-1])  # x轴范围
#mean1 = np.mean(y3)   #平均值
max1 = np.max(y3)     #最大值
min1 = np.min(y3)     #最小值
plt.ylim(min1-1,max1+1)

#设置坐标轴名称
plt.xlabel(title2)  #Time[fs]
plt.ylabel(title5)  #Temp[K]

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)

print("请问是否要保存图片,输入1保存,输入2不保存:")     # 提示命令行输入
x = int(input())              # 注意字符串输入变量的数据类型转换
if x == 1:
    plt.savefig('time-temp')
    print("图片已保存")

plt.show()








