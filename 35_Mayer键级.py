# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:51:45 2022

@author: sun78
"""


#将xyz文件中的坐标画为散点图
#先将x,y,z坐标存为浮点型数据列表，然后可直接画图

from numpy import *
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import json

print("默认打开打开当前目录，是否调用GUI获取文件路径?Yes=1,No=2")     # 提示命令行输入
fileOpen = int(input())              # 注意字符串输入变量的数据类型转换
if fileOpen == 1:
    root = tk.Tk()
    root.withdraw()
    f_path = filedialog.askopenfilename()
    txtName = f_path
    print('\n获取的文件地址：', f_path)
else:
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)  
    print("请输出需要处理的文件名,矩阵txt格式")     # 提示命令行输入
    txtName = input()              # 注意字符串输入变量的数据类型转换

# 单个矩阵是atomNumber*5

pp = 0
tt = 0
# 注意前两行不是有效数据
with open(txtName, 'r') as f:
    lines = f.readlines()
    txtLength = len(lines)
    print("文本行数",txtLength )
    for line in lines:
        pp += 1
        if pp > 3 and tt != 1:
            columnNmuber=len(line.split( ))
            if columnNmuber == 5:
                computeAtoms = pp-4
                tt = 1  # 第一次数成功后
                print("第二个矩阵表头",line)
                print ("此时行数为:",pp,"计算原子数为:",computeAtoms)
                lastElement=int(lines[-computeAtoms-1].split( )[-1])
                print("验证原子数为：",lastElement)
                if computeAtoms == lastElement:
                    print("原子数验证成功！")
                else:
                    print("提醒！！！输入与计算原子数不符，验证失败！")

# 创建原子数*原子数多维矩阵
arrayMatrix = np.arange(float(1),float(computeAtoms*computeAtoms+1)).reshape((computeAtoms, computeAtoms))
print("初始矩阵"+"\n",arrayMatrix)
lineCount = 0
valueCount = 0
with open(txtName, 'r') as bondFile:
    bondLines = bondFile.readlines()
    for bondLine in bondLines:
        lineCount += 1
        print("lineCount,bondLine",lineCount,bondLine)
        if lineCount > 3 and (lineCount-3)%(computeAtoms+1) !=0:
            print("bondLine"+"\n",bondLine)
            #for i in range(1,len(bondLine.split( ))):
            #print("i",i)
            atomIndex = bondLine.split( )[0]
            print("atomIndex",atomIndex)               
            titleLineCount = lineCount-int(atomIndex)
            print("titleLineCount",titleLineCount) 
            titleValues = bondLines[titleLineCount-1].split( )
            print("titleValues",titleValues)
            i=0
            for i1 in titleValues:
                print(float(bondLine.split( )[i+1]))
                arrayMatrix[int(atomIndex)-1][int(i1)-1]= float(bondLine.split( )[i+1])                
                i=i+1
print(arrayMatrix)                  

print("请输入想要提取的中心原子编号,从1开始的，用逗号隔开")     # 提示命令行输入
atomCenter = input()              # 注意字符串输入变量的数据类型转换
print("请输入想要提取的配位原子编号")     # 提示命令行输入
atomCoord = input()              # 注意字符串输入变量的数据类型转换

centerNumber = atomCenter.split(",")           # 把字符串分开
coordNumber = atomCoord.split(",")
valueList = []
value_dict = {}
for i in centerNumber:
    for j in coordNumber:
        matrixValue = arrayMatrix[int(i)-1][int(j)-1]
        print("已输出键级：",  matrixValue)           # 显示输入的内容
        valueList.append(matrixValue)
        value_dict[str(i)+":"+str(j)]= matrixValue
print("atomCenter","atomCoord",atomCenter,atomCoord)
#print("matrixValue",matrixValue)
print("value_dict",value_dict)
print("bondorder_average",mean(valueList))

print("请输入文件保存名字，.txt")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
with open(name, 'w') as new_file:
    new_file.write(json.dumps(value_dict))
    new_file.write("bondorder_average:"+str(mean(valueList)))





        
