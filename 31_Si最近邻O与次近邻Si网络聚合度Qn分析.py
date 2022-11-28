# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:06:10 2021

@author: sun78
"""

# 以下是分析网络聚合度的脚本，通过在ISAACS的bond properties中输入Si-O和Si-Si的截断半径
# 通过分析Si原子周围O的最近邻配位数以及Si的次近邻配位数来计算Qn
# 当NSi>NO时，Qn为NO;当NSi<=NO时,Qn为NSi。

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

print("请输入需要处理的文件名,ISAACS导出的以Si为中心，O最近邻和Si次近邻配位环境数据txt格式")     # 提示命令行输入
na_g = input()              # 注意字符串输入变量的数据类型转换

with open(na_g, 'r') as p:
    lines = p.readlines()
#    print ("文本内容为：",lines)
    v1 = 0
    for line in lines:
        v1 += 1
        if v1 == 3:  # 第三行
            print (line)
        if v1 == 4:  # 第三行
            print (line)            
        if v1 == 5:  # 第三行
            print (line)        

print("请输入Si原子列的序号,如4,注意不是索引")     # 提示命令行输入
Si = int(input())             # 注意字符串输入变量的数据类型转换

print("请输入O原子列的序号,如2，注意不是索引")     # 提示命令行输入
O = int(input())             # 注意字符串输入变量的数据类型转换

q0 = [] #
q1 = [] #
q2 = [] #
q3 = []
q4 = []
q5 = []
q6 = []
q7 = []
q8 = []



pp = 0
nn = 0

# N(tot)   N(O )   N(F )   N(Si)   N(Ca)          Number   or     Percent
#   6        3       0       3       0           0.37313   or       0.868 %

with open(na_g, 'r') as f:
    lines = f.readlines()
    for line in lines:
        pp += 1
#        if pp == 1:
#            title1 = line.split( )[0] #Time(fs)
#            title2 = line.split( )[1] #Time(fs)
 
        if pp > 3:
            nn += 1

            p3x1 = float(line.split( )[Si-1])          
            p3y1 = float(line.split( )[O-1])
            p3z1 = float(line.split( )[-2])
            if p3x1 > p3y1:  #即Si比O多，即一个氧连多个Si，O原子数小于4是因为形成Si-F键，而F只能连接一个Si
                if p3y1 == 0:
                    q0.append(p3z1)
                if p3y1 == 1:  
                    q1.append(p3z1)
                if p3y1 == 2:
                    q2.append(p3z1)
                if p3y1 == 3:
                    q3.append(p3z1)
                if p3y1 == 4:
                    q4.append(p3z1)
                if p3y1 == 5:
                    q5.append(p3z1)
                if p3y1 == 6:
                    q6.append(p3z1)
                if p3y1 == 7:
                    q7.append(p3z1)
                if p3y1 == 8:
                    q8.append(p3z1)
            if p3x1 <= p3y1: #即O比Si多，通过Si原子数来判断Qn
                if p3x1 == 0:
                    q0.append(p3z1)
                if p3x1 == 1:  
                    q1.append(p3z1)
                if p3x1 == 2:
                    q2.append(p3z1)
                if p3x1 == 3:
                    q3.append(p3z1)
                if p3x1 == 4:
                    q4.append(p3z1)
                if p3x1 == 5:
                    q5.append(p3z1)
                if p3x1 == 6:
                    q6.append(p3z1)
                if p3x1 == 7:
                    q7.append(p3z1)
                if p3x1 == 8:
                    q8.append(p3z1)                

                    
#print("请为输出文件命名,txt格式")     # 提示命令行输入
#name = input()              # 注意字符串输入变量的数据类型转换
#print("已输入文件名 ", name)           # 显示输入的内容
#print("已输入文件名 ", name)           # 显示输入的内容
name = "网络连接度Qn.txt"

with open(name, 'w') as new_file:  # 有则覆盖，没有则创建
    new_file.write(str(datetime.datetime.now())+"\n")  #写入时间
    new_file.write(na_g +"\n")  #写入时间
    new_file.write("q0:"+str(sum(q0))+"\n")
    new_file.write("q1:"+str(sum(q1))+"\n")
    new_file.write("q2:"+str(sum(q2))+"\n")
    new_file.write("q3:"+str(sum(q3))+"\n")
    new_file.write("q4:"+str(sum(q4))+"\n")
    new_file.write("q5:"+str(sum(q5))+"\n")
    new_file.write("q6:"+str(sum(q6))+"\n")
    new_file.write("q7:"+str(sum(q7))+"\n")
    new_file.write("q8:"+str(sum(q8))+"\n")
    new_file.write("总和为:"+str(sum(q0)+sum(q1)+sum(q2)+sum(q3)+sum(q4)+sum(q5)+sum(q6)+sum(q7)+sum(q8))+"\n")
    new_file.write("\n")

print("q0:",sum(q0))
print("q1:",sum(q1))
print("q2:",sum(q2))
print("q3:",sum(q3))
print("q4:",sum(q4))
print("q5:",sum(q5))
print("q6:",sum(q6))
print("q7:",sum(q7))
print("q8:",sum(q8))
print("总和为:",sum(q0)+sum(q1)+sum(q2)+sum(q3)+sum(q4)+sum(q5)+sum(q6)+sum(q7)+sum(q8))

print("计算完毕！")


