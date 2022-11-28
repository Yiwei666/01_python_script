# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:00:59 2021

@author: sun78
"""

# 绘制cp2k从头算输出的ener文件
#关注一下文件的数据结构特点，尤其是首行数据和第二行数据
#    #   Step   Time [fs]       Ax [Angstrom]       Ay [Angstrom]       Az [Angstrom]       Bx [Angstrom]       By [Angstrom]       Bz [Angstrom]       Cx [Angstrom]       Cy [Angstrom]       Cz [Angstrom]      Volume [Angstrom^3]
#          0       0.000       14.7599000000        0.0000000000        0.0000000000        0.0000000000       14.7599000000        0.0000000000        0.0000000000        0.0000000000       14.7599000000          3215.5128191628
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
from matplotlib.pyplot import MultipleLocator #从pyplot导入MultipleLocator类，这个类用于设置刻度间隔


# 列出当前路径的所有文件名

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)  

print("请输出需要处理的文件名,cell格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

x1 = [] #Step Nr.
x2 = [] #Time[fs]
y1 = [] #Ax [Angstrom]
y2 = [] #By [Angstrom]
y3 = [] #Cz [Angstrom]
y4 = [] #Volume [Angstrom^3]
#y5 = [] #UsedTime[s] 

pp = 0
nn = 0

with open(na, 'r') as f:
    lines = f.readlines()
    for line in lines:
        pp += 1
        if pp == 1:
            title1 = line.split( )[1] #Step Nr.
            title2 = line.split( )[2] #Time[fs]
            title3 = line.split( )[4] #Ax [Angstrom]
            title4 = line.split( )[12] #By [Angstrom]
            title5 = line.split( )[20] #Cz [Angstrom]
            title6 = line.split( )[22] #Volume [Angstrom^3]
            #title7 = line.split( )[9] #UsedTime[s] 
        if pp > 1:
            nn += 1

            p3x1 = float(line.split( )[0])
            p3x2 = float(line.split( )[1])
            
            p3y1 = float(line.split( )[2])
            p3y2 = float(line.split( )[6])
            p3y3 = float(line.split( )[10])
            p3y4 = float(line.split( )[11])
            #p3y5 = float(line.split( )[6])

            x1.append(p3x1)
            x2.append(p3x2)
            y1.append(p3y1)
            y2.append(p3y2)
            y3.append(p3y3)
            y4.append(p3y4)
            #y5.append(p3y5)

# xlim():设置x坐标轴范围
# ylim():设置y坐标轴范围
# xlabel():设置x坐标轴名称
# ylabel():设置y坐标轴名称
# xticks():设置x轴刻度
# yticks():设置y轴刻度


#创建figure窗口，figsize设置窗口的大小
plt.figure(num=3, figsize=(8, 5))

#画曲线1
plt.subplot(411) # 子图绘制，两行一列第一个图     
plt.plot(x1,y1,color='red') #

#x_major_locator=MultipleLocator(1)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator = MultipleLocator(0.1)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
#ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)    


max1 = np.max(y1)     #最大值
min1 = np.min(y1)     #最小值

#设置坐标轴范围
plt.xlim(0, x1[-1])  # x轴范围
plt.ylim(min1,max1) # y轴范围

#设置坐标轴名称
plt.xlabel(title1)  #Step Nr.
plt.ylabel(title3+" [Angstrom]")  #[Angstrom^3]

plt.grid()  #添加网格线


#画曲线2
plt.subplot(412) # 子图绘制，两行一列第一个图     
plt.plot(x1,y2,color='red') #

#x_major_locator=MultipleLocator(1)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator = MultipleLocator(0.1)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
#ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)    


max1 = np.max(y2)     #最大值
min1 = np.min(y2)     #最小值

#设置坐标轴范围
plt.xlim(0, x1[-1])  # x轴范围
plt.ylim(min1,max1) # y轴范围

#设置坐标轴名称
plt.xlabel(title1)  #Step Nr.
plt.ylabel(title4+" [Angstrom]")  #[Angstrom^3]

plt.grid()  #添加网格线



#画曲线3
plt.subplot(413) # 子图绘制，两行一列第一个图     
plt.plot(x1,y3,color='red') #

#x_major_locator=MultipleLocator(1)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator = MultipleLocator(0.1)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
#ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)    


max1 = np.max(y3)     #最大值
min1 = np.min(y3)     #最小值

#设置坐标轴范围
plt.xlim(0, x1[-1])  # x轴范围
plt.ylim(min1,max1) # y轴范围

#设置坐标轴名称
plt.xlabel(title1)  #Step Nr.
plt.ylabel(title5+" [Angstrom]")  #[Angstrom^3]

plt.grid()  #添加网格线



#画曲线4
plt.subplot(414)  
plt.plot(x2,y4,color='blue', linewidth=1.0, linestyle='-') #Pot.[a.u.]

#设置坐标轴范围
plt.xlim(0, x2[-1])  # x轴范围
#mean1 = np.mean(y3)   #平均值
max1 = np.max(y4)     #最大值
min1 = np.min(y4)     #最小值
plt.ylim(min1-100,max1+100)

#设置坐标轴名称
plt.xlabel(title2+" [fs]")  #Time[fs]
plt.ylabel(title6+" [Angstrom^3]")  #Volume [Angstrom^3]

plt.grid()  #添加网格线



plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
print("请问是否要保存图片,输入1保存,输入2不保存:")     # 提示命令行输入
x = int(input())              # 注意字符串输入变量的数据类型转换
if x == 1:
    plt.savefig('time-temp')
    print("图片已保存")

plt.show()


#####################################






######################################

print("需要继续绘制密度曲线请输入1，不需要则输入2")     # 提示命令行输入
ma = int(input())              # 注意字符串输入变量的数据类型转换
if ma == 1:
    print("请输入初始密度")     # 提示命令行输入
    oa = float(input())         # 注意字符串输入变量的数据类型转换
    midu = []
    for y in y4:
        print(y)
        x = float(y4[0]/y*oa)
        midu.append(x)

    #画曲线1
    plt.subplot(211) # 子图绘制，两行一列第一个图     
    plt.plot(x1,y4,color='red') #
    
    max1 = np.max(y4)     #最大值
    min1 = np.min(y4)     #最小值
    
    #设置坐标轴范围
    plt.xlim(0, x1[-1])  # x轴范围
    plt.ylim(min1-100,max1+100) # y轴范围
    
    #设置坐标轴名称
    plt.xlabel(title1)  #Step Nr.
    plt.ylabel(title6+" [Angstrom^3]")  #Volume [Angstrom^3]
    
    plt.grid()  #添加网格线
    
    ##############################
    
    #画曲线2
    plt.subplot(212)  
    plt.plot(x2,midu,color='blue', linewidth=1.0, linestyle='-') #Pot.[a.u.]
    
    #设置坐标轴范围
    plt.xlim(0, x2[-1])  # x轴范围
    #mean1 = np.mean(y3)   #平均值
    
    #x_major_locator=MultipleLocator(1)
    #把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(0.02)
    #把y轴的刻度间隔设置为10，并存在变量里
    ax=plt.gca()
    #ax为两条坐标轴的实例
    #ax.xaxis.set_major_locator(x_major_locator)
    #把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)    
    
    max1 = np.max(midu)     #最大值
    min1 = np.min(midu)     #最小值
    plt.ylim(min1,max1)
    
    #设置坐标轴名称
    plt.xlabel(title2+" [fs]")  #Time[fs]
    plt.ylabel("Density [g/cm3]")  #Volume [Angstrom^3]
    
    plt.grid()  #添加网格线
    
    
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
    print("请问是否要保存图片,输入1保存,输入2不保存:")     # 提示命令行输入
    x = int(input())              # 注意字符串输入变量的数据类型转换
    if x == 1:
        plt.savefig('time-temp')
        print("图片已保存")
    
    plt.show()
        



