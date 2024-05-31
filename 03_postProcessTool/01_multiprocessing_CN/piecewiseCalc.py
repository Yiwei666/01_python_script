# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:52:30 2024

@author: sun78
"""

# 01函数
"""
注释：用于获取当前目录下的文件名。函数会先询问用户是否需要通过GUI获取文件路径，如果需要则打开文件选择对话框，
否则直接输出当前目录下的所有文件名并要求用户输入需要处理的文件名。最后返回用户输入的文件名
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
import multiprocessing



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
        print("请输出需要处理的文件名,包含xyz、ener等格式，如 50_SiV(0-500).xyz、SiV-1.ener")     # 提示命令行输入
        txtName = input()              # 注意字符串输入变量的数据类型转换
    return txtName




# 02函数，用于数字字符串的分隔
"""
注释：代码的功能是将一个包含数字和范围的字符串（如："1,3,5-10,30"）转换为一个包含所有数字的排序列表 
"""
def inputSplit(strStyleNumber):    # 对数字字符串进行分割，输入"1,3,5-10,30"格式字符串，返回数字列表
    # subSplit是一个在函数内定义的函数，输入类似于"3-5"的单个字符串
    def subSplit(subStr):          # subStr 是这一种 "3-5"，该用于解析['5-10', '55-58']类似列表
        subList = []               # 
        subFinal = []
        for x in subStr.split("-"):
            subList.append(x)
        for y in  range(int(subList[0]),int(subList[1])+1):
            subFinal.append(y)
        # print(subFinal)
        return subFinal            # 输入“3-5”，返回“3”，“4”，“5”
    listOne = []
    listSubOne = []
    listSubTwo = []
    listTotal = []
    for i in strStyleNumber.split(","):
        listOne.append(i)
    print("输入列表：",listOne)
    for j in listOne:
        if j.find("-") == -1:
            listSubOne.append(int(j))     # 添加不含'-'的字符串
        else:
            listSubTwo.append(j)          # 添加包含'-'的字符串
    # print(listSubOne,listSubTwo)
    for m in listSubTwo:                  # 
        listTotal = listTotal + subSplit(m)   # 调用subSplit()函数，
    listFinal = listTotal + listSubOne
    listFinal.sort()                      # 对列表进行排序
    print("返回列表：",listFinal)
    return listFinal                      # 注意返回值是一个数字列表，如[5, 6, 7, 8, 9, 10]
  



