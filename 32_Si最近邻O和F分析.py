# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:19:35 2021

@author: sun78
"""
# 分析Si的最近邻环境需要输入Si-Si，Si-O和Si-F的截断半径
# 其实本脚本完全可以用ISAACS来分析，只输入Si-O和Si-F的截断半径即可，但是本脚本可以计算不同配位数的占比


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

print("请输入需要处理的文件名,ISAACS导出的，以Si为中心，F和O最近邻配位环境数据文件格式")     # 提示命令行输入
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

print("请输入F原子列的序号,如3,注意不是索引")     # 提示命令行输入
F = int(input())             # 注意字符串输入变量的数据类型转换

print("请输入O原子列的序号,如2，注意不是索引")     # 提示命令行输入
O = int(input())             # 注意字符串输入变量的数据类型转换

CN0 = [] #

CN1 = [] #
CN1_0F_1O = [] #
CN1_1F_0O = [] #

CN2 = []
CN2_0F_2O = []
CN2_1F_1O = []
CN2_2F_0O = []

CN3 = []
CN3_0F_3O = []
CN3_1F_2O = []
CN3_2F_1O = []
CN3_3F_0O = []

CN4 = []
CN4_0F_4O = []
CN4_1F_3O = []
CN4_2F_2O = []
CN4_3F_1O = []
CN4_4F_0O = []

CN5 = []
CN5_0F_5O = []
CN5_1F_4O = []
CN5_2F_3O = []
CN5_3F_2O = []
CN5_4F_1O = []
CN5_5F_0O = []

CN6 = []
CN7 = []


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

            p3x1 = float(line.split( )[F-1])          
            p3y1 = float(line.split( )[O-1])
            p3z1 = float(line.split( )[-2])
            t1 = p3x1+p3y1
            
            if t1 == 0:
                CN0.append(p3z1) 
            if t1 == 1:
                CN1.append(p3z1)
                if p3x1 == 0:
                    CN1_0F_1O.append(p3z1)
                if p3x1 == 1:
                    CN1_1F_0O.append(p3z1)
            if t1 == 2:
                CN2.append(p3z1)
                if p3x1 == 0:
                    CN2_0F_2O.append(p3z1)
                if p3x1 == 1:
                    CN2_1F_1O.append(p3z1)                    
                if p3x1 == 2:
                    CN2_2F_0O.append(p3z1)                  
            if t1 == 3:
                CN3.append(p3z1)
                if p3x1 == 0:
                    CN3_0F_3O.append(p3z1)
                if p3x1 == 1:
                    CN3_1F_2O.append(p3z1)
                if p3x1 == 2:
                    CN3_2F_1O.append(p3z1)
                if p3x1 == 3:
                    CN3_3F_0O.append(p3z1)
            if t1 == 4:
                CN4.append(p3z1)
                if p3x1 == 0:
                    CN4_0F_4O.append(p3z1)
                if p3x1 == 1:
                    CN4_1F_3O.append(p3z1)
                if p3x1 == 2:
                    CN4_2F_2O.append(p3z1)
                if p3x1 == 3:
                    CN4_3F_1O.append(p3z1)
                if p3x1 == 4:
                    CN4_4F_0O.append(p3z1)                      
            if t1 == 5:
                CN5.append(p3z1)
                if p3x1 == 0:
                    CN5_0F_5O.append(p3z1)
                if p3x1 == 1:
                    CN5_1F_4O.append(p3z1)
                if p3x1 == 2:
                    CN5_2F_3O.append(p3z1)
                if p3x1 == 3:
                    CN5_3F_2O.append(p3z1)
                if p3x1 == 4:
                    CN5_4F_1O.append(p3z1)
                if p3x1 == 5:
                    CN5_5F_0O.append(p3z1)
            if t1 == 6:
                CN6.append(p3z1)
            if t1 == 7:
                CN7.append(p3z1)
                    
                    
#print("请为输出文件命名,txt格式")     # 提示命令行输入
#name = input()              # 注意字符串输入变量的数据类型转换
#print("已输入文件名 ", name)           # 显示输入的内容
#print("已输入文件名 ", name)           # 显示输入的内容
name = "Si的最近邻配位F与O数量.txt"

with open(name, 'w') as new_file:  # 有则覆盖，没有则创建
    new_file.write(str(datetime.datetime.now())+"\n")  #写入时间
    new_file.write(na_g +"\n")  #写入时间
    new_file.write("CN0:"+str(sum(CN0))+"\n")
    new_file.write("CN1:"+str(sum(CN1))+"\n")
    new_file.write("CN2:"+str(sum(CN2))+"\n")
    new_file.write("CN3:"+str(sum(CN3))+"\n")
    new_file.write("CN4:"+str(sum(CN4))+"\n")
    new_file.write("CN5:"+str(sum(CN5))+"\n")
    new_file.write("CN6:"+str(sum(CN6))+"\n")
    new_file.write("CN7:"+str(sum(CN7))+"\n")
    new_file.write("所有总和为:"+str(sum(CN0)+sum(CN1)+sum(CN2)+sum(CN3)+sum(CN4)+sum(CN5)+sum(CN6)+sum(CN7))+"\n")
    new_file.write("下面是所有二配位的占比:"+"\n")    
    new_file.write("CN2_0F_2O:"+str(sum(CN2_0F_2O))+"\n")    
    new_file.write("CN2_1F_1O:"+str(sum(CN2_1F_1O))+"\n")   
    new_file.write("CN2_2F_0O:"+str(sum(CN2_2F_0O))+"\n") 
    new_file.write("下面是所有三配位的占比:"+"\n")    
    new_file.write("CN3_0F_3O:"+str(sum(CN3_0F_3O))+"\n")    
    new_file.write("CN3_1F_2O:"+str(sum(CN3_1F_2O))+"\n")   
    new_file.write("CN3_2F_1O:"+str(sum(CN3_2F_1O))+"\n")   
    new_file.write("CN3_3F_0O:"+str(sum(CN3_3F_0O))+"\n")   
    new_file.write("下面是所有四配位的占比:"+"\n")       
    new_file.write("CN4_0F_4O:"+str(sum(CN4_0F_4O))+"\n")
    new_file.write("CN4_1F_3O:"+str(sum(CN4_1F_3O))+"\n")
    new_file.write("CN4_2F_2O:"+str(sum(CN4_2F_2O))+"\n")
    new_file.write("CN4_3F_1O:"+str(sum(CN4_3F_1O))+"\n")
    new_file.write("CN4_4F_0O:"+str(sum(CN4_4F_0O))+"\n")
    new_file.write("下面是所有五配位的占比:"+"\n")        
    new_file.write("CN5_0F_5O:"+str(sum(CN5_0F_5O))+"\n")    
    new_file.write("CN5_1F_4O:"+str(sum(CN5_1F_4O))+"\n")     
    new_file.write("CN5_2F_3O:"+str(sum(CN5_2F_3O))+"\n") 
    new_file.write("CN5_3F_2O:"+str(sum(CN5_3F_2O))+"\n") 
    new_file.write("CN5_4F_1O:"+str(sum(CN5_4F_1O))+"\n") 
    new_file.write("CN5_5F_0O:"+str(sum(CN5_5F_0O))+"\n") 

    new_file.write("--------------------------------------\n")    


print("CN0:",sum(CN0))
print("CN1:",sum(CN1))
print("CN2:",sum(CN2))
print("CN3:",sum(CN3))
print("CN4:",sum(CN4))
print("CN5:",sum(CN5))
print("CN6:",sum(CN6))
print("CN7:",sum(CN7))
print("总和为:",sum(CN0)+sum(CN1)+sum(CN2)+sum(CN3)+sum(CN4)+sum(CN5)+sum(CN6)+sum(CN7))
print("CN4_0F_4O:",sum(CN4_0F_4O))
print("CN4_1F_3O:",sum(CN4_1F_3O))
print("CN4_2F_2O:",sum(CN4_2F_2O))
print("CN4_3F_1O:",sum(CN4_3F_1O))
print("CN4_4F_0O:",sum(CN4_4F_0O))
print("配位数为4总和:",sum(CN4_0F_4O)++sum(CN4_1F_3O)+sum(CN4_2F_2O)+sum(CN4_3F_1O)+sum(CN4_4F_0O))

print("计算完毕！更多信息请见输出的Si的最近邻配位F与O数量.txt文件！")






