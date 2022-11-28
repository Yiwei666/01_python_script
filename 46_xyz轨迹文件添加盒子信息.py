# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:16:23 2022

@author: sun78
"""
# 此代码创建了一个用于解析和修改多帧xyz轨迹文件的类，可以用于添加盒子边长信息等

from numpy import *
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import json
from collections import Counter

class Xyz():
    def __init__(self,name,replace,saveFile):  # 注意是__是双下划线
        '''
        self.name = name              # 需要修改的原xyz文件，需要被分析的xyz文件名字，如 53_V-slag(0-500).xyz 格式
        self.replace = replace        # 添加的晶格参数，字符串，
        self.saveFile = saveFile      # 修改后的xyz文件命名，字符串
        self.xyzList = lines          # 轨迹文件列表实例化,列表,每一行为列表中的一个元素
        self.length = len(lines)      # xyz文件行数，数值
        '''
        self.name = name
        self.replace = replace
        self.saveFile = saveFile
        
        with open(self.name, 'r') as f:
            lines = f.readlines()
            self.xyzList = lines          # 轨迹文件列表实例化
            self.length = len(lines)      # 列表长度

        
    def findRep(self):       # # 该方法返回一个带有晶格参数的新的xyz文件
        '''
        self.frames = len(atomIndex)             # 帧数
        self.atomAmounts = mean(atomNumber)-2    # 每一帧原子数
        self.newLines = newList                  # 添加晶格参数后新xyz的列表
        '''
        newList = []
        atomIndex = []
        print("第二行内容:",self.xyzList[1])
        for i,j in enumerate(self.xyzList):    # enumerate默认从0开始
            if j == self.xyzList[1]:           # 基于xyz文件第二行作为基准来查找替换
                atomIndex.append(i)   # 计算帧数
        # 此处写入晶格参数
            if j != self.xyzList[1]:
                newList.append(j)
            else:
                newList.append(self.replace + "\n")
        atomNumber = [atomIndex[i]-atomIndex[i-1] for i,j in enumerate(atomIndex) if i >=1 ]   # 计算每一帧的行数
        # print (atomNumber)
        self.frames = len(atomIndex)              # 计算帧数
        self.atomAmounts = mean(atomNumber)-2     # 计算每一帧原子数
        self.newLines = newList                   # 添加晶格参数后新的列表
        # 判断计算的原子数是否正确
        if self.atomAmounts != float(self.xyzList[0]):
            print("原子数计算错误！")
        print("帧数",self.frames,"原子数：",self.atomAmounts)
        # print(newList)
        # 该方法返回一个带有晶格参数的新的xyz文件
        with open(self.saveFile,'w') as new_file:
            for i,j in enumerate(newList):
                new_file.write(j)


    def firstFrame(self):
        '''
        self.firstFlame = firFlame       # 第一帧轨迹原子的字典，不包括前两行
        self.eleDict = Counter(firElent) # 每帧中各原子数字典        
        '''
        self.findRep()          # 要访问同个类中的其它方法定义的实例变量，必须先调用该方法.        
        firstFlameList = [j for i,j in enumerate(self.newLines[:(int(self.atomAmounts)+2)])]   # 列表解析获得第一帧的元素列表
        firFlame = {}           # 第一帧轨迹原子的字典，不包括前两行
        firElent = []
        for i,line in enumerate(firstFlameList):
            if i >= 2:
                firFlame[i-1] = line.split( )     # 填充字典
                firElent.append(line.split( )[0]) # 第一帧中各原子化学符号组成的列表
        print(firFlame)
        print(firElent)   #0-223,共224
        print(Counter(firElent))
        self.eleDict = Counter(firElent) # 各原子数字典
        self.firstFlame = firFlame       # 第一帧原子的字典，不包括前两行
        print("总原子数：",self.atomAmounts)
        print(firElent[0],"始于序号：",1)
        for i,j in enumerate(firElent):

            if i <= len(firElent)-2:
                if firElent[i+1] != j:
                    print(j,"结束于:",i+1,"下一个原子",firElent[i+1],"始于序号：",i+2)
        print(firElent[-1],"原子结束于：",self.atomAmounts)

"""
    def atomDict(self):
        self.findRep()          # 要访问同个类中的其它方法定义的实例变量，必须先调用该方法.
        for line in self.newLines:
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
        
"""

def inputFunction():
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
        print("请输出需要处理的xyz轨迹文件名,xyz格式，如 50_SiV(0-500).xyz")     # 提示命令行输入
        txtName = input()              # 注意字符串输入变量的数据类型转换
    return txtName


print("请输出需要添加的晶格信息，如 16.4477 16.4477 16.4477")     # 提示命令行输入
cellInfo = input()              # 注意字符串输入变量的数据类型转换
print("请为添加晶格信息后的xyz文件重新命名，如 1.xyz,该变量仅对findRep()方法作用")     # 提示命令行输入
cellName = input()              # 注意字符串输入变量的数据类型转换
xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)    #  


# xyzFile1 = Xyz('50_SiV(0-500).xyz','16.4477 16.4477 16.4477','1.xyz')
# xyzFile1.findRep()
xyzFile1.firstFrame()
  

"""   
    def xyzList(self):       # 返回xyz轨迹文件列表
        
        

            

"""