def xyzImportFile(name,replace,saveFile):  # 注意是__是双下划线，3个形参中只有name参数是每个方法都依赖的
    '''
    self.name = name                     # 需要修改的原xyz文件，需要被分析的xyz文件名字，如 53_V-slag(0-500).xyz 格式
    self.replace = replace               # 添加的晶格参数，字符串，
    self.saveFile = saveFile             # 修改后的xyz文件命名，字符串

    self.xCell = float(self.replace.split( )[0])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为x分量
    self.yCell = float(self.replace.split( )[1])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为y分量
    self.zCell = float(self.replace.split( )[2])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为z分量
    
    self.xyzList = lines                 # 轨迹文件列表实例化,列表,每一行为列表中的一个元素
    self.length = len(lines)             # xyz文件行数，数值
    self.firstline = int(lines[0])       # 第一帧第一行的数字，即第一帧原子数
    
    self.allFirstLineList = iaList       # xyz轨迹文件所有帧的第一行数字列表，即每一帧的原子数
    self.frameNumber = len(iaList)       # 计算xyz文件的所有帧数
    self.allFrameDict = iaDict           # 将每一帧的第一行对应的行数、原子数、以及该帧的所有行写成字典，行数是从1开始的,对应键的值是一个列表
    self.firstLineIndex = lineIndexList  # 列表，用于储存每一帧中首行的对应行数的index，从0开始
    
    self.xyzDict = xyzDict               # 将字典变量设为全局变量，该字典包含每一帧中各原子的xyz坐标，各分坐标以列表形式储存
           
    '''
    
    
    xCell = float(replace.split( )[0])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为x分量，注意数据类型转变，字符串转浮点数
    yCell = float(replace.split( )[1])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为y分量，注意数据类型转变，字符串转浮点数
    zCell = float(replace.split( )[2])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为z分量，注意数据类型转变，字符串转浮点数
    
    with open(name, 'r') as f:
        # lines = f.readlines()
        lines = [line.rstrip('\n') for line in f.readlines()]
        xyzList = lines                       # 轨迹文件列表实例化，即所有行写成一个列表
        length = len(lines)                   # 列表长度
        firstline = int(lines[0])             # 第一帧第一行的数字，即第一帧原子数
    
    ia = 0                                         # 对行数进行计数，index从0开始
    ib = 1                                         # 对帧数进行计数，标记第一帧的序号从1开始
    iaList = []                                    # 列表，用于储存每一帧原子数
    lineIndexList = []                             # 列表，用于储存每一帧中首行的对应行数的index，从0开始
    iaDict = {}                                    # 将每一帧的第一行对应的行数、原子数、以及对应帧的所有行写成字典，行数是从1开始的
    while ia < len(lines):                         # 循环结束的条件是索引小于轨迹文件的总行数
        iaList.append(int(lines[ia]))              # 列表，用于储存每一帧原子数
        lineIndexList.append(ia)                                           # 列表，用于储存每一帧中首行的对应行数的index，从0开始
        iaDict[ib] = [ia+1,int(lines[ia]),lines[ia:ia+2+int(lines[ia])]]   # 切片，列表的第一个参数ia+1代表行数（index参数ia从0开始），第二个参数代表对应行数的数值，即对应帧数的原子数
                                                                           # 上面第三个数字代表相应帧数的元素，包括晶格信息，原子数，元素名称和坐标
                                                   # 切片[i:j]的规则是包含索引为i的不包含索引为j的
        ia = ia + int(lines[ia])+2                 # 确定每一帧首行（含有原子数的的那一行）的索引
        ib = ib + 1 
    allFirstLineList = iaList                 # xyz轨迹文件所有帧的第一行数字列表，即每一帧的原子数
    frameNumber = len(iaList)                 # 计算xyz文件的所有帧数
    allFrameDict = iaDict                     # 将每一帧的第一行对应的行数、原子数、以及对应帧的所有行写成字典
    firstLineIndex = lineIndexList            # 列表，用于储存每一帧中首行的对应行数的index，从0开始
    '''
    self.allFrameDict = iaDict
    {
        1: [1, 2, ['2', '11.2 11.2 11.2', 'Si 0 0 0', 'Ca 1 1 1']], 
        2: [5, 2, ['2', '11.2 11.2 11.2', 'Si 2 2 2', 'Ti 3 3 3']]
     }

    xyzDict是一个字典，称为父字典，其键为帧数，键为1对应第1帧，对应的值是一个字典，称为子字典
    父字典对应键为0的值为一个数值，对应该xyz文件的总帧数
    子字典对应每一帧的每个原子坐标，子字典中键为1对应第一个原子
    子字典对应键为0的值是一个数值，是相应帧数的原子数     

    '''
    xyzDict = {} # 将每一帧的每一个原子坐标写成字典，键是帧数，值是一个子字典，子字典中的键是原子序号，从1开始，值是对应原子坐标。子字典键为0对应的值是对应帧的原子数
    xyzDict[0] = frameNumber                                # 将父字典键为0对应的值设为帧数
    for iframe in range(1,frameNumber+1):                   # 帧数从1开始，一共frameNumber帧
        xyzDict[iframe] = {}                                     # 父字典的值是一个子字典时，需要进行类似的初始化以确定值的字典类型
        xyzDict[iframe][0] = allFrameDict[iframe][1]        # 父字典的键为0对应的值是对应帧数的原子数，注意原子序数是从1开始计数，是一个数值，不是字符串
        for iatom in range(2,allFrameDict[iframe][1] + 2):  # +2代表每一帧的第一行和第二行，range范围后一个值代表对应帧数的总行数            
            perAtomxyz = allFrameDict[iframe][2][iatom].split( )  # iatom是索引index，原子坐标是每帧的索引为2的对应行开始的
            xyzDict[iframe][iatom-1] = perAtomxyz                # 由于iatom是从2开始计数，iatom-1就是起始原子编号，即从1开始
    # xyzDict = xyzDict                                       # 将字典变量设为全局变量，该字典包含每一帧中各原子的xyz坐标，各分坐标以列表形式储存
    return [[xCell,yCell,zCell],frameNumber,xyzDict,allFrameDict]
    
    # self.allFrameDict = {1: [1, 224, ['224\n', 'Frame 0 cell_orig 0.0 0.0 0.0 cell_vec1 16.4477223556 0.0 0.0 cell_vec2 0.0 16.4477223556 0.0 cell_vec3 0.0 0.0 16.4477223556 pbc 1 1 1\n', 'Si 2.3983325131 5.0877985511 13.791799328\n', 
    '''
    xyzDict
    {
        0: 3, 
        1: {0: 2, 1: ['Si', '0', '0', '0'], 2: ['Ca', '1', '1', '1']}, 
        2: {0: 2, 1: ['Si', '2', '2', '2'], 2: ['Ti', '3', '3', '3']}, 
        3: {0: 3, 1: ['H', '3.1', '2.2', '1'], 2: ['B', '4.1', '2.5', '6.6'], 3: ['P', '1.1', '2.2', '3.3']}
    }
    '''



