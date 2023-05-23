# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:26:46 2022

@author: sun78
"""
'''
类的哲学是面向对象编程，选择合适的对象是核心
'''

import json
import sys

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
from collections import Counter

class potential():
    def __init__(self,filenameDB):  # 注意是__是双下划线
        self.filenameDB = filenameDB # 势函数数据库文件名
        
        
    # 01函数，将数据从json文件读取到内存中
    def loadData(self,filename):                                # 将数据从json文件读取到内存中
        '''
        self.allData = allData        # 设置全局变量，json数据库中的所有数据
        '''
        self.filename = filename
        print('|----------------------------------------调用函数：loadData')
        with open(self.filename,'r') as f:              # r 以只读方式打开文件。
            allData = json.load(f)
        print('读取的json文件: ',self.filename,'从json文件中读取到内存的数据: ',allData,'\n')
        print('读取的json文件: ',self.filename,'从json文件中读取到内存的字典键',sorted(list(allData.keys())),'\n')   # 注意是字典形式
        self.allData = allData        # 设置全局变量，json数据库中的所有数据
        return allData                             # 返回被加载的数据，注意返回的数据格式，可能是字典或者列表
    
    
    # 02函数，将数据写入到json文件中，数据可以是字典
    def dumpData(self,dumpFile,writenData):                      # 将数据从内存写入到json文件中，会覆盖原有文件内容,传入的数据是需要写入的数据
        self.dumpFile = dumpFile
        self.writenData = writenData
        print('|----------------------------------------调用函数：dumpData')
        jsonData = self.writenData
        # filename = '38_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json'
        with open(self.dumpFile,'w') as f:              # w 打开一个文件只用于写入。如果该文件已存在则覆盖。如果该文件不存在，创建新文件。。
            json.dump(jsonData,f)
        print('内存写入到json文件中的数据: ',jsonData)    # 文件的内容起始就是jsonData的内容，一摸一样

    # 03函数，将原子电荷信息添加到json数据库中
    def modifyDB(self):
        '''
        需要用到 self.allData 全局变量
        '''
        self.loadData(self.filenameDB)       # 要访问同个类中的其它方法定义的实例变量，必须先调用该方法。
        print('数据库中关于原子电荷信息的内容：',self.allData['charge'])
        print('请依次输入需要添加的原子及相应电荷，用英文逗号隔开，如：O,-0.945,Si,1.89 ，否则报错')
        chemKeyValue = input().split(',')
        if len(chemKeyValue)%2 != 0:
            print('输入的语法错误，请重新输入！')
            sys.exit('404')   
        for i in range(0,len(chemKeyValue),2):
            if chemKeyValue[i] in list(self.allData['charge'].keys()):
                print('!!!!!!!!!!!!警告：数据库中已经存在该原子: ',i,'程序会覆盖该原子已有的电荷信息!!!!!!!!!!!!\n')  
            print('添加的新的原子电荷信息',chemKeyValue[i],chemKeyValue[i+1])
            # print(chemDenDict[chemKeyValue[i]])
            self.allData['charge'][chemKeyValue[i]] = chemKeyValue[i+1]
        
        print('修改后的数据库原子电荷内容：',self.allData['charge'])
        print('是否需要将修改后的数据库字典进行保存？Enter键为保存，F或f为不保存。')
        saveChose = input()
        if saveChose == '':
            self.dumpData(self.filenameDB,self.allData)   # 存为json文件
            print('默认保存的文件为原文件，文件名：', self.filenameDB,'存储方式为覆盖保存')
        else:
            print('修改后的数据未保存！')
        # O,-0.945,Si,1.89,B,1.4175,Ca,0.945,Na,0.4725,Ti,1.89,Al,1.4175,Fe3+,1.4175,Fe2+,0.945,Mg,0.945,K,0.4725
        
    # 04函数，添加原子间相互作用参数
    def interatomicPotential(self):
        '''
        需要用到 self.allData 全局变量
        '''
        self.loadData(self.filenameDB)       # 要访问同个类中的其它方法定义的实例变量，必须先调用该方法。
        print('数据库中关于原子势参数信息的内容：',self.allData['parameter'])
        print('请依次输入需要添加的原子对（用-分隔）及相应势参数，用英文逗号隔开，如：O-O,1.1,2.2,3.3，否则报错。')
        chemKeyValue = input().split(',')   # 用逗号或空格分隔，根据文献来确定 (',') ，根据需要来确定，也可以使用空格分隔
        if len(chemKeyValue)%2 != 0:
            print('输入的语法错误，请重新输入！')
            sys.exit('404')   
        for i in range(0,len(chemKeyValue),4):
            atompairList = chemKeyValue[i].split('-') # Si-O   用'-'分隔
            atomCenter = atompairList[0]   # Si
            atomCoord = atompairList[1]    # O
            if atomCenter + atomCoord in list(self.allData['parameter'].keys()):
                print('!!!!!!!!!!!!警告：数据库中已经存在该原子: ',i,'程序会覆盖该原子已有的势参数信息!!!!!!!!!!!!\n')  
            elif atomCoord + atomCenter in list(self.allData['parameter'].keys()):
                print('!!!!!!!!!!!!警告：数据库中已经存在该原子: ',i,'程序会覆盖该原子已有的势参数信息!!!!!!!!!!!!\n') 
            print('添加的新的原子电荷信息',chemKeyValue[i],chemKeyValue[i+1],chemKeyValue[i+2],chemKeyValue[i+3])
            # print(chemDenDict[chemKeyValue[i]])
            self.allData['parameter'][chemKeyValue[i]] = chemKeyValue[i+1:i+4]
        
        print('修改后的数据库原子势参数内容：',self.allData['parameter'])
        print('是否需要将修改后的数据库字典进行保存？Enter键为保存，F或f为不保存。')
        saveChose = input()
        if saveChose == '':
            self.dumpData(self.filenameDB,self.allData)   # 另存为json文件
            print('默认保存的文件为原文件，文件名：', self.filenameDB,'存储方式为覆盖保存')
        else:
            print('修改后的数据未保存！')
        
    # 05函数，查看数据库内容
    def seeDatabase(self):
        self.loadData(self.filenameDB)       # 要访问同个类中的其它方法定义的实例变量，必须先调用该方法。需要用到其输出的self.allData全局变量
        if 'charge' and 'parameter' in list(self.allData.keys()):  # 针对势参数数据库的查看方法
            print('数据库中具有原子电荷信息的原子种类：',list(self.allData['charge'].keys()))
            print(' ')
            print('数据库中关于原子电荷信息的内容：',self.allData['charge'])
            print(' ')
            print('数据库中具有原子势参数信息的原子对：',list(self.allData['parameter'].keys()))
            print(' ')
            print('数据库中关于原子势参数信息的内容：',self.allData['parameter'])
        
        
    # 06函数，基于势参数数据库输入in文件
    def buckCoul(self):         # 针对buckCoul势函数的势参数输出模板
        self.seeDatabase()
        self.loadData(self.filenameDB)       # 要访问同个类中的其它方法定义的实例变量,self.allData全局变量
        print('输入想要采用的原子顺序，需要与data文件中的一致，用英文逗号隔开，如: Si,B,Ca,O 网络形成体在前，然后是碱金属原子，最后是O原子')
        atomOrderList = input().split(',')
        # potenDict = {}      # 储存势参数的字典
        paraList = []    # 临时列表
        paraInital = 'pair_coeff   *  *  0.00000000 1.000 0.00000000 # others'
        paraList.append(paraInital)
        for i in range(1,len(atomOrderList)+1):
            for j in range(1,len(atomOrderList)+1):
                if j >= i:  # i-j原子对中，j大于等于i时写入
                    # potenKey = str(i)+'-'+str(j)   # 1-2
                    atomi = atomOrderList[i-1]     # Si
                    atomj = atomOrderList[j-1]     # O
                    atomi_j = atomi+'-'+atomj      # Si-O
                    atomj_i = atomj+'-'+atomi      # O-Si
                    if atomi_j in list(self.allData['parameter'].keys()):  # 判断Si-O是否在列表中
                        tempParaList = self.allData['parameter'][atomi_j]  # 势参数值是列表
                        tempStr = 'pair_coeff'+ '   ' + str(i)+'  '+str(j)+ '  '+tempParaList[0]+ '  '+tempParaList[1]+ '  '+tempParaList[2]+'  # '+ atomi_j 
                        print('势参数数据库存在该原子对势参数',atomi_j)
                    elif atomj_i in list(self.allData['parameter'].keys()):  # 判断O-Si是否在列表中
                        tempParaList = self.allData['parameter'][atomj_i]  # 势参数值是列表
                        tempStr = 'pair_coeff'+ '   ' + str(i)+'  '+str(j)+ '  '+tempParaList[0]+ '  '+tempParaList[1]+ '  '+tempParaList[2]+'  # '+ atomj_i +' ' +str(j)+'-'+str(i) 
                        print('势参数数据库存在该原子对势参数',atomj_i)
                    else:
                        tempStr = ''
                        print('势参数数据库中不存在：',atomi_j,'或',atomj_i,'原子对的势参数')
                    
                    if len(tempStr) != 0:
                        paraList.append(tempStr)
        # 下面是为了输出原子类型的序号以及原子电荷
        chargeList = []             # set type 1 charge 1.89 # Si
        groupList = []              # group Si type 1
        for i in range(1,len(atomOrderList)+1):
            atomi = atomOrderList[i-1]     # Si
            charge = self.allData['charge'][atomi]
            chargeSet = 'set type '+ str(i) + ' charge ' + charge + '  # '+ atomi # set type 1 charge 1.89 # Si
            groupSet = 'group '+ atomi + ' type '+ str(i)   # group Si type 1
            chargeList.append(chargeSet)
            groupList.append(groupSet)

        print('\n')
        for i in chargeList:
            print(i)
        print('  ')
        for i in groupList:
            print(i)
        print('  ')
        for i in paraList:
            print(i)
        


# F01函数，选择输入文件，F代表基础函数
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
        
        
        

if __name__ == '__main__':
    print('''
  本脚本的功能如下:
      01: 创建json势参数数据库文件，初始内容为 {"charge": {}, "parameter": {}}
      02: 添加势函数原子电荷信息到数据库文件中
      03: 添加势函数原子对势参数信息到数据库文件中
      04: 查看势参数数据库内容，满足所有json格式数据库的查看
      05: 输出控制lammps运行的in文件(目前主要为元素相互作用势参数部分)
      
      -1: 测试
           
          ''')
    print("请选择功能，输入Enter默认为-1测试")     # 提示选择功能
    defChoose = input()
    
    if defChoose == '' :                       # 将Enter快捷键默认值设为-1
        defChoose = "-1"
        
    if defChoose == "-1":
        print("提示：您选择的功能正在开发，请重新选择！")
        
    elif defChoose == "01":  # 创建json格式文件
        filenameDB = '50_[类-势函数数据库]基于势函数数据库导出lammps运行控制in文件.json' # 默认的势函数文件
        infile = potential(filenameDB)  # 实例化
        print('请为你想要创建的json文件命名，.json格式，Enter采用默认文件名: 50_[类-势函数数据库-空白]基于势函数数据库导出lammps运行控制in文件.json')
        print('数据库初始内容为 {"charge": {}, "parameter": {}}')
        jsonName = input()       # 输入势参数文件名，Enter代表默认的文件名，也可以自定义文件名
        if jsonName == '' :
            jsonName = filenameDB           
        writenData = {}
        writenData["charge"] = {}
        writenData["parameter"] = {}
        infile.dumpData(jsonName,writenData)   # 默认创建一个为空的json文件
        
    elif defChoose == "02":  # 添加原子电荷信息
        filenameDB = '50_[类-势函数数据库]基于势函数数据库导出lammps运行控制in文件.json' # 默认的势函数文件
        print('默认编辑的文件为：',filenameDB)
        infile = potential(filenameDB)       # 实例化
        infile.modifyDB()                    # 对应于03函数

    elif defChoose == "03":  # 添加势参数信息
        filenameDB = '50_[类-势函数数据库]基于势函数数据库导出lammps运行控制in文件.json' # 默认的势函数文件
        print('默认编辑的文件为：',filenameDB)
        infile = potential(filenameDB)       # 实例化
        infile.interatomicPotential()                    # 对应于03函数

    elif defChoose == "04":  # 查看json格式数据库内容
        print('请选择数据库，可以是所有json格式的数据库。')
        filenameDB = inputFunction()
        infile = potential(filenameDB)  # 实例化
        infile.seeDatabase()
        

    elif defChoose == "05":  # 输出in文件
        print('请选择数据库,提示：应选择势函数数据库。')
        filenameDB = inputFunction()
        print('已选择势参数数据库：',filenameDB)
        infile = potential(filenameDB)  # 实例化
        infile.buckCoul()   # 针对buckCoul势函数的势参数输出模板，针对不同的势函数，要写不同的运行方法

    else:
        print("提示：您选择的功能正在开发，请重新选择！")








