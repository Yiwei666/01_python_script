# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:23:37 2021

@author: sun78
"""

#主要是用来处理ISAACS输出的径向分布函数曲线
#从第19行开始是x,y数据
#利用Python获取数组或列表中最大的N个数及其索引


import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import heapq   #利用Python获取数组或列表中最大的N个数及其索引
from matplotlib.pyplot import MultipleLocator #从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
import datetime                      # 导入时间模块


# 列出当前路径的所有文件名

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)  

print("请输入需要处理的文件名,ISAACS导出的g(r)[Si,O]数据文件格式")     # 提示命令行输入
na_g = input()              # 注意字符串输入变量的数据类型转换

x1 = [] #
y1 = [] #

pp1 = 0
nn1 = 0

with open(na_g, 'r') as f:
    lines = f.readlines()
    for line in lines:
        pp1 += 1
#        if pp == 1:
#            title1 = line.split( )[0] #Time(fs)
#            title2 = line.split( )[1] #Time(fs)
 
        if pp1 > 18:
            nn1 += 1

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

plt.title(na_g)  #图表加标题

#画曲线1
plt.subplot(111) # 子图绘制，两行一列第一个图     
plt.plot(x1,y1,color='red') #Temp[K]


x_major_locator=MultipleLocator(1)
#把x轴的刻度间隔设置为1，并存在变量里
#y_major_locator = MultipleLocator(20)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
#ax.yaxis.set_major_locator(y_major_locator) 

max1 = np.max(y1)     #最大值
min1 = np.min(y1)     #最小值

#设置坐标轴范围
plt.xlim(0, x1[-1])  # x轴范围
print ("x轴范围：",x1[0],x1[-1])

#if max1-min1 > 100:
plt.ylim(0,20) # y轴范围
#    print ("y轴范围：min1,max1",min1,max1)
#else:
#    plt.ylim(min1-1,max1+1)
#    print ("y轴范围：min1,max1",min1,max1)

#设置坐标轴名称
plt.xlabel("r")  #r
plt.ylabel("g(r)")  # g(r)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
plt.grid()  #添加网格线
plt.show()

print("第一张图已绘制完毕!")
print("---------------------------------------\n")

##########################################################################################################
#下面这一部分是绘制径向分布函数首个波峰的局部放大图

print("请输入需要放大的x轴坐标范围，用英文逗号间隔 :")     # 提示命令行输入
x_value = input()              # 注意字符串输入变量的数据类型转换
#print("已输入原子编号： ", atom)           # 显示输入的内容
numbers = x_value.split(",")           # 把字符串分开
print("已输入的x轴坐标范围:", numbers)     # 提示命令行输入

#创建figure窗口，figsize设置窗口的大小
plt.figure(num=3, figsize=(8, 5))

plt.title(na_g)  #图表加标题

#画曲线1
plt.subplot(111) # 子图绘制，两行一列第一个图     
plt.plot(x1,y1,'*-.',color='red',linewidth=1) 


x_major_locator=MultipleLocator(0.05)
#把x轴的刻度间隔设置为1，并存在变量里
#y_major_locator = MultipleLocator(20)
#把y轴的刻度间隔设置为10，并存在变量里
ax = plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
#ax.yaxis.set_major_locator(y_major_locator) 

max1 = np.max(y1)     #最大值
min1 = np.min(y1)     #最小值

#设置坐标轴范围
plt.xlim(float(numbers[0]), float(numbers[-1]))  # x轴范围
#plt.xlim(1, 2)  # x轴范围
print ("x轴范围：",numbers[0], numbers[-1])

#if max1-min1 > 100:
plt.ylim(0,20) # y轴范围
#    print ("y轴范围：min1,max1",min1,max1)
#else:
#    plt.ylim(min1-1,max1+1)
#    print ("y轴范围：min1,max1",min1,max1)

#设置坐标轴名称
plt.xlabel("r")  #r
plt.ylabel("g(r)")  #
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
plt.grid()  #添加网格线
plt.show()

print("第二张图已绘制完毕!")
print("---------------------------------------\n")
##########################################################################################################
#下面这一部分是用来计算键长的
#利用Python获取数组或列表中最大的N个数及其索引

print("请输入n值, n代表所要获取列表前n个最大值的")     # 提示命令行输入
nn2 = int(input())              # 注意字符串输入变量的数据类型转换

re1 = heapq.nlargest(nn2, y1) #求列表 p3y1最大的三个元素，并排序
re2 = map(y1.index, heapq.nlargest(nn2, y1)) #求最大的三个索引    nsmallest与nlargest相反，求最小
re2_1 = list(re2) #因为re2由map()生成的不是list，直接print不出来，添加list()就行了
# 注意索引是从0开始的
print("y中最大的前",nn2,"个值从大到小依次是",re1)
print("y中最大的前",nn2,"个值从大到小对应的索引依次是",re2_1)
re3 = []
for i in re2_1:
    fxy = x1[i]
    re3.append(fxy)
print("y中最大的前",nn2,"个值从大到小对应的x依次是",re3)
arr_mean = np.mean(re3)   #求前nn个y值对应的x的平均值
print("y中最大的前",nn2,"个值对应的x的平均值是",arr_mean)

print("第三部分键长计算完毕！")
print("---------------------------------------\n")

##########################################################################################################
#下面是计算径向分布函数第一个波谷对应的截断半径

t1 = re2_1[0]  #最大的y值对应的索引，如148, t1是键长对应的索引
y_list = y1[t1:]
x_list = x1[t1:]

t2 = min(y_list)  #波谷最小值
t3 = y_list.index(min(y_list))   #波谷最小值对应的索引     
t4 = x_list[t3]         #波谷最小值对应的r

print("y的首个波谷值:",t2," 对应的截断半径x值为:",t4)

print("第四部分径向分布函数的截断半径计算完毕！")
print("---------------------------------------\n")

####################################################################################################
#下面这一部分是绘制径向分布函数的首个波谷局部放大图

print("计算g(r)截断半径，请输入x轴坐标范围，用英文逗号间隔 :")     # 提示命令行输入
x_value = input()              # 注意字符串输入变量的数据类型转换
#print("已输入原子编号： ", atom)           # 显示输入的内容
numbers = x_value.split(",")           # 把字符串分开
print("已输入的x轴坐标范围:", numbers)     # 提示命令行输入

#创建figure窗口，figsize设置窗口的大小
plt.figure(num=3, figsize=(8, 5))

plt.title(na_g)  #图表加标题

#画曲线1
plt.subplot(111) # 子图绘制，两行一列第一个图     
plt.plot(x1,y1,'*-.',color='red',linewidth=1) 

plt.text(x = t4,#文本x轴坐标 
         y = t2, #文本y轴坐标
         s="("+str(round(t4,4)) +", "+str(round(t2,4))+")", #文本内容
         )   #数据点添加标注

x_major_locator=MultipleLocator(0.1)
#把x轴的刻度间隔设置为1，并存在变量里
#y_major_locator = MultipleLocator(20)
#把y轴的刻度间隔设置为10，并存在变量里
ax = plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
#ax.yaxis.set_major_locator(y_major_locator) 

max1 = np.max(y1)     #最大值
min1 = np.min(y1)     #最小值

#设置坐标轴范围
plt.xlim(float(numbers[0]), float(numbers[-1]))  # x轴范围
#plt.xlim(1, 2)  # x轴范围
print ("x轴范围：",numbers[0], numbers[-1])

#if max1-min1 > 100:
plt.ylim(0,20) # y轴范围
#    print ("y轴范围：min1,max1",min1,max1)
#else:
#    plt.ylim(min1-1,max1+1)
#    print ("y轴范围：min1,max1",min1,max1)

#设置坐标轴名称
plt.xlabel("r")  #r
plt.ylabel("g(r)")  #
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
plt.grid()  #添加网格线
plt.show()

print("第五部分RDF波谷局部放大图已绘制完毕!")
print("---------------------------------------\n")

############################################################################
#下面这一部分是用来绘制配位数CN曲线的局部放大图
#注意g(r)曲线的横坐标与dn(r)的横坐标值是相同的

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)  

print("下面计算配位数CN，请输入需要处理的文件名,ISAACS导出的 dn(r)[Si,O] 数据文件格式")     # 提示命令行输入
na_cn = input()              # 注意字符串输入变量的数据类型转换

x2 = [] #
y2 = [] #

pp = 0
nn = 0

with open(na_cn, 'r') as f:
    lines = f.readlines()
    for line in lines:
        pp += 1
#        if pp == 1:
#            title1 = line.split( )[0] #Time(fs)
#            title2 = line.split( )[1] #Time(fs)
 
        if pp > 18:
            nn += 1

            p3x2 = float(line.split( )[0])          
            p3y2 = float(line.split( )[1])

            x2.append(p3x2)
            y2.append(p3y2)
            
            
            
            
        
r_index = x2.index(t4)  #t4为首个波谷值对应的r,相对应的索引为r_index
r_CN = y2[r_index]
print("截断半径为:",t4,"对应的配位数为:",r_CN)
        
        
        
        
        
#创建figure窗口，figsize设置窗口的大小
plt.figure(num=3, figsize=(8, 5))


plt.title(na_cn)  #图表加标题

#画曲线1
plt.subplot(111) # 子图绘制，两行一列第一个图     
plt.plot(x2,y2,'*-.',color='m',linewidth=1) 

#round(x,3) #保留浮点数x的小数位为3位

plt.text(x = t4,#文本x轴坐标 
         y = r_CN, #文本y轴坐标
         s="("+str(round(t4,4)) +", "+str(round(r_CN,4))+")", #文本内容
         )   #数据点添加标注

x_major_locator=MultipleLocator(0.5)
#把x轴的刻度间隔设置为1，并存在变量里
#y_major_locator = MultipleLocator(20)
#把y轴的刻度间隔设置为10，并存在变量里
ax = plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
#ax.yaxis.set_major_locator(y_major_locator) 

max1 = np.max(y2)     #最大值
min1 = np.min(y2)     #最小值

#设置坐标轴范围
plt.xlim(0,6)  # x轴范围
#plt.xlim(1, 2)  # x轴范围
#print ("x轴范围：",numbers[0], numbers[-1])

#if max1-min1 > 100:
plt.ylim(0,8) # y轴范围
#    print ("y轴范围：min1,max1",min1,max1)
#else:
#    plt.ylim(min1-1,max1+1)
#    print ("y轴范围：min1,max1",min1,max1)

#设置坐标轴名称
plt.xlabel("r")  #r
plt.ylabel("CN")  #
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
plt.grid()  #添加网格线
plt.show()



print("第六部分配位数CN曲线局部放大图已绘制完毕!")
print("---------------------------------------\n")
print("汇总如下：")
print("RDF中最大的前",nn2,"个值从大到小对应的x依次是",re3)
print("RDF中最大的前",nn2,"个值对应的x的平均值是",arr_mean)
print("截断半径为:",t4,"对应的配位数为:",r_CN)

print("---------------------------------------\n")
print("是否将上述信息保存为文本，是为1，不是为2")
condition = int(input())              # 注意字符串输入变量的数据类型转换
if condition == 1:

#    print("请为输出文件命名,data格式")     # 提示命令行输入
#    name = input()              # 注意字符串输入变量的数据类型转换
    name = na_g+"+"+na_cn+".txt"
    print("默认文件名为：", name)           # 显示输入的内容
    
#    m = open( name, "x")   # 创建新文本
#    m.close()
    

    if not os.path.exists(name):  #如果不存在则创建文件夹
        m = open( name, "x")   # 创建新文本
        m.close()
        
    with open(name, 'a') as new_file:        
        new_file.write(str(datetime.datetime.now())+"\n")  #写入时间
        new_file.write(str(name)+"\n")  #写入文件名
        new_file.write("RDF中最大的前"+str(nn2)+"个值从大到小依次是"+str(re1)+"\n")
        new_file.write("RDF中最大的前"+str(nn2)+"个值从大到小对应的索引依次是"+str(re2_1)+"\n")
        new_file.write("RDF中最大的前"+str(nn2)+"个值从大到小对应的x依次是"+str(re3)+"\n")
        new_file.write("RDF中最大的前"+str(nn2)+"个值对应的x的平均值是"+str(arr_mean)+"\n")
        new_file.write("截断半径为:"+str(t4)+"对应的配位数为:"+str(r_CN)+"\n")
        new_file.write("\n")
        print("信息已保存!")        
print("---------------------------------------\n")
                

