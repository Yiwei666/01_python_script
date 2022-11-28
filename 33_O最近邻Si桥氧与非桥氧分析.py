# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:39:08 2021

@author: sun78
"""

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

print("请输入需要处理的文件名,ISAACS导出的，以O为中心Si最近邻配位环境数据文件格式, En开头的")     # 提示命令行输入
na_g = input()              # 注意字符串输入变量的数据类型转换

with open(na_g, 'r') as p:
    lines = p.readlines()
#    print ("文本内容为：",lines)
    v1 = 0
    for line in lines:
        v1 += 1
        if v1 == 3:  # 第三行
            print (line)
        if v1 == 4:  # 第四行
            print (line)            
        if v1 == 5:  # 第五行
            print (line)        

print("请输入Si原子列的序号,如4,注意不是索引")     # 提示命令行输入
Si = int(input())             # 注意字符串输入变量的数据类型转换
           # 注意字符串输入变量的数据类型转换

q0 = [] # 自由氧
q1 = [] # 非桥氧
q2 = [] # 桥氧
q3 = [] # 三键氧
q4 = [] # 误差


pp = 0
nn = 0

#N(tot)   N(O )   N(F )   N(Si)   N(Ca)          Number   or     Percent
#  1        0       0       1       0          72.55224   or      54.964 %

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
            p3z1 = float(line.split( )[-2])    # 百分占比
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
                
                
name = "O的种类统计.txt"

with open(name, 'w') as new_file:  # 有则覆盖，没有则创建
    new_file.write(str(datetime.datetime.now())+"\n")  #写入时间
    new_file.write(na_g +"\n")  #写入时间
    new_file.write("FO:"+str(sum(q0))+"\n")
    new_file.write("NBO:"+str(sum(q1))+"\n")
    new_file.write("BO:"+str(sum(q2))+"\n")
    new_file.write("TO:"+str(sum(q3))+"\n")
    new_file.write("QO:"+str(sum(q4))+"\n")
    new_file.write("总和为:"+str(sum(q0)+sum(q1)+sum(q2)+sum(q3)+sum(q4))+"\n")
    new_file.write("\n")

print("FO:",sum(q0))
print("NBO:",sum(q1))
print("BO:",sum(q2))
print("TO:",sum(q3))
print("QO:",sum(q4))

print("总和为:",sum(q0)+sum(q1)+sum(q2)+sum(q3)+sum(q4))

print("计算完毕！")                
                



                
                    
                    