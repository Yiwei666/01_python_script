# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:39:03 2022

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
    print("请输出需要处理的轨迹文件名,xyz格式（仅包含一帧），如SiMg400.xyz")     # 提示命令行输入
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
        elementCoordinate = []
        pp += 1
        if pp >= 3 :
            # print(line)
            columnNmuber=len(line.split( ))
            elementList.append(line.split( )[0])
            elementTitle = str(pp-2)
            # print(elementTitle)
            elementCoordinate.append(line.split( )[0]+str(pp-2))
            elementCoordinate.append(line.split( )[1])
            elementCoordinate.append(line.split( )[2])
            elementCoordinate.append(line.split( )[3])
            elementCoordinate.append(line.split( )[0])
            elementCoordinate.append(str(pp-2))
            elementDict[elementTitle] = elementCoordinate
         
    countElementList = Counter(elementList)   # 统计各元素的数量
    # print(elementList)   # 各元素列表
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

listTotal = []
for i in range(0,27):
    listName = 'list'+str(i+1)
    listTotal.append(globals()[listName])
#print(len(listTotal),listTotal)
"""
listTotal = [[-1, -1, 1], [0, -1, 1], [1, -1, 1], [-1, 0, 1], [0, 0, 1], [1, 0, 1], [-1, 1, 1], [0, 1, 1], [1, 1, 1], [-1, -1, 0], [0, -1, 0], [1, -1, 0], [-1, 0, 0], [0, 0, 0], [1, 0, 0], [-1, 1, 0], [0, 1, 0], [1, 1, 0], [-1, -1, -1], [0, -1, -1], [1, -1, -1], [-1, 0, -1], [0, 0, -1], [1, 0, -1], [-1, 1, -1], [0, 1, -1], [1, 1, -1]]
"""





print("请输如盒子边长，单位是 Å，默认为正方体盒子，如16.5342")     # 提示命令行输入
cellSize = float(input())            # 注意字符串输入变量的数据类型转换

########################################
# cellSize = 16.5342
########################################
           

boxTotal = {}
for i, document in enumerate(listTotal):
    boxTitle = "boxTitle"+str(i+1)  
    globals()[boxTitle] = {}   
    # boxTitle1, boxTitle2, ...
    for j in range(0,len(elementList)): 
         
        # ['Si224', '4.365199', '10.98372', '1.787596']
        duplicateCoordinate = []
        #title = elementDict[str(j+1)](0)  
        # elementDict = '1': ['Mg1', '0.002209', '7.279744', '5.676796', 'Mg']
        title = elementDict[str(j+1)][0]
        #print(title)
        # document =  [1,1,-1]       
        x = listTotal[i][0]*cellSize + float(elementDict[str(j+1)][1])
        y = listTotal[i][1]*cellSize + float(elementDict[str(j+1)][2])
        z = listTotal[i][2]*cellSize + float(elementDict[str(j+1)][3])
        elementName = elementDict[str(j+1)][4]    
        serialNumber = elementDict[str(j+1)][5] 
        duplicateCoordinate.append(i+1)
        duplicateCoordinate.append(document)
        duplicateCoordinate.append(title)        
        duplicateCoordinate.append(x)
        duplicateCoordinate.append(y)
        duplicateCoordinate.append(z) 
        duplicateCoordinate.append(elementName)
        duplicateCoordinate.append(serialNumber)
        # duplicateCoordinate = [27, [1, 1, -1], 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si', '224']
        print(duplicateCoordinate)
        # print(type(boxTitle))
        globals()[boxTitle][str(j+1)] = duplicateCoordinate
    boxTotal[str(i+1)] = globals()[boxTitle]
# print(boxTotal["27"]["224"][2])

coordinateTotal = [] 
count = 0   
for j in range(0,27):       
    t = str(j+1)
    #print(boxTotal[t])
    for i in range(0,len(elementList)):
        # '224': [27, [1, 1, -1], 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si']}
        # print(boxTotal[t][str(i+1)][2],boxTotal[t][str(i+1)][3],boxTotal[t][str(i+1)][4],boxTotal[t][str(i+1)][5])
        count += 1 
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
print(coordinateTotal)
        # print(coordinateStr)
        #with open("8888.txt", 'a') as new_file:
        #    new_file.write(coordinateStr)
coordinateOriginal = [] 
t = str(14)
#print(boxTotal[t])
for i in range(0,len(elementList)):
    # '224': [27, [1, 1, -1], 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si']}
    # print(boxTotal[t][str(i+1)][2],boxTotal[t][str(i+1)][3],boxTotal[t][str(i+1)][4],boxTotal[t][str(i+1)][5])
    count += 1 
    coordinateStr = str(boxTotal[t][str(i+1)][2])+ ' ' + str(boxTotal[t][str(i+1)][3])+ ' ' + str(boxTotal[t][str(i+1)][4])+ ' ' + str(boxTotal[t][str(i+1)][5])+'\n'
    coordinateList = []
    coordinateList.append(t)
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



