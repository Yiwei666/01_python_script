# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:16:23 2022

@author: Y.W. Sun
@E-Mail: sun789sun@hotmail.com
"""
"""

此代码创建了一个用于解析和修改多帧xyz轨迹文件的类，可以用于添加盒子边长信息等
适用于单帧或多帧的xyz文件


"""
# class Xyz()
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

# class txtPlot()
# import os
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d.axes3d import Axes3D
# import pandas as pd


timeStart = datetime.datetime.now()          # 显示时间


# 01类
class Xyz():
    def __init__(self,name,replace,saveFile):  # 注意是__是双下划线，3个形参中只有name参数是每个方法都依赖的
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
        
        
        self.name = name
        self.replace = replace
        self.saveFile = saveFile
        
        self.xCell = float(self.replace.split( )[0])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为x分量，注意数据类型转变，字符串转浮点数
        self.yCell = float(self.replace.split( )[1])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为y分量，注意数据类型转变，字符串转浮点数
        self.zCell = float(self.replace.split( )[2])   # 假设输入的晶格为正交，三边长分别用空格分隔，此变量为z分量，注意数据类型转变，字符串转浮点数
        
        with open(self.name, 'r') as f:
            lines = f.readlines()
            self.xyzList = lines                       # 轨迹文件列表实例化，即所有行写成一个列表
            self.length = len(lines)                   # 列表长度
            self.firstline = int(lines[0])             # 第一帧第一行的数字，即第一帧原子数
        
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
        self.allFirstLineList = iaList                 # xyz轨迹文件所有帧的第一行数字列表，即每一帧的原子数
        self.frameNumber = len(iaList)                 # 计算xyz文件的所有帧数
        self.allFrameDict = iaDict                     # 将每一帧的第一行对应的行数、原子数、以及对应帧的所有行写成字典
        self.firstLineIndex = lineIndexList            # 列表，用于储存每一帧中首行的对应行数的index，从0开始
        '''
        xyzDict是一个字典，称为父字典，其键为帧数，键为1对应第1帧，对应的值是一个字典，称为子字典
        父字典对应键为0的值为一个数值，对应该xyz文件的总帧数
        子字典对应每一帧的每个原子坐标，子字典中键为1对应第一个原子
        子字典对应键为0的值是一个数值，是相应帧数的原子数        
        '''
        xyzDict = {} # 将每一帧的每一个原子坐标写成字典，键是帧数，值是一个子字典，子字典中的键是原子序号，从1开始，值是对应原子坐标。子字典键为0对应的值是对应帧的原子数
        xyzDict[0] = self.frameNumber                                # 将父字典键为0对应的值设为帧数
        for iframe in range(1,self.frameNumber+1):                   # 帧数从1开始，一共frameNumber帧
            xyzDict[iframe] = {}                                     # 父字典的值是一个子字典时，需要进行类似的初始化以确定值的字典类型
            xyzDict[iframe][0] = self.allFrameDict[iframe][1]        # 父字典的键为0对应的值是对应帧数的原子数，注意原子序数是从1开始计数，是一个数值，不是字符串
            for iatom in range(2,self.allFrameDict[iframe][1] + 2):  # +2代表每一帧的第一行和第二行，range范围后一个值代表对应帧数的总行数            
                perAtomxyz = self.allFrameDict[iframe][2][iatom].split( )  # iatom是索引index，原子坐标是每帧的索引为2的对应行开始的
                xyzDict[iframe][iatom-1] = perAtomxyz                # 由于iatom是从2开始计数，iatom-1就是起始原子编号，即从1开始
        self.xyzDict = xyzDict                                       # 将字典变量设为全局变量，该字典包含每一帧中各原子的xyz坐标，各分坐标以列表形式储存
        # self.allFrameDict = {1: [1, 224, ['224\n', 'Frame 0 cell_orig 0.0 0.0 0.0 cell_vec1 16.4477223556 0.0 0.0 cell_vec2 0.0 16.4477223556 0.0 cell_vec3 0.0 0.0 16.4477223556 pbc 1 1 1\n', 'Si 2.3983325131 5.0877985511 13.791799328\n', 
        

    # -1 方法    
    def test(self):                                    # 该方法主要用于测试
        print("第一帧原子数：",self.firstline)
        print("xyz文件总帧数",self.frameNumber)
        print("每一帧的原子数、所在行的行数及该帧所有元素字典，注意索引等于行数减去1：",self.allFrameDict)
        print("每一帧首行的Index列表：",self.firstLineIndex)
        print("轨迹文件列表长度：",self.length," 即轨迹文件总行数，该数值不计入最后一行空行")
        print("每一帧原子数列表：",self.allFirstLineList)
        print("self.xyzDict的总帧数，每帧含有的原子数",self.xyzDict[0],[self.xyzDict[i][0] for i in range(1,self.xyzDict[0]+1)])
        if self.allFirstLineList == [self.xyzDict[i][0] for i in range(1,self.xyzDict[0]+1)]:
            print("self.allFirstLineList == [self.xyzDict[i][0] for i in range(1,self.xyzDict[0]+1)]")
        
        self.periodicBox("1 -1 1 -1 1 -1","F")    # self.periodicBox(multiple,saveChoose),调用子方法中的全局变量前必须对子变量进行初始化
        # print(self.xyzSuperDict[2][400],self.xyzDict[2][15])
        print("每一帧的原子数、所在行的行数及该帧所有元素字典，注意索引等于行数减去1：",self.allFrameDict)
        # 括增前后两个子字典值的区别，xyzSuperDict不仅包含扩增后的坐标，还包含扩增倍数，扩增前的原子序号和原子坐标
        # self.xyzDict[2][15] = ['Si', '15.896150', '10.830315', '16.041859']
        # self.xyzSuperDict[2][400] = ['Si', 32.34385, 10.830315, -0.40584100000000234, [1, 0, -1], 15, ['Si', '15.896150', '10.830315', '16.041859']] 
        print(list(self.xyzDict[1]))
        '''
        self.periodicAtomIndex(1)
        print(self.KeyValueDict)
        print(self.KeyValueSuperDict)
        print(self.xyzDict[0])
        print(self.xyzSuperDict[0])
        print(self.frameNumber)
        
        for i,j in enumerate(self.firstLineIndex):
            print("帧数",i+1,"对应行数内容",self.xyzList[j])
        '''

    # 13方法：用于计算每一帧中特定原子到特定3个原子组成的平面间的距离
    def pointToPlaneDistance(self,disIndex,saveFile):
        self.disIndex = disIndex
        self.saveFile = saveFile
        dIndexList = self.disIndex.split(',')
        # import numpy as np
        pA = int(dIndexList[0])
        pB = int(dIndexList[1])
        pC = int(dIndexList[2])
        pD = int(dIndexList[3])
        
        def distance_from_plane(A, B, C, D):     # 点D 到平面ABC的距离
            # 计算平面法向量
            AB = np.subtract(B, A)
            AC = np.subtract(C, A)
            normal = np.cross(AB, AC)
        
            # 计算平面到原点的距离
            d = -np.dot(normal, A)
        
            # 计算点D到平面的距离
            distance = abs(np.dot(normal, D) + d) / np.linalg.norm(normal)
        
            return distance
                
        # A = [8.987708,7.553001,32.346226]
        # B = [6.760567,8.036732,32.353806]
        # C = [6.975581,4.544739,32.231148]
        # D = [0.303598,4.846121,6.626125]

        # distance = distance_from_plane(A, B, C, D)
        # 135,115,139,2
        # print(self.xyzDict[0])  # 总帧数
        for i in range(1,self.xyzDict[0]+1): # 遍历所有帧
            coorABCDList = []
            for j in [pA,pB,pC,pD]:
                xF  = float(self.xyzDict[i][j][1])   # x分坐标
                yF  = float(self.xyzDict[i][j][2])
                zF  = float(self.xyzDict[i][j][3])
                xyzF = [xF,yF,zF]
                coorABCDList.append(xyzF)
            print("A,B,C,D四点坐标分别为：", coorABCDList)
            d = distance_from_plane(coorABCDList[0], coorABCDList[1], coorABCDList[2], coorABCDList[3])
            print("帧数及对应的点到面的距离分别为：",i,"距离：",d)
            with open(self.saveFile, 'a+') as f:
                f.write(str(d)+'\n')



    # 11方法：将xyz文件转换为data文件，用于lammps经典分子动力学模拟
    def xyzToData(self,atomOrder,xyzFrame):   # atomOrder = 'Si,B,Ca,O' , xyzFrame = 1
        '''
        该方法暂不依赖于其他方法,内部中使用了函数
        '''
        self.atomOrder = atomOrder                      # 对方法中传入的原子顺序进行初始化
        self.xyzFrame  = xyzFrame                       # 对帧数进行实例化
        inputAtomList = self.atomOrder.split(',')       # 输入的有顺序的原子列表
        
        def dictCounter(valueList):                     # 定义子函数，统计valueList中各元素出现的次数
            result_dic={}
            for item_str in valueList:
                if item_str not in result_dic:
                    result_dic[item_str]=1
                else:
                    result_dic[item_str]+=1
            # print(result_dic)    
            return result_dic                           # 返回统计字典，{'Si': 216, 'V': 8}
        xyzFrameList = [ self.xyzDict[self.xyzFrame][i][0] for i in range(1,self.xyzDict[self.xyzFrame][0]+1) ]  # 第self.xyzFrame帧的元素符号列表
        xyzFrameDict = dictCounter(xyzFrameList)        # 返回字典，统计各元素出现的次数
        print('各原子数统计字典',xyzFrameDict)
        atomFrequencyList = list(xyzFrameDict.keys())   # 元素种类的列表
        self.atomKinds = len(atomFrequencyList)
        if len(inputAtomList) != self.atomKinds:        # 判断输入的原子种类数和cell文件中的原子种类数是否一致
            print('输入的原子种类数错误，请重新输入！')
            sys.exit('输入的原子种类数错误，请重新输入！')
        
        self.atomNumber = self.xyzDict[self.xyzFrame][0] # 对应帧的原子数
        self.cellLength = self.xCell                     # 盒子的边长
        self.cellWidth  = self.yCell
        self.cellHeight = self.zCell
        
        self.atomKindDict = { l: atomicMassSingleDict[l][3] for l in inputAtomList }   # 各原子类型及相应相对原子质量字典    
        print('原子类型及相对原子质量字典:',self.atomKindDict)
        self.atomDict = self.xyzDict[self.xyzFrame]        # 坐标字典，键是原子序号，值是一个列表，包括原子符号和坐标
        # self.xyzDict[self.xyzFrame]字典中对应某个原子序号(键)的值224: ['V', '7.124123', '14.828195', '2.215896']
        
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
            new_file.write('Atoms # charge'+"\n")                         # 写入Atoms，注释为charge类型
            new_file.write("\n")                                          # 空行
            # 1 1   0   10.11087605 10.30264943 5.200900751
            imass = 1
            for i,j in enumerate(inputAtomList):
                for k in list(self.atomDict.keys())[1:]:
                    if j == self.atomDict[k][0]:        # 判断元素种类 self.atomDict =  {224: ['V', 9.695581698968155, 1.9771535016091875, 15.01112129458808]}
                        dataLine = str(imass) +' '+str(i+1)+ ' 0 '+str(self.atomDict[k][1])+' '+str(self.atomDict[k][2])+' '+str(self.atomDict[k][3])
                        new_file.write(dataLine +"\n")                   # 将序号，原子类型，电荷和坐标写入到data文件中
                        imass += 1
            print('方法11已运行结束，输出文件：',self.saveFile)


    # 07方法：对xyz文件进行周期性扩增
    def periodicBox(self,multiple,saveChoose):                  # 该方法构建一个周期性的盒子，并将其写入字典，saveChoose为“F”或“T”
        '''
        如下，该方法定义了两个比较重要的全局变量
        self.superTrajList = superTrajList     # 将扩增后的轨迹文件逐行写成超级列表
        self.xyzSuperDict = xyzSuperDict       # 将所有帧的原子数及坐标写成一个超级字典，子字典中的值对应一个xyz坐标数值列表，即列表元素是浮点数，而非字符串

        # self.xyzDict[2][15] = ['Si', '15.896150', '10.830315', '16.041859']
        # self.xyzSuperDict[2][400] = ['Si', 32.34385, 10.830315, -0.40584100000000234, [1, 0, -1], 15, ['Si', '15.896150', '10.830315', '16.041859']]         
        # self.xyzSuperDict 中对应的信息依次为 扩增后原子坐标，括增用倍数列表，
        该方法不依赖于其他方法，但是其他方法可能依赖于该方法，因此该方法需要置于其他依赖于该方法的方法之前
        '''
        self.multiple = multiple                                # multiple是一个由空格分隔开的数字字符串，如"1 -2  3 -1  4 -1"
        self.saveChoose = saveChoose                            # 该参数用于判断是否保存扩增后的xyz文件
        multiList = self.multiple.split( )
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
      
        superTrajList = []             # 初始化一个字典，字典包含了盒子扩增后轨迹文件所有行都在内的列表，类似于self.xyzList
        xyzSuperDict = {}              # 初始化一个超级字典，用于储存扩增后的盒子信息，类似于xyzDict储存括增前每一帧的原子坐标等信息
        xyzSuperDict[0] = self.frameNumber      # 1.扩增后的总帧数，跟扩增前一样，扩增不改变帧数
        for i in range(1,self.frameNumber+1):                               # 最外层先遍历帧数
            superTrajList.append(str(self.xyzDict[i][0]*boxNumber)+'\n')    # 2.添加每一帧的原子数，盒子数*每个盒子的原子数，对应每一帧第一行
            superTrajList.append(self.replace + '\n')                       # 3.添加盒子信息，对应每一帧第二行
            xyzSuperDict[i] = {}                                            # 初始化子字典，用于储存原子坐标
            xyzSuperDict[i][0] = self.xyzDict[i][0]*boxNumber               # 4.计算每一帧的原子数
            atomCount = 1                                                   # 对扩增后的每一帧原子进行计数，从1开始，切换下一帧后会重置为1开始计算
            for j in range(1,self.xyzDict[i][0]+1):  # 获取原盒子中每个原子的序号及坐标等信息，次外层遍历每一帧原盒子中的每个原子
                elementName = self.xyzDict[i][j][0]  # 获取原盒子中每个原子的化学符号
                xc = float(self.xyzDict[i][j][1])    # xc代表原子坐标的x分量，component，代表第i帧第j个原子
                yc = float(self.xyzDict[i][j][2])    # yc代表原子坐标的y分量，component  
                zc = float(self.xyzDict[i][j][3])    # zc代表原子坐标的z分量，component                
                # print(elementName,xc,yc,zc)
                for ibox in range(1,boxNumber+1):    # 最内层遍历盒子，也就是说扩增后的盒子中原子的相对顺序并未改变
                    xMul = boxDict[ibox][0] * self.xCell + xc
                    yMul = boxDict[ibox][1] * self.yCell + yc
                    zMul = boxDict[ibox][2] * self.zCell + zc
                    xyzMul =  elementName +' '+ str(xMul)+' '+ str(yMul)+' '+ str(zMul)+'\n'  #
                    superTrajList.append(xyzMul)            # 将扩增后的原子符号和分坐标写进超级列表
                    
                    xyzCoordVector = []                     # 每次写入分坐标都要进行重置归空
                    xyzCoordVector.append(elementName)      # 子字典对应的列表第1个元素是原子的化学符号        
                    xyzCoordVector.append(xMul)             # 第2个元素是原子扩增后的x分坐标，数值
                    xyzCoordVector.append(yMul)             # 第3个元素是原子扩增后的y分坐标，数值
                    xyzCoordVector.append(zMul)             # 第4个元素是原子扩增后的z分坐标，数值
                    xyzCoordVector.append(boxDict[ibox])    # 第5个元素是采用的括增倍数，列表
                    xyzCoordVector.append(j)                # 第6个元素是原盒子中该原子的序号，数值
                    xyzCoordVector.append(self.xyzDict[i][j])  # 第7个元素是原盒子中该原子的元素符号和分坐标，列表字符串形式
                    xyzSuperDict[i][atomCount] = xyzCoordVector
                    atomCount = atomCount + 1
        self.superTrajList = superTrajList           # 将扩增后的轨迹文件逐行写成超级列表
        self.xyzSuperDict = xyzSuperDict             # 将所有帧的原子数及坐标写成一个超级字典，包含扩增后的原子坐标信息以及括增前的坐标信息
        '''
        # 括增前后两个子字典值的区别，xyzSuperDict不仅包含扩增后的坐标，还包含扩增倍数，扩增前的原子序号和原子坐标
        # self.xyzDict[2][15] = ['Si', '15.896150', '10.830315', '16.041859']
        # self.xyzSuperDict[2][400] = ['Si', 32.34385, 10.830315, -0.40584100000000234, [1, 0, -1], 15, ['Si', '15.896150', '10.830315', '16.041859']]         
        '''
        if self.saveChoose == 'T' :
            with open(self.saveFile,'w') as new_file:
                for i,j in enumerate(superTrajList):
                    new_file.write(j)      
            print("扩增后的输出文件已保存！")
        else :
            print("调用 07方法：对xyz文件进行周期性扩增，注意：07方法 本次运行未保存输出文件！")
        print('第一帧原子数:',superTrajList[0])
        print('总原子数(第一帧原子数*总帧数):',self.xyzDict[1][0]*boxNumber*self.xyzDict[0])
        print("扩增后的盒子三边长度(单位：埃)分别为：",(xp-xn+1)*self.xCell,(yp-yn+1)*self.yCell,(zp-zn+1)*self.zCell)
               
        
    # 10方法：统计轨迹文件中盒子扩增前后某一帧各原子分布，通常用于每一帧的分布情况都相同，同类原子连续分布
    def periodicAtomIndex(self,frameSpecific):            # frameNumber是帧数
        '''
        调用07方法。由于该方法用于统计盒子扩增前后指定帧数的原子序号分布，因此需要调用07方法，并传入该方法需要的一些参数
        该方法只需要求每一帧中同类原子连续分布，不需要每帧原子数相同
        创建了两个非常有用的全局变量，如下所示
        self.KeyValueDict = iFrameAtomIndexCalc(self.xyzDict,self.frameNumber)  # 返回的是一个字典，针对括增前的盒子self.xyzDict进行统计
        self.KeyValueSuperDict = iFrameAtomIndexCalc(self.xyzSuperDict,self.frameNumber) # 针对扩增后的盒子self.xyzSuperDict进行统计        
        
        '''
        self.frameSpecific = frameSpecific                 # 对传入的指定帧数变量进行初始化
        self.periodicBox("1 -1 1 -1 1 -1","F")         # 需要调用07方法，因此要进行初始化，初始化时要进行一些默认参数的设置，第一个参数代表扩增的倍数
        # xyzDictList = list(self.xyzDict[self.frameNumber].keys())  # 扩增前盒子中frameNumber帧数下每一个原子的序号列表
        # 定义子函数dictCounter(),输入一个列表valueList，统计该列表中各元素出现的次数，返回一个字典
        # xyzSuperDictList = [self.xyzSuperDict[self.frameNumber][i][0] for i in range(1,self.xyzSuperDict[self.frameNumber][0]+1)]  # 得到字典中键的元素符号的列表
        # xyzSuperDictKeyDict = dictCounter(xyzSuperDictList) # {'Si': 5832, 'V': 216}
        def iFrameAtomIndexCalc(xyzDict,frameSpecific):
            # 定义子函数，统计valueList中各元素出现的次数
            def dictCounter(valueList):    # 定义子函数，统计valueList中各元素出现的次数
                result_dic={}
                for item_str in valueList:
                    if item_str not in result_dic:
                        result_dic[item_str]=1
                    else:
                        result_dic[item_str]+=1
                # print(result_dic)    
                return result_dic          # 返回统计字典，{'Si': 216, 'V': 8}

            xyzDictList = [xyzDict[frameSpecific][i][0] for i in range(1,xyzDict[frameSpecific][0]+1)]  # 得到对应frameNumber帧中元素符号的列表
            print('该帧中总原子数：',xyzDict[frameSpecific][0])             # 统计该帧中总原子数
            xyzDictKeyDict = dictCounter(xyzDictList)    # 调用上面定义的函数dictCounter统计各元素出现的次数, {'Si': 216, 'V': 8}
            print('--**--**--**--各原子的数量',xyzDictKeyDict)
            atomIndexDict = {}                           # 初始化一个字典，用于储存每个元素的开始和结束编号
            for i in list(xyzDictKeyDict.keys()):        # 遍历每一种元素符号，如，Si，V
                atomIndexDict[i] = []                    # 初始化一个列表，用于储存i元素的编号范围
                tempList = []                            # 初始化一个临时列表，用于储存i元素所有的原子编号
                for j in range(1,xyzDict[frameSpecific][0]+1):         # 遍历第frameNumber帧的键，即原子编号
                    if xyzDict[frameSpecific][j][0] == i:   # 判断对应于编号为j的原子的元素符号是否为元素i
                        tempList.append(j)                # 将原子编号添加到临时列表中
                tempList.sort()                           # 对列表进行从小到大正向排序，返回一个新的列表
                atomIndexDict[i].append(tempList[0])      # 对应i元素序号最小值
                atomIndexDict[i].append(tempList[-1])     # 对应i元素序号最大值
            print('原子序号分布：',atomIndexDict)                          # 在函数内部进行打印，外部调用就不再打印了
            return atomIndexDict                          # 返回统计后得到的字典
        
        print('\n------------盒子周期性扩增前的该帧原子序号分布：')
        iFrameAtomIndexCalc(self.xyzDict,self.frameSpecific)
        print('\n盒子周期性扩增后的该帧原子序号分布，默认扩增倍数为 1 -1 1 -1 1 -1：')
        iFrameAtomIndexCalc(self.xyzSuperDict,self.frameSpecific)
        self.KeyValueDict = iFrameAtomIndexCalc(self.xyzDict,self.frameSpecific)  # 返回的是一个字典，针对括增前的盒子self.xyzDict进行统计
        # self.KeyValueDict = {'Si': [1, 216], 'V': [217, 224]}
        self.KeyValueSuperDict = iFrameAtomIndexCalc(self.xyzSuperDict,self.frameSpecific) # 针对扩增后的盒子self.xyzSuperDict进行统计
        # self.KeyValueSuperDict = {'Si': [1, 5832], 'V': [5833, 6048]}
        
    
    # 08方法：提取特定编号原子周围半径r范围内原子，该方法考虑了周期性，该方法使用了方法7中的全局环境变量
    def periodicExtract(self,rCutoff,atomNumberRange):
        '''
        该方法依赖于方法7 self.periodicBox("1 -1 1 -1 1 -1","F") 中定义的扩增后的原子轨迹字典 self.xyzSuperDict
        该方法中暂未定义可供其他方法使用的有价值的全局变量
        '''
        self.rCutoff = rCutoff
        self.atomNumberRange = atomNumberRange
        self.periodicBox("1 -1 1 -1 1 -1","F")         # 需要调用07方法，因此要进行初始化，初始化时要进行一些默认参数的设置，第一个参数代表扩增的倍数
        # print(type(self.xyzSuperDict[0]),type(self.xyzSuperDict[1][0]),self.xyzSuperDict[1][0])   # 测试用的print
        # print(self.xyzSuperDict[1][1],type(self.xyzSuperDict[1][1][1]))                           # 测试用的print
        finalExtractList = []                          # 构建一个列表，用于储存每一帧中满足截断半径要求的原子轨迹信息
        for i in range(1,self.xyzSuperDict[0] +1):     # 帧数循环
            # print(self.xyzSuperDict[0])
            # print(self.xyzSuperDict[i][0])
            iExtract = 0                               # 该参数用于计数，即每一帧中在截断半径内的原子数量
            newExtractList = []                        # 该列表用于储存每一帧中满足截断半径要求的原子信息，该列表每一帧要重新释放置零并重新赋值
            totalExtractList = []
            for j in range(1,self.xyzSuperDict[i][0]+1):   # 每一帧中的原子循环，self.xyzSuperDict[i][0]代表扩增后盒子轨迹第i帧的原子数
                eName = self.xyzSuperDict[i][j][0]         # 计算第i帧中第j个原子的元素符号和各分坐标
                ex = self.xyzSuperDict[i][j][1]            # 针对每一帧，分别将每个原子与传入的目标原子的距离进行比较
                ey = self.xyzSuperDict[i][j][2]
                ez = self.xyzSuperDict[i][j][3]
                # print(eName,ex,ey,ez)
                for l in self.atomNumberRange:             # self.atomNumberRange是传入的目标原子编号列表，即计算这些原子截断半径范围内的配位原子
                    lName = self.xyzDict[i][l][0]
                    lx = float(self.xyzDict[i][l][1])
                    ly = float(self.xyzDict[i][l][2])
                    lz = float(self.xyzDict[i][l][3])
                    distance = math.sqrt(((ex-lx)**2)+((ey-ly)**2)+((ez-lz)**2))                  # 计算两个原子间的距离
                    # print(distance)
                    # print(lName,lx,ly,lz)
                    if self.rCutoff >= distance:                # 判断距离是否满足截断半径
                        iExtract = iExtract +1                  # 对满足截断半径的原子进行计数
                        newExtractList.append(eName+' '+str(ex)+' '+str(ey)+' '+str(ez)+'\n')     # 将满足要求的原子信息添加到列表中
                        # print(eName,ex,ey,ez)
            totalExtractList.append(str(iExtract)+'\n')         # 每一帧的第一行添加原子数，每一帧循环结束后添加原子数
            totalExtractList.append(self.replace+'\n')          # 每一帧的第二行添加晶格信息参数，每一帧循环结束后添加晶格信息
            finalExtractList = finalExtractList + totalExtractList + newExtractList               # 构建一个集成列表，将每一帧的信息都储存在该列表中
        # for i in finalExtractList:
        #     print(i)  
        with open(self.saveFile,'w') as new_file:               # 将提取出来的每一帧原子坐标写入到文件中
            for i,j in enumerate(finalExtractList):             # 遍历最终集成列表中的每一个元素，将其写入到文件中
                new_file.write(j)      
        print("目标原子局域结构输出文件已保存！")        


    # 14方法：提取特定编号原子周围半径r范围内原子，该方法考虑了周期性，该方法使用了方法7中的全局环境变量
    def RijperiodicExtract(self,result,atomNumberRange):
        '''
        该方法依赖于方法7 self.periodicBox("1 -1 1 -1 1 -1","F") 中定义的扩增后的原子轨迹字典 self.xyzSuperDict
        该方法中暂未定义可供其他方法使用的有价值的全局变量
        '''
        self.result = result   # result = [['Si', 'Si', 'Si'], ['0', 'Si', 'Ca'], [2.5, 3.0, 5.0]]  分别是中心原子，配位原子和截断半径
        self.atomNumberRange = atomNumberRange
        self.periodicBox("1 -1 1 -1 1 -1","F")         # 需要调用07方法，因此要进行初始化，初始化时要进行一些默认参数的设置，第一个参数代表扩增的倍数
        # print(type(self.xyzSuperDict[0]),type(self.xyzSuperDict[1][0]),self.xyzSuperDict[1][0])   # 测试用的print
        # print(self.xyzSuperDict[1][1],type(self.xyzSuperDict[1][1][1]))                           # 测试用的print
        finalExtractList = []                          # 构建一个列表，用于储存每一帧中满足截断半径要求的原子轨迹信息
        for i in range(1,self.xyzSuperDict[0] +1):     # 帧数循环
            # print(self.xyzSuperDict[0])
            # print(self.xyzSuperDict[i][0])
            iExtract = 0                               # 该参数用于计数，即每一帧中在截断半径内的原子数量
            newExtractList = []                        # 该列表用于储存每一帧中满足截断半径要求的原子信息，该列表每一帧要重新释放置零并重新赋值
            totalExtractList = []
            for j in range(1,self.xyzSuperDict[i][0]+1):   # 每一帧中的原子循环，self.xyzSuperDict[i][0]代表扩增后盒子轨迹第i帧的原子数
                eName = self.xyzSuperDict[i][j][0]         # 计算第i帧中第j个原子的元素符号和各分坐标
                ex = self.xyzSuperDict[i][j][1]            # 针对每一帧，分别将每个原子与传入的目标原子的距离进行比较
                ey = self.xyzSuperDict[i][j][2]
                ez = self.xyzSuperDict[i][j][3]
                # print(eName,ex,ey,ez)
                for l in self.atomNumberRange:             # self.atomNumberRange是传入的目标原子编号列表，即计算这些原子截断半径范围内的配位原子
                    lName = self.xyzDict[i][l][0]
                    lx = float(self.xyzDict[i][l][1])
                    ly = float(self.xyzDict[i][l][2])
                    lz = float(self.xyzDict[i][l][3])
                    distance = math.sqrt(((ex-lx)**2)+((ey-ly)**2)+((ez-lz)**2))                  # 计算两个原子间的距离
                    # print(distance)
                    # print(lName,lx,ly,lz)
                    """
                    1.设置原子截断半径的中心原子种类 result[0] 范围要大于等于 编号对应的原子种类 atomNumberRange
                    2.注意编号的中心原子的计算
                    """
                    
                    if lName not in self.result[0]:            # 如果编号对应的中心原子与原子对中的中心原子种类不符合，则中断。
                        print("设置原子对截断半径的中心原子种类 与 输入原子编号对应的中心原子种类不符")
                        print("报错的原子编号以及原子种类为：",l,lName)
                        sys.exit(1)                            # 终止程序，返回退出码 1

                    if eName == lName and distance < 0.01:     # 单位是埃，理论上应该设为0，筛选出编号原子
                        iExtract = iExtract +1                 # 对满足截断半径的原子进行计数
                        newExtractList.append(eName+' '+str(ex)+' '+str(ey)+' '+str(ez)+'\n')     # 将满足要求的原子信息添加到列表中
                        continue                               # 当编号的中心原子和配位原子是同一原子时，跳出本次循环

                    for icount,icenter in enumerate(self.result[0]):                  # 遍历result[0]-result[1]中对应的每一个原子对
                        if icenter == lName and self.result[1][icount] == eName:      # 判断result[0]-result[1] 原子对和 l-j 原子对是否相同
                            if self.result[2][icount] >= distance:               # 判断距离是否满足截断半径
                                iExtract = iExtract +1                           # 对满足截断半径的原子进行计数
                                newExtractList.append(eName+' '+str(ex)+' '+str(ey)+' '+str(ez)+'\n')     # 将满足要求的原子信息添加到列表中
                                # print(eName,ex,ey,ez)
                        # elif icenter == lName and eName == lName:       # 筛选编号原子本身，icenter == lName 保证原子对中心原子和编号中心原子一致。
                        #    if distance < 0.05:                         # 判断配位原子和中心原子是否为同一个原子
                        #        iExtract = iExtract +1                  # 对满足截断半径的原子进行计数
                        #        newExtractList.append(eName+' '+str(ex)+' '+str(ey)+' '+str(ez)+'\n')     # 将满足要求的原子信息添加到列表中

            totalExtractList.append(str(iExtract)+'\n')         # 每一帧的第一行添加原子数，每一帧循环结束后添加原子数
            totalExtractList.append(self.replace+'\n')          # 每一帧的第二行添加晶格信息参数，每一帧循环结束后添加晶格信息
            finalExtractList = finalExtractList + totalExtractList + newExtractList               # 构建一个集成列表，将每一帧的信息都储存在该列表中
        # for i in finalExtractList:
        #     print(i)  
        with open(self.saveFile,'w') as new_file:               # 将提取出来的每一帧原子坐标写入到文件中
            for i,j in enumerate(finalExtractList):             # 遍历最终集成列表中的每一个元素，将其写入到文件中
                new_file.write(j)      
        print("目标原子局域结构输出文件已保存！") 


    # 09方法：计算总的径向分布函数
    def trdfCalc(self,dotNumber,frameFromTo,atomicPair):     # dotNumber是取点数,是一个整数值，frameFromTo是一个帧数范围，如350-500, atomicPair是原子对
        '''
        这个方法调用了07方法，因此需要先对07方法进行传参和初始化
        这个方法还调用了10方法
        '''
        self.periodicBox("1 -1 1 -1 1 -1","F")         # 需要调用07方法，因此要进行初始化，初始化时要进行一些默认参数的设置，第一个参数代表扩增的倍数
        self.periodicAtomIndex(1)                      # 以第一帧的原子序号作为参考，可以使用该方法中的两个变量
        # print(self.KeyValueDict)        # self.KeyValueDict = {'Si': [1, 216], 'V': [217, 224]}
        # print(self.KeyValueSuperDict)   # self.KeyValueSuperDict = {'Si': [1, 5832], 'V': [5833, 6048]}
        self.dotNumber = dotNumber                     # 对取点数进行初始化，取点数会影响到球壳厚度
        
        self.atomInner = atomicPair.split('-')[0]        # 中心原子
        self.atomOutside = atomicPair.split('-')[-1]     # 配位原子
        
        atomInnerFrom = self.KeyValueDict[self.atomInner][0]  # 中心原子开始序号，以第一帧为例，中心原子位于原盒子
        atomInnerTo = self.KeyValueDict[self.atomInner][-1]   # 中心原子结束序号
        
        atomOutsideFrom = self.KeyValueSuperDict[self.atomOutside][0] # 配位原子开始序号，配位原子位于扩增盒子
        atomOutsideTo = self.KeyValueSuperDict[self.atomOutside][-1]  # 配位原子结束序号
        
        if frameFromTo == "allFrame":
            self.frameFrom = 1
            self.frameTo = self.xyzDict[0]
        else:
            self.frameFrom = int(frameFromTo.split('-')[0])
            self.frameTo = int(frameFromTo.split('-')[-1])
        print('计算帧数为:',self.frameFrom,'-',self.frameTo)
        
        # 注意每一层列表的元素个数分别为numberOutside+1, numberMiddle+1, numberInner+1, valueList+1, 具体使用时从索引为1开始用
        def nestedList(numberOutside,numberMiddle,numberInner,valueList):  # 构建4层索引的列表
            outsideList = []
            for i in range(0,numberOutside+1):
                outsideList.append(' ')        # append此处可能不能直接添加空列表
                outsideList[i] = []          # 初始化为列表，下一层才能继续append
                for j in range(0,numberMiddle+1):
                    outsideList[i].append(' ') # 基于上一层初始化的列表，此处继续append
                    outsideList[i][j] = []   # 将同层append的空字符串赋值为列表
                    for k in range(0,numberInner+1):
                        outsideList[i][j].append(' ')
                        outsideList[i][j][k] = []
                        for l in range(0,valueList+1):
                            outsideList[i][j][k].append(' ')
                            outsideList[i][j][k][l] = str(i)+' '+str(j)+' '+str(k)+' '+str(l)
            return outsideList   # 返回构建的4层列表，作用与嵌套字典类似，但是更节省内存

        # 定义子函数dictCounter(),输入一个列表valueList，统计该列表中各元素出现的次数，返回一个字典
        def dictCounter(valueList):    # 定义子函数，统计valueList中各元素出现的次数
            result_dic={}
            for item_str in valueList:
                if item_str not in result_dic:
                    result_dic[item_str]=1
                else:
                    result_dic[item_str]+=1
            # print(result_dic)    
            return result_dic
        
        # 定义子函数listAnalysis，返回一个字典，用于统计分析floatList中在0-delta，delta-2delta，..., (n-1)delta-n*delta中元素的个数
        def listAnalysis(floatList, delta):    # 分析floatList中在0-delta，delta-2delta，..., (n-1)delta-n*delta中元素的个数
            ceilList = [math.ceil(i/delta) for i in floatList ]    # 向下取整，比如 math.ceil(3.5) = 4，相除再向下取整即获得所在区间的序号
            analysisDict = dictCounter(ceilList)                   # 调用上述定义的函数，统计列表中各元素出现的次数，返回一个字典，对每个区间序号出现的次数进行统计
            # floatList.sort()                                     # 从小到大排序
            # nMax = math.ceil(floatList[-1]/delta)                # 向下取整，最大的n
            return analysisDict                                    # 返回一个字典
   

        cellxyzMin = sorted([self.xCell,self.yCell,self.zCell])[0]    # 取盒子长宽高的最小值
        xdelta = cellxyzMin/self.dotNumber             # 计算的球壳厚度，将长度cellxyzMin分为了self.dotNumber份，或者说每一份的宽度
        radiusList = [(i+0.5)*xdelta for i in range(0,self.dotNumber)]  # 径向变量r的列表，相当于每一份终点的坐标
        # radiusList = [ 0.5xdelta, 1.5xdelta, ... , (self.dotNumber-0.5)*xdelta ]
        volDelta = [(4/3*math.pi*((j+xdelta/2)**3-(j-xdelta/2)**3)) for j in radiusList ]  
        # volDelta = [vol_1, vol_2, vol_3, ... , vol_n]
        print(volDelta)
        
        '''
        如下，构建一个初始的超级字典，用于储存原盒子每一帧中每一个原子与对应帧扩增后的盒子中每一个原子之间的距离，二者的坐标，元素种类和序号等等
        超级列表初始化传入的扩增前和扩增后的原子数均是按照第一帧的原子数来计算的，理论上来说初始化的列表是一个每一帧的原子数均相同的列表，但不相同也没有关系
        '''     
        
        # distanceList = nestedList(self.xyzSuperDict[0], self.xyzDict[1][0], self.xyzSuperDict[1][0],6)   # 参数都为数值，每一层的元素个数分别为参数+1，如self.xyzSuperDict[i][0]+1
        distanceDict = {}
        for i in range(self.frameFrom,self.frameTo +1):       # 帧数循环,默认从第一帧开始
            iAtomDensity =  self.xyzDict[i][0]/(self.xCell*self.yCell*self.zCell)         # 第i帧盒子的原子密度
            distanceDict[i] = {}                         # 最1层是帧数
            for k in range(atomInnerFrom,atomInnerTo +1):     # 此处的k是原盒子中每一帧中的每一个原子
                # distanceDict[i][k] = {}  # 第2层的键是第i帧中原盒子中每一个原子序号k，对应值是一个字典
                kjDistance = []
                kName = self.xyzDict[i][k][0]
                kx = float(self.xyzDict[i][k][1])
                ky = float(self.xyzDict[i][k][2])
                kz = float(self.xyzDict[i][k][3])
                # if kName == self.atomInner:          # 筛选中心原子
                for j in range(atomOutsideFrom,atomOutsideTo +1):   # 
                    # distanceDict[i][k][j] = []   # 第三层的键是扩增后第i帧中原盒子中第k个原子与扩增盒子中第j个原子，对应的值是一个列表，列表的第一个值是距离
                    eName = self.xyzSuperDict[i][j][0]
                    ex = self.xyzSuperDict[i][j][1]
                    ey = self.xyzSuperDict[i][j][2]
                    ez = self.xyzSuperDict[i][j][3]
                    # if eName == self.atomOutside:    # 筛选配位原子
                    distance = math.sqrt(((ex-kx)**2)+((ey-ky)**2)+((ez-kz)**2))
                    kjDistance.append(distance)
                kjDict = listAnalysis(kjDistance, xdelta)        # 调用上述定义的函数，统计各个区间的原子数
                # kjDict = {1: 1, 2: 1, 3: 3}
                # print(kjDict)
                kjList = []
                for l in range(1,self.dotNumber+1):
                    if l in list(kjDict.keys()):
                        # print(kjDict[l+1],volDelta[l],iAtomDensity)
                        kjnDensity = kjDict[l]/volDelta[l-1]/iAtomDensity
                    else:
                        kjnDensity = 0
                    kjList.append(kjnDensity) # 分别添加第i帧中第k个原子与所有j原子对在 delta，2delta，... , ndelta上的概率密度
                distanceDict[i][k] = kjList   # 将第i帧中第k个原子的rdf添加为列表，列表为在 delta，2delta，... , ndelta上的概率密度
        # print(distanceDict)
        
        list1 = []
        for l in range(0,self.dotNumber): # 将delta，2delta，... , ndelta上的所有概率密度进行平均
            list2 = []
            for i in range(self.frameFrom,self.frameTo +1):         # 帧数，基于帧数对字典进行查询
                for k in range(atomInnerFrom,atomInnerTo +1):  # 原子数，对内层原子序号进行查询
                    list2.append(distanceDict[i][k][l])   # 先将所有帧所有原子对在同一个序号的 delta上的概率密度添加为一个列表
            average2 = mean(list2)   # 然后进行平均
            list1.append(average2)   # 再将平均后的概率密度添加到一个新的列表
        print(list1)                  # 将最终的列表打印
        # plt.scatter(volDelta[0:50],list1[0:50],s=100)
        nPlotFrom = math.ceil(1.5/xdelta)      # 1.5是指画图
        nPlotTo = math.ceil(5.0/xdelta)
        plt.plot(radiusList[nPlotFrom:nPlotTo],list1[nPlotFrom:nPlotTo],linewidth=0.5) # 绘图，其中radiusList = [ 0.5xdelta, 1.5xdelta, ... , (self.dotNumber-0.5)*xdelta ]
        x_major_locator = MultipleLocator(0.25) # 把x轴的刻度间隔设置为1，并存在变量里
        y_major_locator = MultipleLocator(0.5) # 把y轴的刻度间隔设置为0.5，并存在变量里
        ax= plt.gca() # ax为两条坐标轴的实例
        ax.xaxis.set_major_locator(x_major_locator) #把 x轴的主刻度设置为1的倍数
        ax.yaxis.set_major_locator(y_major_locator)        
        
        plt.grid()
        plt.show()
        for x, y in zip(radiusList[nPlotFrom:nPlotTo], list1[nPlotFrom:nPlotTo]):  # 同时遍历长度相同的两个列表
            print(x,y)


    
    # 02方法：添加晶格信息
    def cellInfoAppend(self):                            # 该方法用于添加盒子信息，适用于单帧或多帧xyz轨迹文件，每一帧中的原子数可不相同
        '''
        此方法新定义了一个有价值的全局变量 self.newTrajList ，使用该变量需要先调用02方法
        self.newTrajList = newTrajList                   # 添加晶格参数后新xyz的列表（供类中所有方法使用的新添加的变量）
        '''
        newTrajList = []
        for i,j in enumerate(self.xyzList):              # enumerate默认从0开始
            #for a,b in enumerate(self.firstLineIndex):
            if i in [a+1 for a in self.firstLineIndex]:           # b+1即cell Information所在行的索引Index
                newTrajList.append(self.replace + "\n")
            else:
                newTrajList.append(j)  
        self.newTrajList = newTrajList                   # 添加晶格参数后新xyz的列表（供类中所有方法使用的新添加的变量）
        with open(self.saveFile,'w') as new_file:
            for i,j in enumerate(newTrajList):
                new_file.write(j)
                
    
    # 03方法：计算每一帧的各原子编号
    def atomIndexCalc(self,frameNo):                      # 可用于计算xyz文件某一帧的各类原子序号(序号从1开始)
        '''
        此方法定义的全局变量来源于方法调用传入的参数
        self.frameNo = frameNo                            # frameNo参数是从实例中传入的，需要初始化，注意该帧数从1开始
        '''
        self.frameNo = frameNo                            # 注意该帧数从1开始
        firstFlameList = self.allFrameDict[self.frameNo][2]   # 
        firFlame = {}                                     # 第一帧轨迹原子的字典，不包括前两行
        firElent = []
        for i,line in enumerate(firstFlameList):
            if i >= 2:
                firFlame[i-1] = line.split( )             # 填充字典
                firElent.append(line.split( )[0])         # 第一帧中各原子化学符号组成的列表
        print(firFlame)
        print(firElent)   #0-223,共224
        print(Counter(firElent))
        totalAtomNo = self.allFrameDict[self.frameNo][1]  # 总原子数
        print("总原子数：",totalAtomNo)
        print(firElent[0],"始于序号：",1)
        for i,j in enumerate(firElent):
            if i <= len(firElent)-2:
                if firElent[i+1] != j:
                    print(j,"结束于:",i+1,"下一个原子",firElent[i+1],"始于序号：",i+2)
        print(firElent[-1],"原子结束于：",totalAtomNo)
    

    # 04方法：该方法用于提取指定帧数范围的xyz文件
    def frameExtract(self,frameRange):                       # 该方法用于提取指定帧数范围的xyz文件
        '''
        self.frameRange = frameRange                         # frameRange参数是从实例中传入的，需要初始化，注意该帧数从1开始
        '''
        self.frameRange = frameRange                         # frameRange参数是从实例中传入的，需要初始化，注意该帧数从1开始
        print("共提取帧数：",len(self.frameRange))             # 计算提取的总帧数
        with open(self.saveFile,'w') as new_file:            # 'w'参数将覆盖之前的同名文件
            for i,j in enumerate(self.frameRange):
                for singleLine in self.allFrameDict[j][2]:   # 访问allFrameDict字典中对应帧数的元素列表，字典中帧数是从1开始的
                    new_file.write(singleLine)               # 将列表中的每一行写入到新的文件中


    # 06方法：提取特定编号原子周围半径r范围内原子，该方法未考虑周期性
    def coorExtract(self,rCutoff,atomNumberRange):  # atomNumberRange为要提取的原子编号列表, rCutoff是原子对截断半径
        self.rCutoff = rCutoff                      # 将子方法中传入的参数初始化为全局变量
        self.atomNumberRange = atomNumberRange
        # self.atomIndexCalc(1)                     # 要访问同个类中的其它方法定义的实例变量，必须先调用该方法，而本例中未调用03方法中定义的全局变量，因此此处不需要调用该方法
        na = self.name                              # 输入文件名
        row_len = self.length                       # 统计xyz文件行数
        x = self.firstline                          # 用第一帧的原子数代表每一帧原子数，即认为每一帧的原子数相同
        y = row_len/int(x+2)                        # 计算帧数
        print("帧数，两种方法分别计算",y,self.frameNumber)        
        numbers = self.atomNumberRange              # 要提取的原子编号列表
        aaa = len(numbers)                          # 列表的元素个数，即目标提取的原子个数
        print("原子个数为： ", aaa )                  # 显示输入的内容        
        rc = self.rCutoff                           # 原子对截断半径        
        name = self.saveFile                        # 注意字符串输入变量的数据类型转换
        dict_r = {}                                 #新建一个字典
        en = []     # 帧数,m1
        el = []     # 通过文本行数来标记原子,n1
        em = []     # 统计总共有多少个原子,uu
        x1 = []     # x分坐标,px
        y1 = []     # y分坐标,py
        z1 = []     # z分坐标,pz        
        pp = 0      # 行数
        uu = 0                          
        with open(na, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    pp += 1                              #行数
                    zhen = math.ceil(pp/(int(x+2)))      #通过行数判断处于哪一帧，floor是向下取整,ceil为向上取整
                    #print("帧数为:",zhen,"文本行数为：",pp)
                    for number in numbers:
                        value = (zhen-1)*(x+2)+int(number)+2
                        #print ("原子编号：", number)
                        #print ("行数为：", value)
                        if pp == value:
                            uu += 1
                            em.append(uu)
                        if pp == value:
                            m1 = zhen       #帧数
                            px = float(line.split( )[1])
                            py = float(line.split( )[2])
                            pz = float(line.split( )[3])
                            en.append(m1)
                            el.append(pp)   #行数
                            x1.append(px)
                            y1.append(py)
                            z1.append(pz)
                            break           # break 打破了最小封闭for或while循环        
        #print("帧数列表：",en)                    
        #print("行数列表：",el)  
        #print("原子数列表：",em)  
        #print("x分坐标列表：",x1)          
        #print("-------------")  
        #接下来这一部分是为了筛选出符合条件的原子坐标
        pp = 0        
        qq = 0        
        dict_r = {}                   #新建一个字典
        with open(na, 'r') as f1:
                lines = f1.readlines()
                for line in lines:
                    pp += 1           #行数
                    zhen = math.ceil(pp/(int(x+2)))      #通过行数判断处于哪一帧，floor是向下取整,ceil为向上取整
                    #print("帧数为:",zhen,"文本行数为：",qq)
                    if (pp != (int(x+2)*(zhen-1)+1)) and (pp != (int(x+2)*(zhen-1)+2))  :
                        px = float(line.split( )[1])
                        py = float(line.split( )[2])
                        pz = float(line.split( )[3])
                        ts = aaa*(zhen-1)+1   #定位列表相应元素位置
                        te = aaa*zhen
                        i = ts
                        #print("列表原子数的检索范围：",ts,"——",te,"此时i:",i)
                        while i >= ts and i <= te:
                            distance = math.sqrt( ((px-x1[i-1])**2)+((py-y1[i-1])**2)+((pz-z1[i-1])**2) )
                            #print("分坐标x1[i-1],y1[i-1],z1[i-1]分别为： ", x1[i-1],y1[i-1],z1[i-1])
                            #print("实际距离是 ",distance) 
                            if rc >= distance:
                                #print("文本行数pp满足条件，行数为： ", pp) 
                                qq += 1
                                break # break 打破了最小封闭for或while循环。
                            i += 1                        
                    if pp == (int(x+2)*(zhen-1)+x+2) :    #通过行数判断是否到了每一帧的最后一行
                        #print("正在写入键:",zhen,"值为：",qq)
                        number = zhen              #记下帧数
                        element = qq
                        dict_r[number] = element
                        #print("---------------")
                        qq = 0 
        #print("每一帧符合条件的原子数 ", dict_r)           # 显示输入的内容
        #sys.exit(404)
        pp = 0     #行数          
        mm = 0         
        with open(name, 'w') as new_file:
            with open(na, 'r') as v:
                lines = v.readlines()
                for line in lines:
                    pp += 1           #行数
                    zhen = math.ceil(pp/(int(x+2)))      #判断处于哪一帧，floor是向下取整
                    if pp == (int(x+2)*(zhen-1)+1) :    #通过行数判断是否到了新一帧
                        mm += 1
                        new_file.write(str(dict_r[mm])+ '\n')
                        #print("开始写入主表头",str(dict_r[mm]))
                    if pp == (int(x+2)*(zhen-1)+2) :
                        new_file.write('This is number:'+ str(mm)+'\n')
                        #print("开始写入次表头",'This is number:'+ str(mm))
                    if pp != (int(x+2)*(zhen-1)+1) and pp != (int(x+2)*(zhen-1)+2)  :
                        px = float(line.split( )[1])
                        py = float(line.split( )[2])
                        pz = float(line.split( )[3])
                        ts = aaa*(zhen-1)+1   #定位列表相应元素位置
                        te = aaa*zhen
                        i = ts
                        #print("---------------")
                        while i >= ts and i <= te:
                            distance = math.sqrt( ((px-x1[i-1])**2)+((py-y1[i-1])**2)+((pz-z1[i-1])**2) )
                            #print("实际距离是 ",distance) 
                            if rc >= distance:
                                #print("文本行数pp满足条件，行数为： ", pp) 
                                qq += 1
                                #print("开始写入筛选行",line)
                                new_file.write(line)                        
                                break # break 打破了最小封闭for或while循环。
                            i += 1  #没找到需要继续循环        
        print("每一帧符合条件的原子数 ", dict_r)           # 显示输入的内容
        print("任务完成!")
        print("---------------")  
    

    
    # 01-1方法    
    def findRep(self):       # 该方法返回一个带有晶格参数的新的xyz文件,添加盒子信息后的xyz轨迹文件可用于plumed分析。
                             # 该方法适用于多帧，非单帧，且每一帧的原子数必须相等，原文件中每一帧的第二行必须一样
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
                atomIndex.append(i)   
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

    

    # 01-2方法
    def firstFrame(self):    # 该方法调用了findRep(self)函数
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


# 02类，处理数据txt文件，用于绘图
# 02类，包含05方法
"""
这段代码定义了一个名为txtPlot的类，用于从txt文件中提取数据并存储到字典中。在类的初始化函数中，输入文件名、起始行数和存储文件名等参数，
然后通过open函数读取文件内容，将每一行数据存储到一个列表中。接着，通过split函数将每一行数据按照空格分隔开来，判断数据列数。然后，遍历所有行，
将每一列数据存储到一个字典中，字典的键为列数，值为该列的所有数据。最后，将每列数据存储为列表，作为列数字典的值，列数从1开始。
这个类的实例化对象可以通过调用columnDict属性来获取提取的数据 
"""
class txtPlot():
    def __init__(self,fileName,nStart,saveTxt):  # 默认 nStart = 2，代表起始行数
        '''
        self.fileName = fileName                   # txt输入文件名
        self.nStart = nStart                       # 定义起始的行数，一般为2，第1行一般为标题，nStart从1开始计数,是一个数字  
        self.saveTxt = saveTxt                     # 将用于存储提取的数据的文件命名
                
        self.txtList = lines                       # txt数据文件所有行写成一个列表，包括表头
        self.columnTotal = columnTotal             # 列数
        self.columnDict = columnDict               # 将每列数据存储为字典，列数从1开始
        self.rowTotal = len(self.columnDict[1])    # 键为数字1，即数据第1列的行数(认为第1列的行数代表数据总行数)
        
        '''
        self.fileName = fileName                       # txt输入文件名
        self.nStart = nStart                           # 定义起始的行数，一般为2，第1行一般为标题，nStart从1开始计数,是一个数字  
        self.saveTxt = saveTxt                         # 将用于存储提取的数据的文件命名       
        
        columnDict = {}                                # 将各列数据写进字典，列数从1开始
        with open(self.fileName, 'r') as f:
            lines = f.readlines()
            self.txtList = lines                       # txt数据文件所有行写成一个列表，包括表头
            columnTotal = self.txtList[self.nStart-1].split( )      # 默认多个空格作为分隔符，起始行为第2行，对应的索引为1，判断数据列数
            # print("第一行数据",columnTotal)
            self.columnTotal = len(columnTotal)        # 列数总和,即计算起始行数的列数，基于文本第二行数的数据
            # columnIni = 1                            # 将列数的起始值设为1
            for i in range(1,self.columnTotal+1):      # 遍历所有列数，每一列数据都初始化为一个空列表，列数序号从1开始
                columnDict[i] = []
            # print("列数据字典初始化",columnDict)
            for i,j in enumerate(self.txtList):        # 遍历所有的行
                if i >= self.nStart-1:                 # 行数减去1即为索引index，从数据行的索引开始
                    for m,n in enumerate(j.split( )):  # 遍历每一行中的所有列
                        columnDict[m+1].append(float(n))            # 注意列表循环添加数据的方式没有等号，不是 columnDict[m+1] = columnDict[m+1].append(n)
            # print('实例化后的列数据字典',columnDict)
        self.columnDict = columnDict                   # 将每列数据存储为列表，作为列数字典的值，列数从1开始
        self.rowTotal = len(self.columnDict[1])        # 键为数字1，即数据第1列的行数(认为第1列的行数代表数据总行数)
        # print(self.columnDict[1],self.rowTotal)
            
    # 05 方法
    def tempPot(self):
        # print("数据文件表头：",self.txtList[0])
        x1 = self.columnDict[1]                 # 字典中键为1的数据列表，Step
        x2 = self.columnDict[2]                 # 字典中键为2的数据列表，Time
        y2 = self.columnDict[4]                 # Temp
        y3 = self.columnDict[5]                 # Pot
        print(x2)        
        plt.figure(num=3, figsize=(8, 5))       #创建figure窗口，figsize设置窗口的大小 
        #画曲线1
        plt.subplot(211)                        # 子图绘制，两行一列第一个图     
        plt.plot(x1,y2,color='red')             # Temp[K]        
        max1 = np.max(y2)                       # 最大值
        min1 = np.min(y2)                       # 最小值        
        #设置坐标轴范围
        plt.xlim(0, x1[-1])                     # x轴范围
        plt.ylim(min1-1000,max1+500)            # y轴范围        
        #设置坐标轴名称
        plt.xlabel("Step")                      #Step Nr.
        plt.ylabel("Temp[K]")                   #Temp[K]

        #画曲线2
        plt.subplot(212)  
        plt.plot(x2,y3,color='blue', linewidth=1.0, linestyle='-') #Pot.[a.u.]       
        #设置坐标轴范围
        plt.xlim(0, x2[-1])                     # x轴范围
        #mean1 = np.mean(y3)                    # 平均值
        max1 = np.max(y3)                       # 最大值
        min1 = np.min(y3)                       # 最小值
        plt.ylim(min1-1,max1+1)       
        #设置坐标轴名称
        plt.xlabel("Time")                      # Time[fs]
        plt.ylabel("Pot.[a.u.]")                # Temp[K]       
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
        
        print("请问是否要保存图片,输入1保存,输入2不保存:")     # 提示命令行输入
        x = int(input())                        # 注意字符串输入变量的数据类型转换
        if x == 1:
            plt.savefig('time-temp')
            print("图片已保存")        
        plt.show()
    
    # 12方法，提示自选两列绘图
    """
    这段代码是一个绘图函数，它会提示用户输入两列数据，然后将这两列数据绘制成一张图。其中，第一列数据将作为横坐标，第二列数据将作为纵坐标。
    绘图完成后，程序会提示用户是否保存图片，如果用户输入1，则程序会将图片保存到当前目录下，并输出“图片已保存”。最后，程序会显示绘制的图形 
    """
    def colvarPot(self):
        # print("数据文件表头：",self.txtList[0])
        print('请依次输入需要绘图的两列数据，列数从1开始计数，只允许输入两个整数，用英文逗号隔开，如：1,2')
        coulmList = input().split(',')
        x1 = self.columnDict[int(coulmList[0])]                 # 对应横坐标数据
        # x2 = self.columnDict[2]                 # 字典中键为2的数据列表，Time
        y2 = self.columnDict[int(coulmList[1])]                 # 对应纵坐标数据
        # y3 = self.columnDict[5]                 # Pot
        #print(x2)        
        plt.figure(num=3, figsize=(8, 5))       #创建figure窗口，figsize设置窗口的大小 
        #画曲线1
        # plt.subplot(111)                        # 子图绘制，两行一列第一个图     
        plt.plot(x1,y2,color='red')             # Temp[K]        
        max1 = np.max(y2)                       # 最大值
        min1 = np.min(y2)                       # 最小值        
        #设置坐标轴范围
        plt.xlim(0, x1[-1])                     # x轴范围
        plt.ylim(min1,max1)            # y轴范围        
        #设置坐标轴名称
        plt.xlabel("x")                      #Step Nr.
        plt.ylabel("y")                   #Temp[K]
               
        print("请问是否要保存图片,输入1保存,输入2不保存:")     # 提示命令行输入
        x = int(input())                        # 注意字符串输入变量的数据类型转换
        if x == 1:
            plt.savefig('time-temp')
            print("图片已保存")        
        plt.show()    
        

# 01函数
"""
注释：用于获取当前目录下的文件名。函数会先询问用户是否需要通过GUI获取文件路径，如果需要则打开文件选择对话框，
否则直接输出当前目录下的所有文件名并要求用户输入需要处理的文件名。最后返回用户输入的文件名
"""
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
    
# 01常数，相对原子质量的字典常数
'''
atomicMassSingleDict 是一个相对原子质量的字典
'''
atomicMassSingleDict = {'H': ['1', 'Hydrogen', 'H', '1.00794', '1', '1'], 'He': ['2', 'Helium', 'He', '4.002602', '18', '1'], 'Li': ['3', 'Lithium', 'Li', '6.941', '1', '2'], 'Be': ['4', 'Beryllium', 'Be', '9.012182', '2', '2'], 'B': ['5', 'Boron', 'B', '10.811', '13', '2'], 'C': ['6', 'Carbon', 'C', '12.0107', '14', '2'], 'N': ['7', 'Nitrogen', 'N', '14.0067', '15', '2'], 'O': ['8', 'Oxygen', 'O', '15.9994', '16', '2'], 'F': ['9', 'Fluorine', 'F', '18.9984032', '17', '2'], 'Ne': ['10', 'Neon', 'Ne', '20.1797', '18', '2'], 'Na': ['11', 'Sodium', 'Na', '22.98976928', '1', '3'], 'Mg': ['12', 'Magnesium', 'Mg', '24.3050', '2', '3'], 'Al': ['13', 'Aluminium', 'Al', '26.9815386', '13', '3'], 'Si': ['14', 'Silicon', 'Si', '28.0855', '14', '3'], 'P': ['15', 'Phosphorus', 'P', '30.973762', '15', '3'], 'S': ['16', 'Sulfur', 'S', '32.065', '16', '3'], 'Cl': ['17', 'Chlorine', 'Cl', '35.453', '17', '3'], 'Ar': ['18', 'Argon', 'Ar', '39.948', '18', '3'], 'K': ['19', 'Potassium', 'K', '39.0983', '1', '4'], 'Ca': ['20', 'Calcium', 'Ca', '40.078', '2', '4'], 'Sc': ['21', 'Scandium', 'Sc', '44.955912', '3', '4'], 'Ti': ['22', 'Titanium', 'Ti', '47.867', '4', '4'], 'V': ['23', 'Vanadium', 'V', '50.9415', '5', '4'], 'Cr': ['24', 'Chromium', 'Cr', '51.9961', '6', '4'], 'Mn': ['25', 'Manganese', 'Mn', '54.938045', '7', '4'], 'Fe': ['26', 'Iron', 'Fe', '55.845', '8', '4'], 'Co': ['27', 'Cobalt', 'Co', '58.933195', '9', '4'], 'Ni': ['28', 'Nickel', 'Ni', '58.6934', '10', '4'], 'Cu': ['29', 'Copper', 'Cu', '63.546', '11', '4'], 'Zn': ['30', 'Zinc', 'Zn', '65.409', '12', '4'], 'Ga': ['31', 'Gallium', 'Ga', '69.723', '13', '4'], 'Ge': ['32', 'Germanium', 'Ge', '72.64', '14', '4'], 'As': ['33', 'Arsenic', 'As', '74.92160', '15', '4'], 'Se': ['34', 'Selenium', 'Se', '78.96', '16', '4'], 'Br': ['35', 'Bromine', 'Br', '79.904', '17', '4'], 'Kr': ['36', 'Krypton', 'Kr', '83.798', '18', '4'], 'Rb': ['37', 'Rubidium', 'Rb', '85.4678', '1', '5'], 'Sr': ['38', 'Strontium', 'Sr', '87.62', '2', '5'], 'Y': ['39', 'Yttrium', 'Y', '88.90585', '3', '5'], 'Zr': ['40', 'Zirconium', 'Zr', '91.224', '4', '5'], 'Nb': ['41', 'Niobium', 'Nb', '92.90638', '5', '5'], 'Mo': ['42', 'Molybdenum', 'Mo', '95.94', '6', '5'], 'Tc': ['43', 'Technetium', 'Tc', '98', '7', '5'], 'Ru': ['44', 'Ruthenium', 'Ru', '101.07', '8', '5'], 'Rh': ['45', 'Rhodium', 'Rh', '102.905', '9', '5'], 'Pd': ['46', 'Palladium', 'Pd', '106.42', '10', '5'], 'Ag': ['47', 'Silver', 'Ag', '107.8682', '11', '5'], 'Cd': ['48', 'Cadmium', 'Cd', '112.411', '12', '5'], 'In': ['49', 'Indium', 'In', '114.818', '13', '5'], 'Sn': ['50', 'Tin', 'Sn', '118.710', '14', '5'], 'Sb': ['51', 'Antimony', 'Sb', '121.760', '15', '5'], 'Te': ['52', 'Tellurium', 'Te', '127.60', '16', '5'], 'I': ['53', 'Iodine', 'I', '126.904', '47', '17', '5'], 'Xe': ['54', 'Xenon', 'Xe', '131.293', '18', '5'], 'Cs': ['55', 'Caesium', 'Cs', '132.9054519', '1', '6'], 'Ba': ['56', 'Barium', 'Ba', '137.327', '2', '6'], 'La': ['57', 'Lanthanum', 'La', '138.90547', 'n/a', '6'], 'Ce': ['58', 'Cerium', 'Ce', '140.116', 'n/a', '6'], 'Pr': ['59', 'Praseodymium', 'Pr', '140.90765', 'n/a', '6'], 'Nd': ['60', 'Neodymium', 'Nd', '144.242', 'n/a', '6'], 'Pm': ['61', 'Promethium', 'Pm', '145', 'n/a', '6'], 'Sm': ['62', 'Samarium', 'Sm', '150.36', 'n/a', '6'], 'Eu': ['63', 'Europium', 'Eu', '151.964', 'n/a', '6'], 'Gd': ['64', 'Gadolinium', 'Gd', '157.25', 'n/a', '6'], 'Tb': ['65', 'Terbium', 'Tb', '158.92535', 'n/a', '6'], 'Dy': ['66', 'Dysprosium', 'Dy', '162.500', 'n/a', '6'], 'Ho': ['67', 'Holmium', 'Ho', '164.930', '32', 'n/a', '6'], 'Er': ['68', 'Erbium', 'Er', '167.259', 'n/a', '6'], 'Tm': ['69', 'Thulium', 'Tm', '168.93421', 'n/a', '6'], 'Yb': ['70', 'Ytterbium', 'Yb', '173.04', 'n/a', '6'], 'Lu': ['71', 'Lutetium', 'Lu', '174.967', '3', '6'], 'Hf': ['72', 'Hafnium', 'Hf', '178.49', '4', '6'], 'Ta': ['73', 'Tantalum', 'Ta', '180.94788', '5', '6'], 'W': ['74', 'Tungsten', 'W', '183.84', '6', '6'], 'Re': ['75', 'Rhenium', 'Re', '186.207', '7', '6'], 'Os': ['76', 'Osmium', 'Os', '190.23', '8', '6'], 'Ir': ['77', 'Iridium', 'Ir', '192.217', '9', '6'], 'Pt': ['78', 'Platinum', 'Pt', '195.084', '10', '6'], 'Au': ['79', 'Gold', 'Au', '196.966569', '11', '6'], 'Hg': ['80', 'Mercury', 'Hg', '200.59', '12', '6'], 'Tl': ['81', 'Thallium', 'Tl', '204.3833', '13', '6'], 'Pb': ['82', 'Lead', 'Pb', '207.2', '14', '6'], 'Bi': ['83', 'Bismuth', 'Bi', '208.98040', '15', '6'], 'Po': ['84', 'Polonium', 'Po', '210', '16', '6'], 'At': ['85', 'Astatine', 'At', '210', '17', '6'], 'Rn': ['86', 'Radon', 'Rn', '220', '18', '6'], 'Fr': ['87', 'Francium', 'Fr', '223', '1', '7'], 'Ra': ['88', 'Radium', 'Ra', '226', '2', '7'], 'Ac': ['89', 'Actinium', 'Ac', '227', 'n/a', '7'], 'Th': ['90', 'Thorium', 'Th', '232.03806', 'n/a', '7'], 'Pa': ['91', 'Protactinium', 'Pa', '231.03588', 'n/a', '7'], 'U': ['92', 'Uranium', 'U', '238.02891', 'n/a', '7'], 'Np': ['93', 'Neptunium', 'Np', '237', 'n/a', '7'], 'Pu': ['94', 'Plutonium', 'Pu', '244', 'n/a', '7'], 'Am': ['95', 'Americium', 'Am', '243', 'n/a', '7'], 'Cm': ['96', 'Curium', 'Cm', '247', 'n/a', '7'], 'Bk': ['97', 'Berkelium', 'Bk', '247', 'n/a', '7'], 'Cf': ['98', 'Californium', 'Cf', '251', 'n/a', '7'], 'Es': ['99', 'Einsteinium', 'Es', '252', 'n/a', '7'], 'Fm': ['100', 'Fermium', 'Fm', '257', 'n/a', '7'], 'Md': ['101', 'Mendelevium', 'Md', '258', 'n/a', '7'], 'No': ['102', 'Nobelium', 'No', '259', 'n/a', '7'], 'Lr': ['103', 'Lawrencium', 'Lr', '262', '3', '7'], 'Rf': ['104', 'Rutherfordium', 'Rf', '261', '4', '7'], 'Db': ['105', 'Dubnium', 'Db', '262', '5', '7'], 'Sg': ['106', 'Seaborgium', 'Sg', '266', '6', '7'], 'Bh': ['107', 'Bohrium', 'Bh', '264', '7', '7'], 'Hs': ['108', 'Hassium', 'Hs', '277', '8', '7'], 'Mt': ['109', 'Meitnerium', 'Mt', '268', '9', '7'], 'Ds': ['110', 'Darmstadtium', 'Ds', '271', '10', '7'], 'Rg': ['111', 'Roentgenium', 'Rg', '272', '11', '7'], 'Uub': ['112', 'Ununbium', 'Uub', '285', '12', '7'], 'Uut': ['113', 'Ununtrium', 'Uut', '284', '13', '7'], 'Uuq': ['114', 'Ununquadium', 'Uuq', '289', '14', '7'], 'Uup': ['115', 'Ununpentium', 'Uup', '288', '15', '7'], 'Uuh': ['116', 'Ununhexium', 'Uuh', '292', '16', '7'], 'Uuo': ['118', 'Ununoctium', 'Uuo', '294', '18', '7']}



if __name__ == '__main__':
    print('''
  本脚本的功能如下:
      01: 添加盒子信息到多帧xyz文件并输出各类原子范围。输入的xyz文件主要是基于VMD周期性处理过的，输出适用于plumed软件分析的xyz轨迹文件（依赖于其他方法）
      02: 添加盒子信息，针对单帧/多帧xyz轨迹文件，且每一帧的原子数可以不相同（不依赖于其他方法）
      03: 计算xyz轨迹文件某一帧的原子序号分布（不依赖于其他方法）,主要是用于辅助plumed输入文件编写
      04: 提取xyz轨迹文件某些范围帧数，如 1,3,5-10,30,每帧原子数可不同
      05: cp2k输出的ener文件温度、势能随步数绘图，标准ener文件格式即可
      06: 提取多帧xyz文件特定编号原子周围半径r范围内的原子[未考虑周期性]
      07: 对xyz轨迹文件进行周期性扩增
      08: 提取多帧xyz文件特定编号原子周围半径r范围内的原子[考虑周期性]，功能 06升级版
      09: 计算总的径向分布函数TRDF
      10: 返回xyz轨迹文件盒子周期性扩增前后某一帧的原子序号分布（依赖于07方法，需要每一帧中同类原子连续分布）
      11: xyz文件某一帧转data文件，data文件可用于lammps经典分子动力学模拟
      12: colvar数据文件等绘图（自选列数），标准colvar文件格式即可
      13: 计算xyz文件所有帧中某个原子到某个平面的距离，平面由三个原子的序号确定
      14: 基于不同原子对的截断半径Rij，提取多帧xyz文件特定编号原子周围半径Rij范围内的配位原子[考虑周期性]，功能 08升级版
      
      -1: 测试
           
          ''')
    print("请选择功能，输入Enter默认为-1测试")     # 提示选择功能
    defChoose = input()
    
    if defChoose == '' :                       # 将Enter快捷键默认值设为-1
        defChoose = "-1"
        
    if defChoose == "-1":
        cellInfo = "16.4477 16.4477 16.4477"   # 该参数为类默认值，对test该方法无意义
        cellName = "6868.xyz"                  # 该参数为类默认值，对test该方法无意义
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)        
        xyzFile1.test()


    elif defChoose == "01":
        # xyzFile1 = Xyz('50_SiV(0-500).xyz','16.4477 16.4477 16.4477','1.xyz')
        # xyzFile1.findRep()
        print("请输出需要添加的晶格信息，输入Enter默认为16.4477 16.4477 16.4477")     # 提示命令行输入
        cellInfo = input()              # 注意字符串输入变量的数据类型转换
        if cellInfo == '' :
            cellInfo = "16.4477 16.4477 16.4477"  # 设置输入Enter时候的默认值
            print("采用默认 16.4477 16.4477 16.4477")
        print("请为添加晶格信息后的xyz文件重新命名，输入Enter默认为 01_cellInfoPlus.xyz")     # 提示命令行输入
        cellName = input()              # 注意字符串输入变量的数据类型转换
        if cellName == '' :
            cellName = "01_cellInfoPlus.xyz"       # 设置输入Enter时默认的输出文件名
            print("采用默认 01_cellInfoPlus.xyz ")  
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化
        xyzFile1.firstFrame()
              
        
    elif defChoose == "02":
        print("请输出需要添加的晶格信息，输入Enter默认为16.4477 16.4477 16.4477")     # 提示命令行输入
        cellInfo = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellInfo == '' :
            cellInfo = "16.4477 16.4477 16.4477"                                # 设置输入Enter时候的晶格常数默认值
            print("采用默认 16.4477 16.4477 16.4477")
        print("请为添加晶格信息后的xyz文件重新命名，输入Enter默认为 01_cellInfoPlus.xyz")                        # 提示命令行输入
        cellName = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellName == '' :
            cellName = "01_cellInfoPlus.xyz"                                    # 设置输入Enter时默认的输出文件名
            print("采用默认 01_cellInfoPlus.xyz ")          
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化
        xyzFile1.cellInfoAppend()
        

    elif defChoose == "03":
        cellInfo = "16.4477 16.4477 16.4477"                                    # 该参数为类默认值，对该方法无意义
        cellName = "01_cellInfoPlus.xyz"                                        # 该参数为类默认值，对该方法无意义
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化
        print("请输入想要进行原子序号分布分析的帧数n，帧数从1开始，输入Enter默认为分析第1帧")
        frameNo = input()                                                       # n是指帧数，从1开始
        if frameNo == '':
            n = 1
        else :
            n = int(frameNo)                                                
        xyzFile1.atomIndexCalc(n)                                               # n是方法中的形参，调用时需要传入该参数
        
    
    elif defChoose == "04":
        cellInfo = "16.4477 16.4477 16.4477"                                    # 该参数为类默认值，对该方法无意义
        print("请为提取帧数组成的新xyz文件命名，输入Enter默认为 02_trajExtra_python47.xyz")                        # 提示命令行输入
        cellName = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellName == '' :
            cellName = "02_trajExtra_python47.xyz"                                   # 设置输入Enter时默认的输出文件名
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化
        # def __init__(self,name,replace,saveFile):
        print("请输入想要提取的帧数范围，如 1,3,5-10,30，帧数从1开始，用英文逗号隔开")
        # inputSplit("1,3,5-10,55-58")
        frameRange = inputSplit(input())                                        # inputSplit是调用上述定义的第二个函数 
        xyzFile1.frameExtract(frameRange)


    elif defChoose == "05":
        # class txtPlot():
        # def __init__(self,fileName,nStart,saveTxt,separator):
        nStart = 2        # 数据起始行的行数，一般从第2行开始
        print("请为绘图数据的txt文件命名，输入Enter默认为 03_dataPlot_python47.txt")                        # 提示命令行输入
        saveTxt = input()                                                       # 注意字符串输入变量的数据类型转换
        if saveTxt == '' :
            saveTxt = "03_dataPlot_python47.txt"     
        xyzFile1 = txtPlot(inputFunction(),nStart,saveTxt)
        xyzFile1.tempPot()

        
    elif defChoose == "06":
        cellInfo = "16.4477 16.4477 16.4477"                                    # 该参数为类默认值，对该方法无意义
        print("请为提取原子组成的新xyz文件命名，输入Enter默认为 06_rCutoff_python47.xyz")                        # 提示命令行输入
        cellName = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellName == '' :
            cellName = "06_rCutoff_python47.xyz"              
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # cellName是为输出文件命名
        xyzFile1.atomIndexCalc(1)                                               # 调用03方法计算第1帧中的原子序号分布，此处atomIndexCalc方法中的frameNo参数为1
        print("上述为调用03方法计算第1帧中原子序号分布，接下来为06方法")
        print("设置原子对的截断半径，输入Enter默认为 3 埃")                          # 提示命令行输入
        r = input()                                                             # 注意字符串输入变量的数据类型转换
        if r == '' :
            rCutoff = 3
        else:
            rCutoff = float(r)                                                   
        print("请输入想要提取的原子编号范围，如 217-224 ，原子编号从1开始，用英文逗号隔开")
        # inputSplit("1,3,5-10,55-58")
        atomNumberRange = inputSplit(input())   # input()函数返回的是一个字符串
        # 注意此处的rCutoff是一个浮点型数值，并非字符串,atomNumberRange是一个类似于[5, 6, 7, 8, 9, 10]的数字列表
        xyzFile1.coorExtract(rCutoff,atomNumberRange)


    elif defChoose == "07":
        print("请输出需要添加的晶格信息，输入Enter默认为 16.4477 16.4477 16.4477 ,采用空格分隔")     # 提示命令行输入
        cellInfo = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellInfo == '' :
            cellInfo = "16.4477 16.4477 16.4477"                                # 设置输入Enter时候的晶格常数默认值
            print("采用默认 16.4477 16.4477 16.4477")
        print("请为周期性扩增后的xyz文件重新命名，输入Enter默认为 07_boxMultiple.xyz,输入 f 或 F 即不保存文件")                        # 提示命令行输入
        cellName = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellName == '' :
            cellName = "07_boxMultiple.xyz"                                    # 设置输入Enter时默认的输出文件名
            print("采用默认 07_boxMultiple.xyz ")    
            saveChoose = "T"                                                   # saveChoose参数用于判断是否保存扩增后的文件，否则仅为全局变量
        elif cellName == 'f'or 'F':
            saveChoose = "F"
        else :
            saveChoose = "T"
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化        
        print("请输入盒子括增的倍数，输入格式为 xp xn yp yn zp zn, 用空格隔开， Enter默认为xyz方向各扩增1倍，即 1 -1 1 -1 1 -1")     # 提示命令行输入
        print('''
        1 -1 1 -1 1 -1 代表xyz方向均扩增一倍，即xyz方向均有3个盒子，共计27个盒子
        0 0 0 0 0 0 代表xyz方向均未扩增的原胞
        1 0 1 0 1 0 代表仅在 x+ y+ z+ 方向扩增一倍
        1 -1 1 -1 0 0 代表仅在 x+ x- y+ y- z z 方向扩增一倍
        1 0 0 0 0 0 代表仅在 x+ 方向扩增一倍
        10 -10 10 -10 10 -10 代表仅在 x+ x- y+ y- z+ z- 方向均扩增10倍
        5 -5 5 -5 5 -5 代表仅在 x+ x- y+ y- z+ z- 方向均扩增5倍 '''      )
        
        multiInfo = input()                                                      # 注意字符串输入变量的数据类型转换
        if multiInfo == '' :
            multiInfo = "1  -1  1  -1  1  -1"                                # 设置输入Enter时候的晶格常数默认值
            print("默认 xp xn yp yn zp zn 采用 1 -1  1 -1 1 -1 ")        
        
        xyzFile1.periodicBox(multiInfo,saveChoose)                           # saveChoose参数用于判断是否保存括增后的xyz文件，取值为“F”或“T”
    
    elif defChoose == "08":
        print("请输出需要添加的晶格信息，输入Enter默认为 16.4477 16.4477 16.4477 ,采用空格分隔")     # 提示命令行输入
        cellInfo = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellInfo == '' :
            cellInfo = "16.4477 16.4477 16.4477"                                # 设置输入Enter时候的晶格常数默认值
            print("采用默认 16.4477 16.4477 16.4477")
        print("请为提取后的xyz文件重新命名，输入Enter默认为 08_atomsExtract_PBC.xyz")                        # 提示命令行输入
        cellName = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellName == '' :
            cellName = "08_atomsExtract.xyz"                                    # 设置输入Enter时默认的输出文件名
            print("采用默认 08_atomsExtract.xyz ")    
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化        
        xyzFile1.atomIndexCalc(1)                                               # 调用03方法计算第1帧中的原子序号分布，此处atomIndexCalc方法中的frameNo参数为1
        print("上述为调用03方法计算第1帧中原子序号分布，接下来为08方法")
        print("设置原子对的截断半径，输入Enter默认为 3 Å")                          # 提示命令行输入
        r = input()                                                             # 注意字符串输入变量的数据类型转换
        if r == '' :
            rCutoff = 3
        else:
            rCutoff = float(r)                                                   
        print("请输入想要提取的原子编号范围，如 217-224 ，原子编号从1开始，用英文逗号隔开")
        # inputSplit("1,3,5-10,55-58")
        atomNumberRange = inputSplit(input())   # input()函数返回的是一个字符串
        # 注意此处的rCutoff是一个浮点型数值，并非字符串,atomNumberRange是一个类似于[5, 6, 7, 8, 9, 10]的数字列表    
        xyzFile1.periodicExtract(rCutoff,atomNumberRange)   # 注意此处的rCutoff是一个浮点型数值，并非字符串,atomNumberRange是一个类似于[5, 6, 7, 8, 9, 10]的数字列表


    elif defChoose == "09":          # 计算总的径向分布函数，即不区分原子种类
        print("请输出需要添加的晶格信息，输入Enter默认为 16.4477 16.4477 16.4477 ,采用空格分隔")     # 提示命令行输入
        cellInfo = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellInfo == '' :
            cellInfo = "16.4477 16.4477 16.4477"                                # 设置输入Enter时候的晶格常数默认值
            print("采用默认 16.4477 16.4477 16.4477")
        print("请为rdf数据文本命名，输入Enter默认为 09_rdfData.txt")                        # 提示命令行输入
        cellName = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellName == '' :
            cellName = "09_rdfData.txt"                                    # 设置输入Enter时默认的输出文件名
            print("采用默认 09_rdfData.txt ")    
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化        
      
        print("请输入帧数范围，如 350-500，输入Enter默认为所有帧, 若只计算第n帧，则输入 n-n ")
        frameFromTo = input()                                                      # 注意字符串输入变量的数据类型转换
        if frameFromTo == '' :
            frameFromTo = "allFrame"                                    # 设置输入Enter时默认的输出文件名
            # print("采用默认 09_rdfData.txt ")        
        print("请输入原子对，如 V-Si")
        atomicPair = input()                                                      # 注意字符串输入变量的数据类型转换
        print("设置取点数目n，输入Enter默认为 n = 300 ")                          # 提示命令行输入
        n = input()                                                             # 注意字符串输入变量的数据类型转换
        if n == '' :
            n = 300
        else:
            n = int(n)                                                   
        
        xyzFile1.trdfCalc(n,frameFromTo,atomicPair)
        
    elif defChoose == "10":                        # 方法10用于统计xyz文件中各类原子的序号分布，也可计算盒子扩增后的原子序号分布
        print("请输出需要添加的晶格信息，输入Enter默认为 16.4477 16.4477 16.4477 ,采用空格分隔")     # 提示命令行输入
        cellInfo = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellInfo == '' :
            cellInfo = "16.4477 16.4477 16.4477"                                # 设置输入Enter时候的晶格常数默认值
            print("采用默认 16.4477 16.4477 16.4477")
        # 由于该方法后续还会用于分析扩增后盒子中的原子序号分布，所以传入准确的盒子信息是非常必要的
        cellName = "10_cellInfoPlus.xyz"                                        # 该参数为类默认值，对该方法无意义
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化
        print("请输入想要进行原子序号分布分析的帧数n，帧数从1开始，输入Enter默认为分析第1帧")
        frameNo = input()                                                       # n是指帧数，从1开始
        if frameNo == '':
            n = 1
        else :
            n = int(frameNo)                                                
        xyzFile1.periodicAtomIndex(n)                                           # n是方法中的形参，调用时需要传入该参数

    elif defChoose == "11":                        # 方法11用于将多帧xyz文件中的某一帧转化为data文件
        print("请输出需要添加的晶格信息，格式如：16.4477 16.4477 16.4477 ,采用空格分隔")
        cellInfo = input()
        print("请为转换得到的data文件命名，输入Enter默认为 11_xyzToData.data")       # 提示命令行输入
        saveFile = input()                         
        if saveFile == '' :
            saveFile = "11_xyzToData.data"                                      # 设置输入Enter时默认的输出文件名
            print("采用默认 11_xyzToData.data ")  
        xyzFile1 = Xyz(inputFunction(),cellInfo,saveFile)                       # 对方法进行实例化
        print("请输入想要进行原子序号分布分析的帧数n，帧数从1开始，输入Enter默认为分析第1帧")
        xyzFrame = input()                                                      # n是指帧数，从1开始
        if xyzFrame == '':
            xyzFrame = 1
        else :
            xyzFrame = int(xyzFrame)         
        xyzFile1.periodicAtomIndex(xyzFrame)                                    # 调用方法10，统计xyz文件中的原子类型
        print("请输入想要采用的原子顺序，用英文逗号隔开，如: Si,B,Ca,O")
        atomOrder = input() 
        xyzFile1.xyzToData(atomOrder,xyzFrame)                                  # 调用方法11，传入原子顺序和指定帧两个参数

    elif defChoose == "12":
        # class txtPlot():
        # def __init__(self,fileName,nStart,saveTxt,separator):
        # 提示用户输入行数 nStart
        user_input = input("请输入数据的起始行数（按Enter键使用默认值2），行数从1开始计数：")
        # 如果用户输入了内容，将其作为行数；否则使用默认值2
        nStart = int(user_input) if user_input else 2
        # 在这里添加你的处理逻辑
        print("起始行数：", nStart)
        # nStart = 2        # 数据起始行的行数，一般从第2行开始
        print("请为绘图数据的txt文件命名，输入Enter默认为 12_dataPlot_python47.txt")                        # 提示命令行输入
        saveTxt = input()                                                       # 注意字符串输入变量的数据类型转换
        if saveTxt == '' :
            saveTxt = "12_dataPlot_python47.txt"     
        xyzFile1 = txtPlot(inputFunction(),nStart,saveTxt)
        xyzFile1.colvarPot()

    elif defChoose == "13":   # 方法用于计算每一帧中特定原子到特定3个原子组成的平面间的距离。
        cellInfo = "16.4477 16.4477 16.4477" 
        print("默认输出的文件名为：distance.txt")
        saveFile = "distance.txt"
        xyzFile1 = Xyz(inputFunction(),cellInfo,saveFile) 
        print("请依次输入确定平面的三个原子序号和平面外的原子序号，用英文逗号隔开，如：1,2,3,10")
        disIndex = input()
        xyzFile1.pointToPlaneDistance(disIndex,saveFile)
        
        
    elif defChoose == "14":
        print("请输出需要添加的晶格信息，输入Enter默认为 16.4477 16.4477 16.4477 ,采用空格分隔")     # 提示命令行输入
        cellInfo = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellInfo == '' :
            cellInfo = "16.4477 16.4477 16.4477"                                # 设置输入Enter时候的晶格常数默认值
            print("采用默认 16.4477 16.4477 16.4477")
        print("请为提取后的xyz文件重新命名，输入Enter默认为 08_atomsExtract_PBC.xyz")                        # 提示命令行输入
        cellName = input()                                                      # 注意字符串输入变量的数据类型转换
        if cellName == '' :
            cellName = "14_atomsExtract.xyz"                                    # 设置输入Enter时默认的输出文件名
            print("采用默认 14_atomsExtract.xyz ")    
        xyzFile1 = Xyz(inputFunction(),cellInfo,cellName)                       # 对类进行实例化        
        xyzFile1.atomIndexCalc(1)                                               # 调用03方法计算第1帧中的原子序号分布，此处atomIndexCalc方法中的frameNo参数为1
        print("上述为调用03方法计算第1帧中原子序号分布，接下来为08方法")
        print("设置原子对的截断半径，输入Enter默认为 3 Å")                          # 提示命令行输入
        
        """
        r = input()                                                             # 注意字符串输入变量的数据类型转换
        if r == '' :
            rCutoff = 3
        else:
            rCutoff = float(r)                         
        """
        
        # 从用户输入的字符串中提取周期性结构的化学符号和数字，将它们分别存储在不同的列表中，并将这三个列表组合成一个列表。
        input_str = input("请按中心原子、配位原子、截断半径的顺序输入字符串（以空格分隔，符号和数字总数必须是3的整数倍），如 Si O 2.5 Si Si 3.0 Si Ca 5.0 "+"\n")
        # 检查输入字符串的符号和数字总数是否是3的整数倍
        tokens = input_str.split()
        if len(tokens) % 3 != 0:
            print("输入格式错误！符号和数字总数必须是3的整数倍。")
        else:
            symbols_1 = []
            symbols_2 = []
            numbers = []
        
            for i in range(0, len(tokens), 3):
                symbols_1.append(tokens[i])
                symbols_2.append(tokens[i+1])
                numbers.append(float(tokens[i+2]))
        
            result = [symbols_1, symbols_2, numbers]   # [['Si', 'Si', 'Si'], ['0', 'Si', 'Ca'], [2.5, 3.0, 5.0]]
            
            # 打印 symbols_1 中的字符串种类数
            unique_symbols_1 = set(symbols_1)
            num_unique_symbols_1 = len(unique_symbols_1)
            print("中心原子种类数：", num_unique_symbols_1)
            # 检查 symbols_2 中是否有重复的字符串
            if len(symbols_2) != len(set(symbols_2)):
                print("配原子种类有重复！配位原子重复时，中心原子不能重复。")
                print("中心原子、配位原子和截断半径：",result)
                # sys.exit(1)                            # 终止程序，返回退出码 1
            else:
                print("中心原子、配位原子和截断半径：",result)

        print("请输入想要提取的中心原子编号范围，如 1,2,217-224,300 ，原子编号从1开始，用英文逗号隔开")
        # inputSplit("1,3,5-10,55-58")
        atomNumberRange = inputSplit(input())   # input()函数返回的是一个字符串
        # 注意此处的rCutoff是一个浮点型数值，并非字符串,atomNumberRange是一个类似于[5, 6, 7, 8, 9, 10]的数字列表    
        xyzFile1.RijperiodicExtract(result,atomNumberRange)   # 注意此处的rCutoff是一个浮点型数值，并非字符串,atomNumberRange是一个类似于[5, 6, 7, 8, 9, 10]的数字列表

        
    else:
        print("提示：您选择的功能正在开发，请重新选择！")
        

timeEnd = datetime.datetime.now()          # 显示时间 
timeDuration = timeEnd - timeStart  
print('''
-----------------------------
该任务执行完毕，祝您工作顺利!\n任务总耗时：
''',timeDuration)
