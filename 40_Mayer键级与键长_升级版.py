# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:01:16 2023

@author: sun78
"""

from collections import Counter   # 统计列表元素个数
from numpy import *
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import json
import datetime


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
    print("请输出需要处理的轨迹文件名,xyz格式（仅包含一帧），应当为电子结构计算用的xyz文件，如SiMg400.xyz")     # 提示命令行输入
    txtName = input()              # 注意字符串输入变量的数据类型转换


########################################
# txtName = "SiMg400.xyz"
########################################
    

pp = 0
tt = 0
elementList = []
elementDict = {}
# 注意前两行不是有效数据
with open(txtName, 'r') as f:
    lines = f.readlines()
    txtLength = len(lines)
    print("文本行数",txtLength, "原子数量",txtLength-2)
    for line in lines:
        elementCoordinate = []                          # 初始化列表，用于储存原子编号，符号，分坐标等
        pp += 1
        if pp >= 3 :
            # print(line)
            columnNmuber=len(line.split( ))             # 列数，一般为4
            elementList.append(line.split( )[0])        # 列表中添加元素符号
            elementTitle = str(pp-2)                    # 原子编号，从1开始计数
            # print(elementTitle)
            elementCoordinate.append(line.split( )[0]+str(pp-2))        # 将元素符号和原子编号结合在一起，如Mg1，在列表中的索引为0
            elementCoordinate.append(line.split( )[1])                  # 原子的x分坐标，列表中的索引为1
            elementCoordinate.append(line.split( )[2])
            elementCoordinate.append(line.split( )[3])
            elementCoordinate.append(line.split( )[0])                  # 元素符号，如Mg，列表中的索引为4
            elementCoordinate.append(str(pp-2))                         # 原子编号，列表中的索引为5
            elementDict[elementTitle] = elementCoordinate               # 构造字典，键为原子编号，值为列表
         
    countElementList = Counter(elementList)   # 统计各元素的数量
    # print(elementList)                      # 各元素列表
    # elementList =  ['Mg', 'Mg', 'Mg', 'Mg', 'Mg', 'Mg', 'Mg', 'Mg', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si']
    print("各类原子数量:",countElementList,"总原子数:",len(elementList)) # 
    # '1': ['Mg1', '0.002209', '7.279744', '5.676796']
    # '1': ['Mg1', '0.002209', '7.279744', '5.676796', 'Mg']
    print(elementDict)

list1 = [-1,-1,1]    # x,y,z
list2 = [0,-1,1]  
list3 = [1,-1,1]  
list4 = [-1,0,1]  
list5 = [0,0,1]  
list6 = [1,0,1]  
list7 = [-1,1,1]  
list8 = [0,1,1]  
list9 = [1,1,1]  

list10 = [-1,-1,0]  
list11 = [0,-1,0]  
list12 = [1,-1,0]  
list13 = [-1,0,0]  
list14 = [0,0,0]  
list15 = [1,0,0]  
list16 = [-1,1,0]  
list17 = [0,1,0]  
list18 = [1,1,0]  

list19 = [-1,-1,-1]  
list20 = [0,-1,-1]  
list21 = [1,-1,-1]  
list22 = [-1,0,-1]  
list23 = [0,0,-1]  
list24 = [1,0,-1]  
list25 = [-1,1,-1]  
list26 = [0,1,-1]  
list27 = [1,1,-1]  

listTotal = []                                   # 初始化一个列表，为了生成数组
for i in range(0,27):
    listName = 'list'+str(i+1)
    listTotal.append(globals()[listName])
#print(len(listTotal),listTotal)
"""
listTotal = [[-1, -1, 1], [0, -1, 1], [1, -1, 1], [-1, 0, 1], [0, 0, 1], [1, 0, 1], [-1, 1, 1], [0, 1, 1], [1, 1, 1], [-1, -1, 0], [0, -1, 0], [1, -1, 0], [-1, 0, 0], [0, 0, 0], [1, 0, 0], [-1, 1, 0], [0, 1, 0], [1, 1, 0], [-1, -1, -1], [0, -1, -1], [1, -1, -1], [-1, 0, -1], [0, 0, -1], [1, 0, -1], [-1, 1, -1], [0, 1, -1], [1, 1, -1]]
"""





print("请输如盒子边长，单位是 Å，默认为正方体盒子，如16.5342，只需要输入一个浮点数即可")     # 提示命令行输入
cellSize = float(input())            # 注意字符串输入变量的数据类型转换

########################################
# cellSize = 16.5342
########################################
           

boxTotal = {}
for i, document in enumerate(listTotal):    # 遍历周期变换列表
    boxTitle = "boxTitle"+str(i+1)         
    globals()[boxTitle] = {}                # 动态地创建一个以boxTitle变量中字符串表示的名称为键的字典。globals()函数返回全局符号字典（全局变量表），然后将这个新字典赋值给动态生成的名称。换句话说，代码为每次迭代创建一个带有唯一名称的字典。
    # boxTitle1, boxTitle2, ...
    for j in range(0,len(elementList)):     # 遍历所有原子索引
         
        # ['Si224', '4.365199', '10.98372', '1.787596']
        duplicateCoordinate = []                                             # 储存了每一个原子变换前后的相关信息
        #title = elementDict[str(j+1)](0)  
        # elementDict = '1': ['Mg1', '0.002209', '7.279744', '5.676796', 'Mg']
        title = elementDict[str(j+1)][0]      # 获取元素符号＋编号，如Mg1
        #print(title)
        # document =  [1,1,-1]       
        x = listTotal[i][0]*cellSize + float(elementDict[str(j+1)][1])       # 周期变换后的x分坐标
        y = listTotal[i][1]*cellSize + float(elementDict[str(j+1)][2])       # 周期变换后的y分坐标
        z = listTotal[i][2]*cellSize + float(elementDict[str(j+1)][3])       # 周期变换后的z分坐标
        elementName = elementDict[str(j+1)][4]                               # 元素符号
        serialNumber = elementDict[str(j+1)][5]                              # 原子编号
        duplicateCoordinate.append(i+1)                                      # 周期变换的序号，1~27
        duplicateCoordinate.append(document)                                 # 周期变换的位置，如[1, 1, -1]
        duplicateCoordinate.append(title)                                    # Mg1
        duplicateCoordinate.append(x)
        duplicateCoordinate.append(y)
        duplicateCoordinate.append(z) 
        duplicateCoordinate.append(elementName)
        duplicateCoordinate.append(serialNumber)
        # duplicateCoordinate = [27, [1, 1, -1], 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si', '224']
        print(duplicateCoordinate)
        # print(type(boxTitle))
        globals()[boxTitle][str(j+1)] = duplicateCoordinate                  # boxTitle1,  boxTitle2,  ..., boxTitle27, 每一个字典中都存储了相应周期盒子变换后的原子信息
    boxTotal[str(i+1)] = globals()[boxTitle]
# print(boxTotal["27"]["224"][2])                                            # 存储了27个周期变换后盒子中的原子信息

coordinateTotal = [] 
count = 0   
for j in range(0,27):       
    t = str(j+1)
    #print(boxTotal[t])
    for i in range(0,len(elementList)):
        # '224': [27, [1, 1, -1], 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si']}
        # print(boxTotal[t][str(i+1)][2],boxTotal[t][str(i+1)][3],boxTotal[t][str(i+1)][4],boxTotal[t][str(i+1)][5])
        count += 1                  # 用于计数，计算变换后的所有原子数
        coordinateStr = str(boxTotal[t][str(i+1)][2])+ ' ' + str(boxTotal[t][str(i+1)][3])+ ' ' + str(boxTotal[t][str(i+1)][4])+ ' ' + str(boxTotal[t][str(i+1)][5])+'\n'
        coordinateList = []
        coordinateList.append(j+1)
        coordinateList.append(boxTotal[t][str(i+1)][2])
        coordinateList.append(boxTotal[t][str(i+1)][3])
        coordinateList.append(boxTotal[t][str(i+1)][4])
        coordinateList.append(boxTotal[t][str(i+1)][5])
        coordinateList.append(boxTotal[t][str(i+1)][6])
        coordinateList.append(boxTotal[t][str(i+1)][7])
        coordinateList.append(count)
        coordinateTotal.append(coordinateList)
# coordinateTotal[6048] = [27, 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si', 6048]]
print(coordinateTotal)            # 这是一个超级列表，包含了变换后的所有原子信息
        # print(coordinateStr)
        #with open("8888.txt", 'a') as new_file:
        #    new_file.write(coordinateStr)
        
        
coordinateOriginal = []   # 注意该列表储存初始原子的相关信息
t = str(14)               # 注意：t = "14"的含义，list14 = [0,0,0]，即原始原子坐标，未经变换的
#print(boxTotal[t])
for i in range(0,len(elementList)):
    # '224': [27, [1, 1, -1], 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si']}
    # print(boxTotal[t][str(i+1)][2],boxTotal[t][str(i+1)][3],boxTotal[t][str(i+1)][4],boxTotal[t][str(i+1)][5])
    count += 1 
    coordinateStr = str(boxTotal[t][str(i+1)][2])+ ' ' + str(boxTotal[t][str(i+1)][3])+ ' ' + str(boxTotal[t][str(i+1)][4])+ ' ' + str(boxTotal[t][str(i+1)][5])+'\n'
    coordinateList = []
    coordinateList.append(t)                             # 注意 索引为 0，即 
    coordinateList.append(boxTotal[t][str(i+1)][2])
    coordinateList.append(boxTotal[t][str(i+1)][3])
    coordinateList.append(boxTotal[t][str(i+1)][4])
    coordinateList.append(boxTotal[t][str(i+1)][5])
    coordinateList.append(boxTotal[t][str(i+1)][6])
    coordinateList.append(boxTotal[t][str(i+1)][7])
    # coordinateList.append(count)
    coordinateOriginal.append(coordinateList)
print(coordinateOriginal)
# print(boxTotal["27"]["224"])



print("请输入中心原子种类，如Mg")      # 提示命令行输入
atomCenterName = input()           # 注意字符串输入变量的数据类型转换

#################################
# atomCenterName = "Mg"
#################################

atomCenterList = []                                   # 存储原始盒子中心原子的相关信息
for i, document in enumerate(coordinateOriginal):     # 遍历未经变换的原子列表，找到所有中心原子
    # coordinateOriginal[i] = ['14', 'Si224', 4.365199, 10.98372, 1.787596, 'Si']
    if coordinateOriginal[i][5] == atomCenterName:
        atomCenterList.append(document)
print(atomCenterList)
      


print("请输入配位原子种类，如Si，注意不能与中心原子相同")     # 提示命令行输入
atomCoordinateName = input()                           # 注意字符串输入变量的数据类型转换

#################################
# atomCoordinateName = "Si"
##################################
atomCoordinateList = []
for i, document in enumerate(coordinateTotal):         # 遍历变换后的所有盒子，包括中心盒子
    # atomCoordinateList[i] = [27, 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si', 6048]
    if coordinateTotal[i][5] == atomCoordinateName:
        atomCoordinateList.append(document)
print(atomCoordinateList)                              # 存储配位原子信息的列表

print('***************')



print("请输入截断半径，如2.4, 单位 Å")                    # 提示命令行输入
cutoff = float(input())                                # 注意字符串输入变量的数据类型转换

#################################
# cutoff = 4
##################################


finalDict = {}                                         # 初始化一个字典，用于储存每一个中心原子特定截断半径下，特定种类的配位原子编号
distanceDict = {}                                      # 初始化一个字典，用于储存所有中心原子及其配位原子的距离，最后将基于该字典打印所有原子对的原子间距

# ['14', 'Mg1', 0.002209, 7.279744, 5.676796, 'Mg', '1']
for i, m in enumerate(atomCenterList):                # 遍历每一个中心原子
    finalList = []
    # [14, 'Si16', 0.465257, 9.42725, 7.053936, 'Si', '16', 2928]
    for j, n in enumerate(atomCoordinateList):        # 遍历每一个配位原子
        x0 = m[2]       # 中心原子的x坐标
        y0 = m[3]       # 中心原子的y坐标
        z0 = m[4]       # 中心原子的x坐标
        x1 = n[2]       # 配位原子的x坐标
        y1 = n[3]       # 配位原子的y坐标
        z1 = n[4]       # 配位原子的z坐标
        distance = (x1-x0)*(x1-x0) + (y1-y0)*(y1-y0)  + (z1-z0)*(z1-z0)    # 计算中心原子和配位原子间距离的平方，此处已经开始计算距离了
        if distance <= (cutoff*cutoff):
            finalList.append(n[6])                     # 满足要求，则记录相应配位原子编号
            sqrt_distance = np.sqrt(distance)          # 计算原子间距，开平方根
            distanceDict[m[6]+':'+n[6]] = sqrt_distance    # 将中心原子和配位原子的间距存储到字典中，m是中心原子列表，n是配位原子列表
            # print (m,n)
            #print (finalList)
    finalDict[m[6]] = finalList                        # 针对每一个中心原子的配位原子列表信息，由于都是配位原子，所以不包含原子本身；键是原子编号，值是配位原子列表信息

print(finalDict)                                       # 储存每一个中心原子及其所有配位原子的字典，该数据非常重要，键是中心原子，值是配位原子列表

####################################################################
#######################################################################

# 定义 calculate_bondOrder()函数，atomDict形参是每个中心原子及其配位原子的字典 ，具有3方面功能
# 1. 基于bndmat.txt中的数据结构，自恰验证原子数
# 2. 将所有键级数据存储到 arrayMatrix 数组中
# 3. 计算中心原子及其配位原子的键级数据


def calculate_bondOrder(atomDict, atom_pair):
    
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
        print("请输出需要处理的文件名,键级矩阵txt格式，提示！一般为为bndmat.txt")     # 提示命令行输入
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
                    computeAtoms = pp-4                                         # 计算体系中可能的原子数
                    tt = 1  # 第一次数成功后                                      # tt为1之后，后续便不再进入该循环
                    print("第二个矩阵表头",line)
                    print ("此时行数为:",pp,"计算原子数为:",computeAtoms)
                    lastElement=int(lines[-computeAtoms-1].split( )[-1])        # 基于上述原子数计算最后一个矩阵表头的最后一个原子编号
                    print("验证原子数为：",lastElement)
                    if computeAtoms == lastElement:
                        print("原子数验证成功！")                                 # 查看二者计算出来的原子数是否一致
                    else:
                        print("提醒！！！输入与计算原子数不符，验证失败！")
    
    # 创建原子数*原子数多维矩阵
    # 使用NumPy库创建一个computeAtoms行 computeAtoms列的二维数组（矩阵），矩阵中的元素从1开始，每个元素增加1，直到computeAtoms*computeAtoms为止。
    
    arrayMatrix = np.arange(float(1),float(computeAtoms*computeAtoms+1)).reshape((computeAtoms, computeAtoms))
    print("初始矩阵"+"\n",arrayMatrix)
    lineCount = 0
    valueCount = 0
    with open(txtName, 'r') as bondFile:
        bondLines = bondFile.readlines()
        for bondLine in bondLines:              # 遍历bndmat.txt键级数据文件的每一行
            lineCount += 1                      # 对遍历的所有行进行计数，从1开始
            print("lineCount,bondLine",lineCount,bondLine)
            if lineCount > 3 and (lineCount-3)%(computeAtoms+1) !=0:            # 筛选出不是表头的行
                print("bondLine"+"\n",bondLine)
                #for i in range(1,len(bondLine.split( ))):
                #print("i",i)
                atomIndex = bondLine.split( )[0]                                # 获取所有非表头行的第一个元素，即原子编号，如1，2，3 ...
                print("atomIndex",atomIndex)               
                titleLineCount = lineCount-int(atomIndex)                       # 计算当前矩阵对应表头所在行
                print("titleLineCount",titleLineCount) 
                titleValues = bondLines[titleLineCount-1].split( )              # 获取表头所在行的所有原子编号
                print("titleValues",titleValues)
                i=0
                for i1 in titleValues:
                    print(float(bondLine.split( )[i+1]))                        # 计算当前矩阵所有非表头行的数据
                    arrayMatrix[int(atomIndex)-1][int(i1)-1]= float(bondLine.split( )[i+1])    # 将每一行的键级数据写进二维数组中            
                    i=i+1
    print(arrayMatrix)                          # 打印二维数组  
    
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    """
    print("请输入想要提取的中心原子编号,从1开始的，用逗号隔开")     # 提示命令行输入
    atomCenter = input()              # 注意字符串输入变量的数据类型转换
    print("请输入想要提取的配位原子编号")     # 提示命令行输入
    atomCoord = input()              # 注意字符串输入变量的数据类型转换
    """
    # atomDict =  {'1': ['86', '146', '149', '161', '16', '23', '28', '48', '129', '158'], '2': ['35', '41', '43', '53', '68', '70', '82', '124', '125', '169', '177', '185', '218'], '3': ['21', '34', '37', '77', '105', '110', '124', '150', '156', '90', '188', '203'], '4': ['16', '23', '48', '75', '88', '93', '113', '129', '142', '171', '206', '214', '215'], '5': ['22', '80', '82', '119', '125', '132', '172', '192', '196', '199', '209', '210'], '6': ['34', '89', '124', '150', '156', '172', '199', '205', '209', '218'], '7': ['109', '161', '28', '48', '57', '88', '98', '104', '107', '152', '158', '168', '176', '202'], '8': ['31', '201', '83', '117', '152', '176', '58', '116', '179', '97', '203']}
    totalDict = {}                                    # 初始化一个字典，用于储存所有中心原子及其配位原子的键级数据
    for c in  range(0,len(list(atomDict.keys()))):    # 遍历所有中心原子，注意atomDict是一个形参字典
        # print(len(list(atomDict.keys())))
        atomCenter = list(atomDict.keys())[c]         # 获取每一个中心原子的编号
        atomCoord = atomDict[atomCenter]              # 获取对应的配位原子列表
        print("---------------------------------------")
        print(atomCenter,atomCoord)                   # 打印中心原子及其配位原子
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    
        # centerNumber = atomCenter.split(",")           # 把字符串分开
        # coordNumber = atomCoord.split(",")
        coordNumber = atomCoord               # 配位原子列表
        valueList = []                        # 储存键级数据
        value_dict = {}
        # for i in centerNumber:
            
        i = atomCenter                        # 针对外循环中的每一个中心原子
        for j in coordNumber:
            matrixValue = arrayMatrix[int(i)-1][int(j)-1]
            print("已输出每对原子键级：",  matrixValue)           # 显示输入的内容
            valueList.append(matrixValue)
            value_dict[str(i)+":"+str(j)]= matrixValue         # 键的格式为 "P:Si"
        print("中心原子","配位原子",atomCenter,atomCoord)
        #print("matrixValue",matrixValue)
        print("value_dict",value_dict)                             # 存有一个中心原子及相应原子对所有键级数据
        totalDict = dict(**totalDict,**value_dict)                 # 汇总到包含有所有中心原子键级数据的字典中
        print("同一个中心原子所有键级",valueList)
        print("平均键级",mean(valueList))                           # 计算同一个中心原子的键级 
        
        print("请输入文件保存名字，默认bondOrder.txt")                # 提示命令行输入
        # name = input()                                           # 注意字符串输入变量的数据类型转换
        name = "bondOrder.txt"                                     # 将计算出来的键级数据默认保存到 bondOrder.txt 文件中
        # 写入每一个中心原子及其配位原子的键级数据
        with open(name, 'a') as new_file:
            new_file.write(json.dumps(value_dict)+'\n')            # value_dict是一个中心原子的键级字典，如：{"184:18": 1.62418862, "184:52": 1.17449284, "184:99": 1.25638453, "184:102": 1.39759876}
            new_file.write("bondorder_average: "+str(mean(valueList))+'\n')      # 写入平均值
            
    print(totalDict)                                              # 存有所有原子对键级数据的字典
    totalKeysList = list(totalDict.keys())                        # 列表中是所有的原子对
    totalValuesList = list(totalDict.values())                    # 计算所有的键级数据
    print("所有原子对列表：",totalKeysList,"\n")
    print("所有键值列表：", totalValuesList,"\n")
    mean1 = np.mean(totalValuesList)                              # 平均值
    max1 = np.max(totalValuesList)                                # 最大值
    min1 = np.min(totalValuesList)                                # 最小值
    var1 = np.var(totalValuesList)
    std1 = np.std(totalValuesList,ddof=1)
    print("总对数：",len(totalValuesList),"所有平均值: ",mean1, "所有最大值: ", max1,"所有最小值: ", min1,"方差: ",var1,"标准差差: ",std1)    
    for h, docunment in enumerate(totalValuesList):
        print(docunment)                                          # 打印出所有的键级数据
    
    str_keyBndLen = 'atomPair  bondLength  bondOrder \n'                 # 初始化一个空字符串，用于储存key，键长和键级
    for key in totalDict.keys():
        print(key, round(distanceDict[key],3), round(totalDict[key],3))            # 打印所有原子对及其对应的间距和键级数据
        str_keyBndLen = str_keyBndLen + key + '  ' + str(round(distanceDict[key],3)) + '  '  + str(round(totalDict[key],3)) + '\n'
        
    # 将汇总的计算数据写入到 txt文件中
    x = datetime.datetime.now()
    with open(name, 'a') as new_file:
        new_file.write("截断半径："+str(cutoff)+'\n')
        new_file.write( "总对数："+ str(len(totalValuesList))+" 所有平均值: "+ str(mean1)+ " 所有最大值: "+ str(max1)+" 所有最小值: "+ str( min1)+" 方差: "+ str(var1)+" 标准差: "+ str(std1)+'\n')
        new_file.write( str(x) +'\n')
        new_file.write( str_keyBndLen )                          # 将原子对，键长，键级等数据写入到txt文件中
        new_file.write( atom_pair + '\n' )
        new_file.write("----------------------------------"+'\n')


### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 下面调用计算键级的函数
atom_pair = atomCenterName + '-' + atomCoordinateName           # 构建原子对，如P-O

calculate_bondOrder(finalDict, atom_pair)                 # 调用函数计算键级，并将相关信息写入到txt文件中



     