# 03方法：计算每一帧的各原子编号
def atomIndexCalc(frameNo, allFrameDict):                      # 可用于计算xyz文件某一帧的各类原子序号(序号从1开始)
    '''
    此方法定义的全局变量来源于方法调用传入的参数
    self.frameNo = frameNo                            # frameNo参数是从实例中传入的，需要初始化，注意该帧数从1开始
    '''
    # self.frameNo = frameNo                            # 注意该帧数从1开始
    firstFlameList = allFrameDict[frameNo][2]   # 
    firFlame = {}                                     # 第一帧轨迹原子的字典，不包括前两行
    firElent = []
    for i,line in enumerate(firstFlameList):
        if i >= 2:
            firFlame[i-1] = line.split( )             # 填充字典
            firElent.append(line.split( )[0])         # 第一帧中各原子化学符号组成的列表
    print(firFlame)
    print(firElent)   #0-223,共224
    print(Counter(firElent))
    totalAtomNo = allFrameDict[frameNo][1]  # 总原子数
    print("总原子数：",totalAtomNo)
    print(firElent[0],"始于序号：",1)
    for i,j in enumerate(firElent):
        if i <= len(firElent)-2:
            if firElent[i+1] != j:
                print(j,"结束于:",i+1,"下一个原子",firElent[i+1],"始于序号：",i+2)
    print(firElent[-1],"原子结束于：",totalAtomNo)




