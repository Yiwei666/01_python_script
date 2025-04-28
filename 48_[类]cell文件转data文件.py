# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:39:34 2022

@author: sun78
"""

import datetime
from numpy import *
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import json
from collections import Counter
import sys
import math


timeStart = datetime.datetime.now()          # 显示时间

class cellConventer():
    def __init__(self,cellName,saveFile):
        self.cellName = cellName
        self.saveFile = saveFile
        '''
        self.lines = lines                          # 轨迹文件列表实例化，即所有行写成一个列表        
        self.txtLength = txtLength                  # 文本行数
        
        self.cellLength = lines[1].split( )[0]
        self.cellWidth  = lines[2].split( )[1]
        self.cellHeight = lines[3].split( )[2]
        
        self.Xa = float(lines[1].split( )[0])       # 后面计算笛卡尔坐标时用到了
        self.Ya = float(lines[1].split( )[1])
        self.Za = float(lines[1].split( )[2])
        self.Xb = float(lines[2].split( )[0])
        self.Yb = float(lines[2].split( )[1])
        self.Zb = float(lines[2].split( )[2])
        self.Xc = float(lines[3].split( )[0])
        self.Yc = float(lines[3].split( )[1])
        self.Zc = float(lines[3].split( )[2])    

        self.endingLineIndex = iIndex-1              # 最后一行原子坐标的index
        self.atomNumber = iIndex-6-1                 # 利用索引计算原子数
        self.startIndex = startIndex                 # 相对原子质量开始的index
        self.endIndex = endIndex                     # 设置全局变量，相对原子质量结束的index
        
        self.atomKinds = self.endIndex-self.startIndex+1            # 利用相对原子质量所在行的索引来计算原子种类数
        self.atomKindDict = atomKindDict                            # 将得到的字典设置为全局变量

        self.atomList  = atomList                   # 存储元素化学符号的列表
        self.atomLines = atomLines                  # 存储笛卡尔坐标的列表，该列表包含了多个原子的坐标
        self.atomDict  = atomDict                   # 这个字典存储了所有原子的化学符号和笛卡尔坐标，以列表的形式，键是原子序号，值是原子符号和坐标的列表

        '''

        with open(self.cellName, 'r') as f:
            lines = f.readlines()
            txtLength = len(lines)                      # 由于最后两行是空行，txtLength比实际值大1，也就是还计算了一个空行
            self.lines = lines                          # 轨迹文件列表实例化，即所有行写成一个列表        
            self.txtLength = txtLength                  # 文本行数, 这个行数包含了1个空行，实际文本最后两行是空行，读取的时候去除了1个空行

            self.cellLength = lines[1].split( )[0]      # cell文件的2-4行是晶格参数在x，y，z方向的分坐标，对应行数的索引为1-3。注意这是字符串
            self.cellWidth  = lines[2].split( )[1]
            self.cellHeight = lines[3].split( )[2]
            # A(Xa, Ya, Za)
            # B(Xb, Yb, Zb)
            # C(Xc, Yc, Zc)
            self.Xa = float(lines[1].split( )[0])       # 计算每一个晶格参数的x,y,z的分坐标。
            self.Ya = float(lines[1].split( )[1])       # 后面计算笛卡尔坐标时用到了
            self.Za = float(lines[1].split( )[2])
            self.Xb = float(lines[2].split( )[0])
            self.Yb = float(lines[2].split( )[1])
            self.Zb = float(lines[2].split( )[2])
            self.Xc = float(lines[3].split( )[0])
            self.Yc = float(lines[3].split( )[1])
            self.Zc = float(lines[3].split( )[2])
                                

            '''
            下面主要是为了计算原子坐标的起始行和终止行的索引，以及原子数
            '''
            iIndex = 6                              # "%BLOCK POSITIONS_FRAC"，6 是坐标起始标志的索引，索引为6对应的行数为7.
            while iIndex < txtLength-1 :            # 文本最后有2个空行，倒数第2个空行的行数为txtLength，对应的索引为txtLength-1。由于是 < 号，该while筛选不到倒数第2个空行
                if not len(lines[iIndex].strip()):  # if not 判断是否为NONE，len(line.strip())为0，len()统计的字符串的长度.'\n'也占用一个字符长度
                    print('空行索引index',iIndex)
                else:                               # 筛选非空行，且所有非空行都至少有两个字符串
                    # Ending line is "%ENDBLOCK POSITIONS_FRAC"
                    if lines[iIndex].split( )[0]== "%ENDBLOCK" and lines[iIndex].split( )[1] == "POSITIONS_FRAC":  # 查找结束行标志的索引
                        print("原子坐标起始、结束行的index分别为：",7,iIndex-1,"\n","原子坐标开始和结束标志分别为：\n",lines[6],lines[iIndex])
                        self.endingLineIndex = iIndex-1              # 最后一行原子坐标的index
                        self.atomNumber = iIndex-6-1                 # 利用索引计算原子数
                        print("体系原子数：",self.atomNumber)

                    if lines[iIndex].split( )[0]== "%BLOCK" and lines[iIndex].split( )[1] == "SPECIES_MASS":   # 查找相对原子质量所在的index
                        startIndex = iIndex+1                           # 加上1是因为此时的iIndex仅仅是标志的索引
                        self.startIndex = startIndex                    # 相对原子质量开始的index
                    if lines[iIndex].split( )[0]== "%ENDBLOCK" and lines[iIndex].split( )[1] == "SPECIES_MASS":
                        endIndex = iIndex-1                             # 相对原子质量结束的index，注意此时不是标志的index
                        self.endIndex = endIndex                        # 设置全局变量，相对原子质量结束的index
                        break                                           # 最后一个条件满足之后就可以跳出循环了
                iIndex += 1

            '''
            下面主要是获取每种原子的相对原子质量，字典的形式
            '''
            self.atomKinds = self.endIndex-self.startIndex+1            # 利用相对原子质量所在行的索引来计算原子种类数
            atomKindDict = {}                                           # 初始化字典，用于储存原子的相对原子质量，键是元素符号，值是相对原子质量
            for i,j in enumerate(lines[self.startIndex:self.endIndex+1]):       # 切片包含前面，不包含后面，
                elementFormula = j.split( )[0]                          #       Si     28.0849990845  ，元素符号
                elementMass = j.split( )[1]                             # 相对原子质量
                atomKindDict[elementFormula] = elementMass              # 键-值对写入字典
            self.atomKindDict = atomKindDict                            # 将得到的字典设置为全局变量
            # self.atomKindDict = {'Si': '28.0849990845', 'V': '50.9410018921'}
            print('----------各原子类型及相对原子质量----------：',self.atomKindDict)
            
            '''
            下面主要是为了将分数坐标转换为笛卡尔坐标，并写入到字典中
            '''
            atomList = []       # 用来储存每一个原子的化学符号
            atomLines = []      # 用来存储转换后的笛卡尔坐标, 列表中的每一个元素都是一个原子的化学符号和xyz坐标，可以直接将该元素列表写成xyz轨迹文件
            atomIndex = 7       # 原子坐标起始的index
            atomDict = {}       # 初始化字典，用于存储笛卡尔坐标，字典的键是序号，从1开始
            while atomIndex <= self.endingLineIndex:  #  最后一行原子坐标的index
                tempList = []                         # 构造临时列表，储存元素符号和原子坐标，用于字典的值，包括元素符号和xyz的各分坐标
                lineFirstElement = lines[atomIndex].split( )[0]        # 获取原子坐标所在行的元素符号
                atomList.append(lineFirstElement)     # 列表添加元素符号
                # Xcar=Xa*x+Xb*y+Xc*z
                # Ycar=Ya*x+Yb*y+Yc*z
                # Zcar=Za*x+Zb*y+Zc*z            
                xCoordinate = float(lines[atomIndex].split( )[1])      # 获取x分坐标
                yCoordinate = float(lines[atomIndex].split( )[2])      # 获取y分坐标
                zCoordinate = float(lines[atomIndex].split( )[3])      # 获取z分坐标
                Xcar = self.Xa*xCoordinate+self.Xb*yCoordinate+self.Xc*zCoordinate    # 计算x笛卡尔分坐标
                Ycar = self.Ya*xCoordinate+self.Yb*yCoordinate+self.Yc*zCoordinate    # 计算y笛卡尔分坐标
                Zcar = self.Za*xCoordinate+self.Zb*yCoordinate+self.Zc*zCoordinate    # 计算z笛卡尔分坐标
                carContent = lineFirstElement+" "+str(Xcar)+" "+str(Ycar)+" "+str(Zcar)+"\n"         # 将元素符号和xyz坐标用空格分隔，连接成字符串
                atomLines.append(carContent)         # 列表添加笛卡尔坐标
                tempList.append(lineFirstElement)    # 临时列表添加元素符号
                tempList.append(Xcar)                # 临时列表添加x笛卡尔分坐标，注意该分坐标是一个数值，而不是字符串
                tempList.append(Ycar)
                tempList.append(Zcar)
                atomDict[atomIndex-6] = tempList     # 字典的键从1开始，值是一个列表，列表存储了元素符号和xyz的笛卡尔分坐标
                atomIndex += 1             
            self.atomList  = atomList                # 存储元素化学符号的列表
            self.atomLines = atomLines               # 存储笛卡尔坐标的列表，该列表包含了多个原子的坐标
            self.atomDict  = atomDict                # 这个字典存储了所有原子的化学符号和笛卡尔坐标，以列表的形式，键是原子序号，值是原子符号和坐标的列表           
            # self.atomDict =  {224: ['V', 9.695581698968155, 1.9771535016091875, 15.01112129458808]}

    # -1 方法    
    def test(self):                                    # 该方法主要用于测试
        print('总原子数：',self.atomNumber,'最后一行原子坐标的索引',self.endingLineIndex,'体系中各原子数量',Counter(self.atomList))
        print('笛卡尔原子坐标列表',self.atomLines)
        print('笛卡尔坐标字典',self.atomDict)
        # print('读取的原文件',self.lines)
        print('相对原子质量字典',self.atomKindDict)


    # 01方法，分数坐标转笛卡尔坐标        
    def cellToxyz(self):
        with open(self.saveFile, 'w') as new_file:     # 打开一个文件只用于写入。如果该文件已存在覆盖原有内容。如果该文件不存在，创建新文件。
            new_file.write(str(self.atomNumber)+"\n")  # 首行先写入体系的原子数
            # Tv_1: 7.426 0.0 0.0 Tv_2: 3.6 6 6.40 0.0 Tv_3: 0.0 0.0 10.0
            new_file.write("Tv_1: "+ str(self.cellLength)+ " 0.0 0.0 Tv_2: 0.0 "+ str(self.cellWidth) + " 0.0 Tv_3: 0.0 0.0 "+ str(self.cellHeight)+"\n")
        with open(self.saveFile, 'a') as new_file:     # 追加用a，若文件不存在，则创建新文件进行写入
            for i,j in enumerate(self.atomLines):      # 将原子坐标列表中每一个元素写入到文件中
                new_file.write(j)
        print ('体系中总原子数量',len(self.atomList),"体系中各原子数量",Counter(self.atomList))


    # 02方法，分数坐标转data文件
    def cellToData(self,atomOrder):
        self.atomOrder = atomOrder                     # 对方法中传入的原子顺序进行初始化
        inputAtomList = self.atomOrder.split(',')      # 输入的有顺序的原子列表
        if len(inputAtomList) != self.atomKinds:       # 判断输入的原子种类数和cell文件中的原子种类数是否一致
            print('输入的原子种类数错误，请重新输入！')
            sys.exit('输入的原子种类数错误，请重新输入！')
        with open(self.saveFile, 'w') as new_file:     # 打开一个文件只用于写入。如果该文件已存在覆盖原有内容。如果该文件不存在，创建新文件。
            new_file.write("# LAMMPS data file converted by Python 3.8, Y.W. Sun"+"\n")  # 第1行先写入注释，也可以写入空行
            new_file.write(str(self.atomNumber)+ ' ' +'atoms' +"\n")      # 第2行写入原子数
            new_file.write("\n")                                          # 第3行写入空行
            new_file.write(str(self.atomKinds)+ ' ' +'atom types' +'\n')               # 第4行写入原子类型的数量
            new_file.write("\n")                                          # 第5行写入空行
            new_file.write('0.0 '+ str(self.cellLength) +' xlo xhi'+"\n") # 第6行写入盒子x方向的长度
            new_file.write('0.0 '+ str(self.cellWidth) +' ylo yhi'+"\n")  # 第7行写入盒子x方向的长度
            new_file.write('0.0 '+ str(self.cellHeight) +' zlo zhi'+"\n") # 第8行写入盒子x方向的长度
            new_file.write("\n")                                          # 第9行写入空行
            new_file.write('Masses'+"\n")                                 # 第10行写入Masses
            new_file.write("\n")                                          # 第11行写入空行
            #     1 28.0855 # Si
            for i,j in enumerate(inputAtomList):                          # 遍历输入的元素列表，该列表是有顺序的
                #     1 28.0855 # Si
                massStr = str(i+1)+' '+ self.atomKindDict[j] + ' # '+ j
                new_file.write( massStr +"\n")                            # 第12起行写入原子类型和相对原子质量，列表索引i是从0开始的
            new_file.write("\n")                                          # 空行
            choice = input("请选择 atomic_style（输入 1 代表 'charge'，输入 2 代表 'atomic'）：")
            if choice == '1':      # charge 原子格式
                new_file.write('Atoms # charge'+"\n")                         # 写入Atoms，注释为charge类型
                new_file.write("\n")                                          # 空行
                # 1 1   0   10.11087605 10.30264943 5.200900751
                imass = 1
                for i,j in enumerate(inputAtomList):
                    for k in list(self.atomDict.keys()):
                        if j == self.atomDict[k][0]:        # 判断元素种类 self.atomDict =  {224: ['V', 9.695581698968155, 1.9771535016091875, 15.01112129458808]}
                            dataLine = str(imass) +' '+str(i+1)+ ' 0 '+str(self.atomDict[k][1])+' '+str(self.atomDict[k][2])+' '+str(self.atomDict[k][3])
                            new_file.write(dataLine +"\n")                   # 将序号，原子类型，电荷和坐标写入到data文件中
                            imass += 1

            elif choice == '2':    # atomic 原子格式
                new_file.write('Atoms # atomic'+"\n")                         # 写入Atoms，注释为charge类型
                new_file.write("\n")                                          # 空行
                # 1 1   0   10.11087605 10.30264943 5.200900751
                imass = 1
                for i,j in enumerate(inputAtomList):
                    for k in list(self.atomDict.keys()):
                        if j == self.atomDict[k][0]:        # 判断元素种类 self.atomDict =  {224: ['V', 9.695581698968155, 1.9771535016091875, 15.01112129458808]}
                            dataLine = str(imass) +' '+str(i+1)+ ' '+str(self.atomDict[k][1])+' '+str(self.atomDict[k][2])+' '+str(self.atomDict[k][3])
                            new_file.write(dataLine +"\n")                   # 将序号，原子类型，电荷和坐标写入到data文件中
                            imass += 1
            else:
                print("输入无效，请输入1或2。")

def inputFunction():     # 打印出当前目录下的所有文件名
    print("默认打开当前目录，是否调用GUI获取文件路径?Yes=1,No=2, 直接输入Enter键默认为2")     # 提示命令行输入
    fileOpenStyle = input()
    if fileOpenStyle == '':
        fileOpenStyle = 2
    # fileOpen = int(input())              # 注意字符串输入变量的数据类型转换
    if fileOpenStyle == "1":
        root = tk.Tk()
        root.withdraw()
        f_path = filedialog.askopenfilename()
        txtName = f_path
        print('\n获取的文件地址：', f_path)
    else:
        for root, dirs, files in os.walk("."):
            for filename in files:
                print(filename)  
        print("请输出需要处理的.cell文件名")     # 提示命令行输入
        txtName = input()              # 注意字符串输入变量的数据类型转换
    return txtName



if __name__ == '__main__':
    print('''
  本脚本的功能如下:
      01: Material Studio分数坐标cell文件转 Multiwfn标准格式的xyz笛卡尔坐标文件
      02: Material Studio分数坐标cell文件转 lammps标准格式的data结构文件
      
      -1: 测试
           
          ''')
    print("请选择功能，输入Enter默认为-1测试")     # 提示选择功能
    defChoose = input()
    
    if defChoose == '' :                       # 将Enter快捷键默认值设为-1
        defChoose = "-1"
        
    if defChoose == "-1":
        saveFile = "6868.xyz"                  # 该参数为类默认值，对test该方法无意义
        cellFile1 = cellConventer(inputFunction(),saveFile)        
        cellFile1.test()

        
    elif defChoose == "01":
        print("请为转换后的文件命名，输入Enter默认为 01_cellToxyz.xyz")     # 提示命令行输入
        saveFile = input()              # 注意字符串输入变量的数据类型转换
        if saveFile == '' :
            saveFile = "01_cellToxyz.xyz"       # 设置输入Enter时默认的输出文件名
            print("采用默认 01_cellToxyz.xyz ")  
        cellFile1 = cellConventer(inputFunction(),saveFile)                        # 对类进行实例化
        cellFile1.cellToxyz()

    elif defChoose == "02":
        print("请为转换得到的data文件命名，输入Enter默认为 02_cellToData.data")     # 提示命令行输入
        saveFile = input()              # 注意字符串输入变量的数据类型转换
        if saveFile == '' :
            saveFile = "02_cellToData.data"       # 设置输入Enter时默认的输出文件名
            print("采用默认 02_cellToData.data ")  
        cellFile1 = cellConventer(inputFunction(),saveFile)                        # 对类进行实例化
        print("请输入想要采用的原子顺序，用英文逗号隔开，如: Si,B,Ca,O")
        atomOrder = input()
        cellFile1.cellToData(atomOrder)

    else:
        print("提示：您选择的功能正在开发，请重新选择！")
        

timeEnd = datetime.datetime.now()          # 显示时间 
timeDuration = timeEnd - timeStart  
print('''
-----------------------------
该任务执行完毕，祝您工作顺利!\n任务总耗时：
''',timeDuration)
     
