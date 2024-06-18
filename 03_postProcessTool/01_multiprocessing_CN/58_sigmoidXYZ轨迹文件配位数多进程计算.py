# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:00:42 2024

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
import multiprocessing
from piecewiseCalc import inputFunction, inputSplit, sigmoid_coordination_mtd, process_sigmoid_frame, atomIndexCalc, periodicBox, xyzImportFile


if __name__ == '__main__':

    print("请输出需要添加的晶格信息，输入Enter默认为 16.4477 16.4477 16.4477 ,采用空格分隔")     # 提示命令行输入
    cellInfo = input()                                                      # 注意字符串输入变量的数据类型转换
    if cellInfo == '' :
        cellInfo = "16.4477 16.4477 16.4477"                                # 设置输入Enter时候的晶格常数默认值
        print("采用默认 16.4477 16.4477 16.4477")
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print("请为提取的数据文件命名，输入Enter默认为 15_coordination_sigmoid.txt")                        # 提示命令行输入
    cellName = input()                                                      # 注意字符串输入变量的数据类型转换
    if cellName == '' :
        cellName = "15_coordination_sigmoid_" + timestamp + ".txt"                                # 设置输入Enter时默认的输出文件名
        print("采用默认 15_coordination_sigmoid.txt ")    
    
    xyzFile = xyzImportFile(inputFunction(),cellInfo,cellName)                       # 对类进行实例化        
    # return [[xCell,yCell,zCell],frameNumber,xyzDict,allFrameDict]
    # xCell = xyzFile[0][0]
    cellList = xyzFile[0]
    print("盒子边长分别为：", cellList)
    frameNo = 1
    allFrameDict = xyzFile[3]
    atomIndexCalc(frameNo, allFrameDict)
    # xyzFile1.atomIndexCalc(1)                                               # 调用03方法计算第1帧中的原子序号分布，此处atomIndexCalc方法中的frameNo参数为1
    print("上述为调用03方法计算第1帧中原子序号分布，接下来为08方法")
    print("设置原子对的截断半径，输入Enter默认为 3 Å")                          # 提示命令行输入
    
    
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
    # xyzFile1.piecewise_func_coordination(result,atomNumberRange)   # 注意此处的rCutoff是一个浮点型数值，并非字符串,atomNumberRange是一个类似于[5, 6, 7, 8, 9, 10]的数字列表
    # xyzFile1.multiprocessing_piecewise_coord(result,atomNumberRange)
        
    # 17方法：基于多进程加速，分段函数实时计算每一帧中指定原子对的配位数，该方法考虑了周期性，该方法使用了方法7中的全局环境变量，该方法在方法16： piecewise_func_coordination 基础上进行修改
    # def multiprocessing_piecewise_coord(self,result,atomNumberRange):


    # atPairCut_Result = self.result
    # grandxyzDict = self.xyzSuperDict
    # prexyzDict = self.xyzDict
    # inputCenterAtomRange = self.atomNumberRange


    
    multiple = "1 -1 1 -1 1 -1"
    saveChoose = "F"
    frameNumber = xyzFile[1]
    replace = cellInfo             # 盒子边长
    xyzDict = xyzFile[2]
    xyzCellList = xyzFile[0]
    xyzSuperDict = periodicBox(multiple,saveChoose,frameNumber,replace,xyzDict,xyzCellList)
    # return xyzSuperDict


    # Prompt the user to input p and q values separated by a space
    user_input = input("Please enter the values for NN and ND separated by a space: ")
    # Split the input string into a list where the first element is p and the second is q
    NN, ND = map(float, user_input.split())


    # self.result = result   # result = [['Si', 'Si', 'Si'], ['0', 'Si', 'Ca'], [2.5, 3.0, 5.0]]  分别是中心原子，配位原子和截断半径
    # self.atomNumberRange = atomNumberRange         # 中心原子列表 [5, 6, 7, 8, 9, 10]
    # self.periodicBox("1 -1 1 -1 1 -1","F")         # 需要调用07方法，因此要进行初始化，初始化时要进行一些默认参数的设置，第一个参数代表扩增的倍数

    totalFrameNumber = xyzSuperDict[0]              # 总帧数
    fourFramDvid = int(xyzSuperDict[0]/5)      # 总帧数分成4部分
    # (1,self.xyzSuperDict[0]), (self.xyzSuperDict[0],2*self.xyzSuperDict[0]), (2*self.xyzSuperDict[0],3*self.xyzSuperDict[0]), (3*self.xyzSuperDict[0],self.xyzSuperDict[0] +1)
    
    # 创建一个Manager字典，用于进程间通信
    manager = multiprocessing.Manager()
    result_dict = manager.dict()
    
    # 创建进程池
    pool = multiprocessing.Pool(processes=5)

    # 准备输入数据
    inputs = [[1,fourFramDvid], [fourFramDvid,2*fourFramDvid], [2*fourFramDvid,3*fourFramDvid], [3*fourFramDvid,4*fourFramDvid], [4*fourFramDvid,totalFrameNumber+1]]

    # 启动多进程
    # def process_piecewise_frame(frameNumberList, atPairCut_Result, prexyzDict, grandxyzDict, inputCenterAtomRange, result_dict):
    for input in inputs:
        # pool.apply_async(process_piecewise_frame, args=(input,result,xyzDict,xyzSuperDict,atomNumberRange,result_dict))
        # def process_sigmoid_frame(frameNumberList, atPairCut_Result, prexyzDict, grandxyzDict, inputCenterAtomRange, cellLength, NN, ND, result_dict):
        pool.apply_async(process_sigmoid_frame, args=(input,result,xyzDict,xyzSuperDict,atomNumberRange,cellList, NN, ND,result_dict))

    # 关闭进程池，等待所有进程完成
    pool.close()
    pool.join()


    # rij_coord_outputDict = result_dict
    rij_coord_outputDict = {key: result_dict[key] for key in sorted(result_dict)}                     # 对字典按照帧数排序
    print("汇总后的字典",result_dict)
    coordination_output_List = []
    atomPairList = list(rij_coord_outputDict[1].keys())
    print("原子对顺序列表：", atomPairList)
    aveCoordDict = {i:[] for i in atomPairList}                                                       # 初始化一个字典，将原子对初始化为键，值是空的列表
    print("原子对截断半径 R_0：", result)
    for frame, atomPairsDict in rij_coord_outputDict.items():
        output_info = str(frame)+ "   "
        for i in  atomPairList:
            output_info = output_info + str(atomPairsDict[i]["perFrameAverageCN"]) + "   "
            aveCoordDict[i].append(float(atomPairsDict[i]["perFrameAverageCN"]))                      # 将每一帧中相应原子对的配位数追加到相应列表中
        output_info = output_info + '\n'
        coordination_output_List.append(output_info)
    # print(aveCoordDict)
    average_values = {key: sum(value) / len(value) for key, value in aveCoordDict.items() if value}   # 计算各原子对的配位数平均值
    print("各原子对的配位数平均值", average_values)                                                      # 打印各原子对配位数平均值 
    frameNoDict = {key: len(value) for key, value in aveCoordDict.items() if value}                   # 计算帧数，避免多进程遗漏数据
    print("各原子对帧数: ", frameNoDict)                                                                # 打印各原子对帧数
    print("NN和ND: ",NN,ND)
    with open(cellName,'w') as new_file:                            # 将提取出来的每一帧原子坐标写入到文件中
        for i,j in enumerate(coordination_output_List):             # 遍历最终集成列表中的每一个元素，将其写入到文件中
            new_file.write(j)  





# 15方法：基于logistic曲线（sigmoid函数）实时计算每一帧中指定原子对的配位数，该方法考虑了周期性，该方法使用了方法7中的全局环境变量，该方法在方法14：RijperiodicExtract(self,result,atomNumberRange)基础上进行修改

    
    

                
                
                
                
                