def periodicBox(multiple,saveChoose,frameNumber,replace,xyzDict,xyzCellList):                  # 该方法构建一个周期性的盒子，并将其写入字典，saveChoose为“F”或“T”
    '''
    如下，该方法定义了两个比较重要的全局变量
    self.superTrajList = superTrajList     # 将扩增后的轨迹文件逐行写成超级列表
    self.xyzSuperDict = xyzSuperDict       # 将所有帧的原子数及坐标写成一个超级字典，子字典中的值对应一个xyz坐标数值列表，即列表元素是浮点数，而非字符串

    # self.xyzDict[2][15] = ['Si', '15.896150', '10.830315', '16.041859']
    # self.xyzSuperDict[2][400] = ['Si', 32.34385, 10.830315, -0.40584100000000234, [1, 0, -1], 15, ['Si', '15.896150', '10.830315', '16.041859']]         
    # self.xyzSuperDict 中对应的信息依次为 扩增后原子坐标，括增用倍数列表，
    该方法不依赖于其他方法，但是其他方法可能依赖于该方法，因此该方法需要置于其他依赖于该方法的方法之前
    '''
    # self.multiple = multiple                                # multiple是一个由空格分隔开的数字字符串，如"1 -2  3 -1  4 -1"
    # self.saveChoose = saveChoose                            # 该参数用于判断是否保存扩增后的xyz文件
    # self.frameNumber = len(iaList)                          # 计算xyz文件的所有帧数
    # self.replace = replace                                  # 添加的晶格参数，字符串
    # xyzCellList = [xCell,yCell,zCell]
    xCell = xyzCellList[0]
    yCell = xyzCellList[1]
    zCell = xyzCellList[2]
    multiList = multiple.split( )
    xp = int(multiList[0])                                  # 在x正轴扩增的倍数，p代表positive，n代表negative
    xn = int(multiList[1])
    yp = int(multiList[2])
    yn = int(multiList[3])
    zp = int(multiList[4])
    zn = int(multiList[5])
    xList = sorted(list(set([j for j in range(xn,1)] + [i for i in range(0,xp+1)] )))
    yList = sorted(list(set([j for j in range(yn,1)] + [i for i in range(0,yp+1)] )))
    zList = sorted(list(set([j for j in range(zn,1)] + [i for i in range(0,zp+1)] )))
    # print('xList,yList,zList分别为',xList,yList,zList)
    '''
    # xList = [-2, -1, 0, 1]
    # yList = [-1, 0, 1, 2, 3]
    # zList = [-1, 0, 1, 2, 3, 4]
    '''
    boxNumber = len(xList)*len(yList)*len(zList)
    boxDict = {}
    for d in range(1,boxNumber+1):     # 初始化为列表
        boxDict[d] = []                # 构建一个字典，字典的值是列表，列表依次储存扩增的倍数
    icount = 1                         # 字典的键从1开始计数
    for x in xList:
        for y in yList:
            for z in zList:
                boxDict[icount].append(x)
                boxDict[icount].append(y)
                boxDict[icount].append(z)
                icount = icount +1
    # print('扩增盒子字典：',boxDict)
    '''
    {
        1: [-2, -1, -1],
        2: [-2, -1, 0],
        3: [-2, -1, 1],
        # ...
        119: [1, 3, 3],
        120: [1, 3, 4]
    }
    '''
    superTrajList = []             # 初始化一个字典，字典包含了盒子扩增后轨迹文件所有行都在内的列表，类似于self.xyzList
    xyzSuperDict = {}              # 初始化一个超级字典，用于储存扩增后的盒子信息，类似于xyzDict储存括增前每一帧的原子坐标等信息
    xyzSuperDict[0] = frameNumber      # 1.扩增后的总帧数，跟扩增前一样，扩增不改变帧数
    for i in range(1,frameNumber+1):                               # 最外层先遍历帧数
        '''
        xyzDict
        {
            0: 3, 
            1: {0: 2, 1: ['Si', '0', '0', '0'], 2: ['Ca', '1', '1', '1']}, 
            2: {0: 2, 1: ['Si', '2', '2', '2'], 2: ['Ti', '3', '3', '3']}, 
            3: {0: 3, 1: ['H', '3.1', '2.2', '1'], 2: ['B', '4.1', '2.5', '6.6'], 3: ['P', '1.1', '2.2', '3.3']}
        }
        '''
        superTrajList.append(str(xyzDict[i][0]*boxNumber)+'\n')    # 2.添加每一帧的原子数，盒子数*每个盒子的原子数，对应每一帧第一行
        superTrajList.append(replace + '\n')                       # 3.添加盒子信息，对应每一帧第二行
        xyzSuperDict[i] = {}                                            # 初始化子字典，用于储存原子坐标
        xyzSuperDict[i][0] = xyzDict[i][0]*boxNumber               # 4.计算每一帧的原子数
        atomCount = 1                                                   # 对扩增后的每一帧原子进行计数，从1开始，切换下一帧后会重置为1开始计算
        for j in range(1,xyzDict[i][0]+1):  # 获取原盒子中每个原子的序号及坐标等信息，次外层遍历每一帧原盒子中的每个原子
            elementName = xyzDict[i][j][0]  # 获取原盒子中每个原子的化学符号
            xc = float(xyzDict[i][j][1])    # xc代表原子坐标的x分量，component，代表第i帧第j个原子
            yc = float(xyzDict[i][j][2])    # yc代表原子坐标的y分量，component  
            zc = float(xyzDict[i][j][3])    # zc代表原子坐标的z分量，component                
            # print(elementName,xc,yc,zc)
            for ibox in range(1,boxNumber+1):    # 最内层遍历盒子，也就是说扩增后的盒子中原子的相对顺序并未改变

                xMul = boxDict[ibox][0] * xCell + xc
                yMul = boxDict[ibox][1] * yCell + yc
                zMul = boxDict[ibox][2] * zCell + zc
                xyzMul =  elementName +' '+ str(xMul)+' '+ str(yMul)+' '+ str(zMul)+'\n'  #
                superTrajList.append(xyzMul)            # 将扩增后的原子符号和分坐标写进超级列表
                
                xyzCoordVector = []                     # 每次写入分坐标都要进行重置归空
                xyzCoordVector.append(elementName)      # 子字典对应的列表第1个元素是原子的化学符号        
                xyzCoordVector.append(xMul)             # 第2个元素是原子扩增后的x分坐标，数值
                xyzCoordVector.append(yMul)             # 第3个元素是原子扩增后的y分坐标，数值
                xyzCoordVector.append(zMul)             # 第4个元素是原子扩增后的z分坐标，数值
                xyzCoordVector.append(boxDict[ibox])    # 第5个元素是采用的括增倍数，列表
                xyzCoordVector.append(j)                # 第6个元素是原盒子中该原子的序号，数值
                xyzCoordVector.append(xyzDict[i][j])  # 第7个元素是原盒子中该原子的元素符号和分坐标，列表字符串形式
                xyzSuperDict[i][atomCount] = xyzCoordVector
                atomCount = atomCount + 1
    # self.superTrajList = superTrajList           # 将扩增后的轨迹文件逐行写成超级列表
    # self.xyzSuperDict = xyzSuperDict             # 将所有帧的原子数及坐标写成一个超级字典，包含扩增后的原子坐标信息以及括增前的坐标信息
    '''
    # 括增前后两个子字典值的区别，xyzSuperDict不仅包含扩增后的坐标，还包含扩增倍数，扩增前的原子序号和原子坐标
    # self.xyzDict[2][15] = ['Si', '15.896150', '10.830315', '16.041859']
    # self.xyzSuperDict[2][400] = ['Si', 32.34385, 10.830315, -0.40584100000000234, [1, 0, -1], 15, ['Si', '15.896150', '10.830315', '16.041859']]         
    '''


    print('第一帧原子数:',superTrajList[0])
    print('总原子数(第一帧原子数*总帧数):',xyzDict[1][0]*boxNumber*xyzDict[0])
    print("扩增后的盒子三边长度(单位：埃)分别为：",(xp-xn+1)*xCell,(yp-yn+1)*yCell,(zp-zn+1)*zCell)
    return xyzSuperDict