print("请输入中心原子种类，如Mg")     # 提示命令行输入
atomCenterName = input()           # 注意字符串输入变量的数据类型转换

#################################
# atomCenterName = "Mg"
#################################

atomCenterList = []
for i, document in enumerate(coordinateOriginal):
    # coordinateOriginal[i] = ['14', 'Si224', 4.365199, 10.98372, 1.787596, 'Si']
    if coordinateOriginal[i][5] == atomCenterName:
        atomCenterList.append(document)
print(atomCenterList)
      
   

print("请输入配位原子种类，如Si，注意不能与中心原子相同")     # 提示命令行输入
atomCoordinateName = input()           # 注意字符串输入变量的数据类型转换

#################################
# atomCoordinateName = "Si"
##################################
atomCoordinateList = []
for i, document in enumerate(coordinateTotal):
    # atomCoordinateList[i] = [27, 'Si224', 20.899399, 27.517919999999997, -14.746603999999998, 'Si', 6048]
    if coordinateTotal[i][5] == atomCoordinateName:
        atomCoordinateList.append(document)
print(atomCoordinateList)

print('***************')



print("请输入截断半径，如2.4, 单位 Å")     # 提示命令行输入
cutoff = float(input())           # 注意字符串输入变量的数据类型转换

#################################
# cutoff = 4
##################################


finalDict = {}
# ['14', 'Mg1', 0.002209, 7.279744, 5.676796, 'Mg', '1']
for i, m in enumerate(atomCenterList):   
    finalList = []
    # [14, 'Si16', 0.465257, 9.42725, 7.053936, 'Si', '16', 2928]
    for j, n in enumerate(atomCoordinateList):
        x0 = m[2]
        y0 = m[3]
        z0 = m[4]
        x1 = n[2]
        y1 = n[3]
        z1 = n[4]
        distance = (x1-x0)*(x1-x0) + (y1-y0)*(y1-y0)  + (z1-z0)*(z1-z0)
        if distance <= (cutoff*cutoff):
            finalList.append(n[6])
            # print (m,n)
            #print (finalList)
    finalDict[m[6]] = finalList
print(finalDict)           

####################################################################
#######################################################################

def calculate_bondOrder(atomDict):
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
    totalDict = {}
    for c in  range(0,len(list(atomDict.keys()))):
        # print(len(list(atomDict.keys())))
        atomCenter = list(atomDict.keys())[c]
        atomCoord = atomDict[atomCenter]
        print("---------------------------------------")
        print(atomCenter,atomCoord)
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    
        centerNumber = atomCenter.split(",")           # 把字符串分开
        # coordNumber = atomCoord.split(",")
        coordNumber = atomCoord
        valueList = []
        value_dict = {}
        for i in centerNumber:
            for j in coordNumber:
                matrixValue = arrayMatrix[int(i)-1][int(j)-1]
                print("已输出每对原子键级：",  matrixValue)           # 显示输入的内容
                valueList.append(matrixValue)
                value_dict[str(i)+":"+str(j)]= matrixValue
        print("中心原子","配位原子",atomCenter,atomCoord)
        #print("matrixValue",matrixValue)
        print("value_dict",value_dict)
        totalDict = dict(**totalDict,**value_dict)
        print("同一个中心原子所有键级",valueList)
        print("平均键级",mean(valueList))       
        
        print("请输入文件保存名字，默认bondOrder.txt")     # 提示命令行输入
        # name = input()              # 注意字符串输入变量的数据类型转换
        name = "bondOrder.txt"
        with open(name, 'a') as new_file:
            new_file.write(json.dumps(value_dict)+'\n')
            new_file.write("bondorder_average: "+str(mean(valueList))+'\n')    
    print(totalDict)
    totalKeysList = list(totalDict.keys())    
    totalValuesList = list(totalDict.values()) 
    print("所有原子对列表：",totalKeysList,"\n")
    print("所有键值列表：", totalValuesList,"\n")
    mean1 = np.mean(totalValuesList)   #平均值
    max1 = np.max(totalValuesList)     #最大值
    min1 = np.min(totalValuesList)     #最小值
    var1 = np.var(totalValuesList)
    std1 = np.std(totalValuesList,ddof=1)
    print("总对数：",len(totalValuesList),"所有平均值: ",mean1, "所有最大值: ", max1,"所有最小值: ", min1,"方差: ",var1,"标准差差: ",std1)    
    for h, docunment in enumerate(totalValuesList):
        print(docunment)
    
    x = datetime.datetime.now()
    with open(name, 'a') as new_file:
        new_file.write("截断半径："+str(cutoff)+'\n')
        new_file.write( "总对数："+ str(len(totalValuesList))+" 所有平均值: "+ str(mean1)+ " 所有最大值: "+ str(max1)+" 所有最小值: "+ str( min1)+" 方差: "+ str(var1)+" 标准差: "+ str(std1)+'\n')
        new_file.write( str(x) +'\n')
        new_file.write("----------------------------------"+'\n')


### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 下面调用计算键级的函数
calculate_bondOrder(finalDict)


"""

    


"""
     