def coordination_piecewise(r_ij, d_AB):        # 分段函数，小于等于截断半径，配位数为1，否则为0
    if r_ij <= d_AB:
        return 1
    else:
        return 0    
  




def sigmoid_coordination_mtd(r_ij, d_AB, NN, ND):
    # Calculate the numerator part of the formula
    # p = NN
    # q = ND - NN
    
    numerator = 1 - (r_ij / d_AB) ** NN
    
    # Calculate the denominator part of the formula
    denominator = 1 - (r_ij / d_AB) ** ND
    
    # Return the final result of the function
    return numerator / denominator




# atPairCut_Result = self.result
# grandxyzDict = self.xyzSuperDict
# prexyzDict = self.xyzDict
# inputCenterAtomRange = self.atomNumberRange



        
def process_piecewise_frame(frameNumberList, atPairCut_Result, prexyzDict, grandxyzDict, inputCenterAtomRange, result_dict):
    print(frameNumberList)
    rij_coordinationDict = {}                             # 该字典用于储存每一帧中各中心与配位原子对的配位数
    rij_coord_outputDict = {}                             # 进一步计算 rij_coordinationDict 保存的数据
    for u in range(frameNumberList[0],frameNumberList[1]):
        rij_coordinationDict[u] = {}                      # 每一帧中可能有好几种原子对，每一种原子对都用一个字典来管理
        rij_coord_outputDict[u] = {}
        for x,y in zip(atPairCut_Result[0],atPairCut_Result[1]):
            atom_pair = x +"-"+ y
            rij_coordinationDict[u][atom_pair] = []       # 给每一种中心原子及其配位原子的距离初始化一个列表，包含中心原子与其本身形成的原子对
            rij_coord_outputDict[u][atom_pair] = {}
    
    for i in range(frameNumberList[0],frameNumberList[1]):     # 帧数循环
        # print(self.xyzSuperDict[0])
        # print(self.xyzSuperDict[i][0])
        iExtract = 0                               # 该参数用于计数，即每一帧中在截断半径内的原子数量
        newExtractList = []                        # 该列表用于储存每一帧中满足截断半径要求的原子信息，该列表每一帧要重新释放置零并重新赋值
         
        for j in range(1,grandxyzDict[i][0]+1):   # 每一帧中的原子循环，self.xyzSuperDict[i][0]代表扩增后盒子轨迹第i帧的原子数
            eName = grandxyzDict[i][j][0]         # 计算第i帧中第j个原子的元素符号和各分坐标
            ex = grandxyzDict[i][j][1]            # 针对每一帧，分别将每个原子与传入的目标原子的距离进行比较
            ey = grandxyzDict[i][j][2]
            ez = grandxyzDict[i][j][3]
            # print(eName,ex,ey,ez)
            for l in inputCenterAtomRange:             # self.atomNumberRange是传入的目标原子编号列表，即计算这些原子截断半径范围内的配位原子
                lName = prexyzDict[i][l][0]
                lx = float(prexyzDict[i][l][1])
                ly = float(prexyzDict[i][l][2])
                lz = float(prexyzDict[i][l][3])
                distance = math.sqrt(((ex-lx)**2)+((ey-ly)**2)+((ez-lz)**2))                  # 计算两个原子间的距离
                # print(distance)
                # print(lName,lx,ly,lz)
                """
                1.设置原子截断半径的中心原子种类 result[0] 范围要大于等于 编号对应的原子种类 atomNumberRange
                2.注意编号的中心原子的计算
                """
                
                if lName not in atPairCut_Result[0]:            # 如果编号对应的中心原子与原子对中的中心原子种类不符合，则中断。
                    print("设置原子对截断半径的中心原子种类 与 输入原子编号对应的中心原子种类不符")
                    print("报错的原子编号以及原子种类为：",l,lName)
                    sys.exit(1)                            # 终止程序，返回退出码 1

                if eName == lName and distance < 0.01:     # 单位是埃，理论上应该设为0，筛选出编号原子
                    iExtract = iExtract +1                 # 对满足截断半径的原子进行计数
                    newExtractList.append(eName+' '+str(ex)+' '+str(ey)+' '+str(ez)+'\n')     # 将满足要求的原子信息添加到列表中
                    continue                               # 当编号的中心原子和配位原子是同一原子时，跳出本次循环

                for icount,icenter in enumerate(atPairCut_Result[0]):                        # 遍历result[0]-result[1]中对应的每一个原子对
                    if icenter == lName and atPairCut_Result[1][icount] == eName:            # 判断result[0]-result[1] 原子对和 l-j 原子对是否相同
                        if distance <= atPairCut_Result[2][icount] :                         # 判断距离是否满足截断半径
                            r_ij = distance
                            d_AB = atPairCut_Result[2][icount]
                            perCoordination = coordination_piecewise(r_ij, d_AB)
                            rij_coordinationDict[i][lName+"-"+eName].append(perCoordination)
                            iExtract = iExtract +1                                                    # 对满足截断半径的原子进行计数
                            newExtractList.append(eName+' '+str(ex)+' '+str(ey)+' '+str(ez)+'\n')     # 将满足要求的原子信息添加到列表中
    
    # print("目标原子局域结构输出文件已保存！",rij_coordinationDict)    

    for frame, i in rij_coordinationDict.items():
        for atomPair,perCoorValueList in i.items():
            rij_coord_outputDict[frame][atomPair]["total_sum"] = f"{sum(perCoorValueList):.3g}"
            rij_coord_outputDict[frame][atomPair]["atomPair_number"] = len(perCoorValueList)
            rij_coord_outputDict[frame][atomPair]["perFrameAverageCN"] = f"{sum(perCoorValueList)/len(inputCenterAtomRange):.3g}"   # 需要除以中心原子的总数，对于单个原子是1
    print(rij_coord_outputDict)

    result_dict.update(rij_coord_outputDict)
    print(result_dict)

  


  
# xCell 盒子边长
def process_sigmoid_frame(frameNumberList, atPairCut_Result, prexyzDict, grandxyzDict, inputCenterAtomRange, xCell, NN, ND, result_dict):
    print(frameNumberList)
    rij_coordinationDict = {}                             # 该字典用于储存每一帧中各中心与配位原子对的配位数
    rij_coord_outputDict = {}                             # 进一步计算 rij_coordinationDict 保存的数据
    for u in range(frameNumberList[0],frameNumberList[1]):
        rij_coordinationDict[u] = {}                      # 每一帧中可能有好几种原子对，每一种原子对都用一个字典来管理
        rij_coord_outputDict[u] = {}
        for x,y in zip(atPairCut_Result[0],atPairCut_Result[1]):
            atom_pair = x +"-"+ y
            rij_coordinationDict[u][atom_pair] = []       # 给每一种中心原子及其配位原子的距离初始化一个列表，包含中心原子与其本身形成的原子对
            rij_coord_outputDict[u][atom_pair] = {}
    
    for i in range(frameNumberList[0],frameNumberList[1]):     # 帧数循环
        # print(self.xyzSuperDict[0])
        # print(self.xyzSuperDict[i][0])
        iExtract = 0                               # 该参数用于计数，即每一帧中在截断半径内的原子数量
        newExtractList = []                        # 该列表用于储存每一帧中满足截断半径要求的原子信息，该列表每一帧要重新释放置零并重新赋值
         
        for j in range(1,grandxyzDict[i][0]+1):   # 每一帧中的原子循环，self.xyzSuperDict[i][0]代表扩增后盒子轨迹第i帧的原子数
            eName = grandxyzDict[i][j][0]         # 计算第i帧中第j个原子的元素符号和各分坐标
            ex = grandxyzDict[i][j][1]            # 针对每一帧，分别将每个原子与传入的目标原子的距离进行比较
            ey = grandxyzDict[i][j][2]
            ez = grandxyzDict[i][j][3]
            # print(eName,ex,ey,ez)
            for l in inputCenterAtomRange:             # self.atomNumberRange是传入的目标原子编号列表，即计算这些原子截断半径范围内的配位原子
                lName = prexyzDict[i][l][0]
                lx = float(prexyzDict[i][l][1])
                ly = float(prexyzDict[i][l][2])
                lz = float(prexyzDict[i][l][3])
                distance = math.sqrt(((ex-lx)**2)+((ey-ly)**2)+((ez-lz)**2))                  # 计算两个原子间的距离
                # print(distance)
                # print(lName,lx,ly,lz)
                """
                1.设置原子截断半径的中心原子种类 result[0] 范围要大于等于 编号对应的原子种类 atomNumberRange
                2.注意编号的中心原子的计算
                """
                
                if lName not in atPairCut_Result[0]:            # 如果编号对应的中心原子与原子对中的中心原子种类不符合，则中断。
                    print("设置原子对截断半径的中心原子种类 与 输入原子编号对应的中心原子种类不符")
                    print("报错的原子编号以及原子种类为：",l,lName)
                    sys.exit(1)                            # 终止程序，返回退出码 1

                if eName == lName and distance < 0.01:     # 单位是埃，理论上应该设为0，筛选出编号原子
                    iExtract = iExtract +1                 # 对满足截断半径的原子进行计数
                    newExtractList.append(eName+' '+str(ex)+' '+str(ey)+' '+str(ez)+'\n')     # 将满足要求的原子信息添加到列表中
                    continue                               # 当编号的中心原子和配位原子是同一原子时，跳出本次循环

                for icount,icenter in enumerate(atPairCut_Result[0]):                       # 遍历result[0]-result[1]中对应的每一个原子对
                    if icenter == lName and atPairCut_Result[1][icount] == eName:           # 判断result[0]-result[1] 原子对和 l-j 原子对是否相同
                        if xCell/2 >= distance:                                             # 判断距离是否满足截断半径，xcell是盒子边长
                            r_ij = distance
                            d_AB = atPairCut_Result[2][icount]
                            perCoordination = sigmoid_coordination_mtd(r_ij, d_AB, NN, ND)  # NN和ND必须要在函数外获取，否则每个新进程中都得按照提示输入
                            rij_coordinationDict[i][lName+"-"+eName].append(perCoordination)
                            iExtract = iExtract +1                                                    # 对满足截断半径的原子进行计数
                            newExtractList.append(eName+' '+str(ex)+' '+str(ey)+' '+str(ez)+'\n')     # 将满足要求的原子信息添加到列表中

    # print("目标原子局域结构输出文件已保存！",rij_coordinationDict)    

    for frame, i in rij_coordinationDict.items():
        for atomPair,perCoorValueList in i.items():
            rij_coord_outputDict[frame][atomPair]["total_sum"] = f"{sum(perCoorValueList):.3g}"
            rij_coord_outputDict[frame][atomPair]["atomPair_number"] = len(perCoorValueList)
            rij_coord_outputDict[frame][atomPair]["perFrameAverageCN"] = f"{sum(perCoorValueList)/len(inputCenterAtomRange):.3g}"   # 需要除以中心原子的总数，对于单个原子是1
    # print(rij_coord_outputDict)

    result_dict.update(rij_coord_outputDict)
    # print(result_dict)
