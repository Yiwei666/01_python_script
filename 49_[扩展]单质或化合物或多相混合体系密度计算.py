# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:05:48 2022

@author: sun78
"""
import math
import sys
import json


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

'''
05 调用05函数strToDict()，提示输入偶数个字符串，然后返回字典形式
10 调用10函数atomMakeupDict()，判断组元是否在化合物原子组成json数据库中，返回更新后的化合物组成字典,以及所有输入的化合物分子式列表，二者位于一个列表中
    01 在10函数atomMakeupDict()内部调用 01函数 loadData，将数据从json文件读取到内存中
    03 在10函数atomMakeupDict()内部调用 03函数 chemicalsSplit，获取分子式的原子组成，返回一个分子的组成字典
    02 在10函数atomMakeupDict()内部调用 02函数 dumpData，将数据写入到json文件中，数据可以是字典
04 调用04函数 moleMassCalc()计算输入的所有化合物的相对分子质量
08 调用08函数 whetherInDatabase()判断输入的组元是否都存在于密度数据库中（单质或化合物数据库），对于不在的提示基于factsage计算密度或手动录入密度
    09 在08函数内部调用09函数 ChemDensityCalc()，基于factsage计算化合物密度
        04 在09函数内部调用 04函数 moleMassCalc()计算输入的所有化合物的相对分子质量
    11 在08函数内部调用11函数 molDensityInput()，手动录入化合物密度字典   
06 调用06函数 densityMixCalc()，用于计算多组元混合体系的密度
07 调用07函数factDensityCalc()，基于factsage计算混合密度
'''



# 01函数，将数据从json文件读取到内存中
def loadData(filename):                                # 将数据从json文件读取到内存中
    '''
    filename形参是需要加载的json文件名，loadData自定义函数并未调用其他函数
    '''
    print('|----------------------------------------调用函数：loadData')
    # filename = '38_[扩展-1化合物密度数据库]单质或化合物或多相混合体系密度计算.json' # 对应本脚本的数据库文件名字
    with open(filename,'r') as f:              # r 以只读方式打开文件。
        allData = json.load(f)
    print('读取的json文件: ',filename,'从json文件中读取到内存的数据: ',allData,'\n')
    print('读取的json文件: ',filename,'从json文件中读取到内存的字典键',sorted(list(allData.keys())),'\n')   # 注意是字典形式
    print('从json文件中读取到内存的字典键的总数为：',len(list(allData.keys())),'\n')
    return allData                             # 返回被加载的数据，注意返回的数据格式，可能是字典或者列表


# 02函数，将数据写入到json文件中，数据可以是字典
def dumpData(filename,writenData):                      # 将数据从内存写入到json文件中，会覆盖原有文件内容,传入的数据是需要写入的数据
    '''
    filename形参是写入参数的文件名
    writenData 是传入的需要写进json文件中的数据，每次写入json文件内容都会被覆盖
    dumpData自定义函数并未调用其他函数
    '''
    print('|----------------------------------------调用函数：dumpData')
    jsonData = writenData
    # filename = '38_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json'
    with open(filename,'w') as f:              # w 打开一个文件只用于写入。如果该文件已存在则覆盖。如果该文件不存在，创建新文件。。
        json.dump(jsonData,f)
    print('内存写入到json文件中的数据: ',jsonData)    # 文件的内容起始就是jsonData的内容，一摸一样
    if isinstance(jsonData,dict):  # isinstance函数用于判断数据类型
        print('写入的键的总数为: ', len(list(jsonData.keys())))
    else:
        print('写入到json中的数据类型不是字典类型！')    
    


# 03函数，获取分子式的原子组成，返回一个分子的组成字典
def chemicalsSplit(missMoleList):   # 传入需要添加化合物组成的列表，chemString = 'Si-1-O-2,Ca-1-O-1,B-2-O-3'
    '''
    missMoleList形参是一个分子式列表，该函数会提示输入这些分子式的详细原子组成，如 Si-1-O-2,Ca-1-O-1
    chemicalsSplit自定义函数并未调用其他函数，会返回一个或多个分子式的原子组成字典，类似于 {'MoO2': {'Mo': '1', 'O': '2', 'total': 3}}
    '''
    print('|----------------------------------------调用函数：chemicalsSplit')
    print('-----部分化合物组元不在原子组成数据库内，请为以下化合物添加原子组成-----：',missMoleList)
    print('请输入需要转换成字典的组分化学式，按照如下格式: Si-1-O-2,Ca-1-O-1,B-2-O-3 ,分子式用逗号隔开，元素用-隔开,可同时输入多个化合物原子组成。')
    compString = input()
    compList = compString.split(',')
    chemDict = {}
    for mol in compList:        # mol =  'Si-2-O-1'
        molList = mol.split('-') # 用-分隔
        molFormula = ''
        oddList = []            # 计算原子数的列表
        for i,j in enumerate(molList):
            if (i%2) != 0:       # 第一个说明为奇数索引
                oddList.append(int(j))   # (i%2)不等于0说明索引为奇数，对应的为偶数位置，是原子数量
                if int(j) == 1: # 判断是否为1
                    temp = ''
                else:
                    temp = j
            else:               # (i%2)为0时，i全为偶数，对应奇数位置，元素符号
                temp = j
            molFormula = molFormula + temp
        # print('化合物的化学式：',molFormula)
        chemDict[molFormula] = {}
        
        for k in range(0,int(len(molList)/2)):
            keyEle = molList[k*2]  # ['Si','1','O','2']
            valueEle = molList[k*2+1]
            chemDict[molFormula][keyEle] = valueEle
        chemDict[molFormula]['total'] = str(sum(oddList))    # 注意此处要将数值型变量转化为字符串变量，否则调用json.dump()函数会报错
    print('------化合物分子式的原子组成字典------：',chemDict)   # chemDict = {'SiO2': {'Si': '1', 'O': '2', 'total': 3}, 'CaO': {'Ca': '1', 'O': '1', 'total': 2}, 'B2O3': {'B': '2', 'O': '3', 'total': 5}}
    return chemDict                                    # 返回的字典是一个分子式的原子组成字典


"""
To convert atomic number to atomic symbol. 
numberToSymbolDict is greatly not recommended to be modified.
"""
# numberToSymbolDict = {'1': 'H', '2': 'He', '3': 'Li', '4': 'Be', '5': 'B', '6': 'C', '7': 'N', '8': 'O', '9': 'F', '10': 'Ne', '11': 'Na', '12': 'Mg', '13': 'Al', '14': 'Si', '15': 'P', '16': 'S', '17': 'Cl', '18': 'Ar', '19': 'K', '20': 'Ca', '21': 'Sc', '22': 'Ti', '23': 'V', '24': 'Cr', '25': 'Mn', '26': 'Fe', '27': 'Co', '28': 'Ni', '29': 'Cu', '30': 'Zn', '31': 'Ga', '32': 'Ge', '33': 'As', '34': 'Se', '35': 'Br', '36': 'Kr', '37': 'Rb', '38': 'Sr', '39': 'Y', '40': 'Zr', '41': 'Nb', '42': 'Mo', '43': 'Tc', '44': 'Ru', '45': 'Rh', '46': 'Pd', '47': 'Ag', '48': 'Cd', '49': 'In', '50': 'Sn', '51': 'Sb', '52': 'Te', '53': 'I', '54': 'Xe', '55': 'Cs', '56': 'Ba', '57': 'La', '58': 'Ce', '59': 'Pr', '60': 'Nd', '61': 'Pm', '62': 'Sm', '63': 'Eu', '64': 'Gd', '65': 'Tb', '66': 'Dy', '67': 'Ho', '68': 'Er', '69': 'Tm', '70': 'Yb', '71': 'Lu', '72': 'Hf', '73': 'Ta', '74': 'W', '75': 'Re', '76': 'Os', '77': 'Ir', '78': 'Pt', '79': 'Au', '80': 'Hg', '81': 'Tl', '82': 'Pb', '83': 'Bi', '84': 'Po', '86': 'Rn', '88': 'Ra', '89': 'Ac', '90': 'Th', '91': 'Pa', '92': 'U', '93': 'Np', '94': 'Pu', '95': 'Am', '96': 'Cm', '97': 'Bk', '98': 'Cf'}


# 05函数，提示输入偶数个字符串，然后返回字典形式
def strToDict():
    '''
    该函数没有形参，函数内部提示输入组元组成字符串，返回一个组元组成字典
    '''
    print('|----------------------------------------调用函数：strToDict')
    print("请依次输入原子或分子符号及数量，用英文逗号隔开,如: Si,90,B,10 或 CaO,1,SiO2,1 注意目前仅支持前98号元素和部分氧化物。")
    elementList = input()
    listColumn = elementList.split(',')
    elementNumber = len(listColumn)                   # 统计输入列表的元素个数，包含化学符号及相应的数量
    if elementNumber%2 != 0 :
        print('输入的字符串语法错误，元素数量应为偶数个，请重新输入！')
        sys.exit("404")
    for i in range(1,elementNumber+1,2): # 2代表步长为2，遍历输入的序号为偶数位置的元素是否只有数字组成
        if listColumn[i].isdigit() : # isdigit() 方法检测字符串是否只由数字组成，只对 0 和 正数有效
            print('输入的组元及数量',listColumn[i-1],listColumn[i])
        else:
            print('输入的字符串语法错误，组元数量输入错误，请重新输入！')
            sys.exit("404")
        
    elementKindNumber = float(elementNumber/2)        # 统计化学符号的种类数
    print("化学符号种类数量：",elementKindNumber,' 注意：化学符号包括原子符号和分子的化学式')
    elementDict = {}                                  # 该字典用于统计每种化学符号的数量，如：{'Si': '170', 'V': '10', 'B': '20'}
    for i in range(0,elementNumber,2):
        elementDict[listColumn[i]] = listColumn[i+1]  # 将输入的化学符号及相应数量储存到字典中
    print("凝聚态混合体系构成",elementDict,'\n')              # 即上述字典的内容，{'Si': '170', 'V': '10', 'B': '20'}
    return elementDict                                # 返回输入字符串的字典
    # 上面的这部分代码是将输入的字符串转化为字典，如输入 Si,90,B,10 转化为类似 {'Si': '90', 'B': '10'}



# atomDict = loadData('38_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json')     # 调用01函数，将化合物的原子组成从指定的json文件加载到字典中
# atomDict = loadData(dataBaseFile1)    # 
# 例如，atomDict = {"CaO": {"Ca": "1", "O": "1", "total": "2"}, "SiO2": {"Si": "1", "O": "2", "total": "3"}, "B2O3": {"B": "2", "O": "3", "total": "5"}, "P2O5": {"P": "2", "O": "5", "total": "7"}, "MgO": {"Mg": "1", "O": "1", "total": 2}, "Al2O3": {"Al": "2", "O": "3", "total": 5}, "K2O": {"K": "2", "O": "1", "total": 3}, "TiO2": {"Ti": "1", "O": "2", "total": 3}, "V2O5": {"V": "2", "O": "5", "total": 7}, "Cr2O3": {"Cr": "2", "O": "3", "total": 5}, "MnO": {"Mn": "1", "O": "1", "total": 2}, "MnO2": {"Mn": "1", "O": "2", "total": 3}, "FeO": {"Fe": "1", "O": "1", "total": 2}, "Fe3O4": {"Fe": "3", "O": "4", "total": 7}, "Fe2O3": {"Fe": "2", "O": "3", "total": 5}, "Co2O3": {"Co": "2", "O": "3", "total": 5}, "NiO": {"Ni": "1", "O": "1", "total": 2}, "Cu2O": {"Cu": "2", "O": "1", "total": 3}, "CuO": {"Cu": "1", "O": "1", "total": 2}, "ZrO2": {"Zr": "1", "O": "2", "total": 3}, "CaF2": {"Ca": "1", "F": "2", "total": 3}}


# 10函数，判断组元是否在化合物原子组成json数据库中，返回更新后的化合物原子组成字典,以及筛选出的所有输入的分子式列表
# atomicMassSingleDict, 相对原子质量字典数据库
# atomDict,json数据库中的原子组成字典
# elementDict，输入的组元组成字典，考虑了单质和化合物共存体系并分开讨论
def atomMakeupDict(atomicMassSingleDict,DBfilename,elementDict):   # 输入的3个字典分别是原子质量字典，化合物原子组成json字典，输入的字典
    '''
    该函数有3个形参，分别为输入的组元组成字典，json原子组成数据库文件名，一个相对原子质量字典数据库
    首先对组元进行分类，判断单质和化合物，对原子组成数据库中缺少的化合物提示添加并更新
    该函数返回两个参数，一个是输入组元中的化合物列表，还有一个是更新后的原子组成字典
    该函数内部调用了3个函数，分别为 loadData， dumpData 以及 chemicalsSplit
    该函数一定会被调用，为计算输入的化合物组元的相对分子质量提供了两个极其重要的数据
    '''
    print('|----------------------------------------调用函数：atomMakeupDict')
    atomDict = loadData(DBfilename)           # 加载原子组成数据库json字典
    simpleSubList = []                        # 用于储存单质的列表
    jsonMoleList = []                         # 用于储存位于json文件中的化合物的列表
    missMoleList = []                         # 该列表用于储存输入的而数据库中缺少原子组成的化学符号
    for i in list(elementDict.keys()):        # 下面是将elementDict的键进行分类，判断是单质还是化合物
        if i in list(atomicMassSingleDict.keys()):       # 判断输入的物质是否为单质
            simpleSubList.append(i)
            print('已确认该化学符号在原子相对质量数据库中 ',i)
        elif i in list(atomDict.keys()):      # 判断输入的物质是否存在于json文件中
            jsonMoleList.append(i)            # 已经存在于json文件中的化合物分子式
            print('已确认该化学符号在json分子相对质量数据库中 ',i)
        else:         # 剩下的肯定是json文件中没有的分子式                            
            print('已确认该化学符号未在json相对分子质量数据库中，请添加该化学符号的原子组成 ',i)
            missMoleList.append(i)            # 储存输入字典中不在json文件中的分子式
    chemSubList = jsonMoleList + missMoleList               # 该列表用于储存输入的所有化合物的分子式
    # 判断输入的字符串活字典中的组元构成情况
    if len(simpleSubList) == 0:
        print('混合体系不存在单质组元，所有组元均为化合物。')
    elif len(chemSubList) == 0:
        print('混合体系所有组元均为单质，不存在化合物。')
    else:
        print('混合体系中既有单质组元也有化合物组元。')
    #     
    if len(missMoleList) == 0:
        print('~~~~~~~~~所有化合物组元均在原子组成数据库内,原子组成数据库如下：',sorted(list(atomDict.keys()))) # json文件中的数据
    else:                                     # 如果有需要添加的新的分子式，则会要求输入原子组成，更新文件
        # print('-----部分化合物组元不在原子组成数据库内，请为以下化合物添加原子组成-----：',missMoleList)
        plusDict = chemicalsSplit(missMoleList)     # 调用03函数，为部分化合物添加原子组成，返回一个字典plusDict，该字典中含有化合物的原子组成，如下所示
        # plusDict = {'SiO2': {'Si': '1', 'O': '2', 'total': 3}, 'CaO': {'Ca': '1', 'O': '1', 'total': 2}, 'B2O3': {'B': '2', 'O': '3', 'total': 5}}
        atomDict = { **atomDict, **plusDict } # 将字典进行拼接并更新，该字典是一个包含所有化合物的原子组成的字典
        print('全新化合物原子组成字典为：',atomDict)
        print('是否将新的化合物原子构成添加到json数据库中？不添加不影响本次计算，但下次需重新输入化合物原子构成。默认Enter键为添加，F或f为不添加。')
        inputChose = input()
        if inputChose == '':
            # dumpData('38_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json',atomDict)   # 调用02函数，将更新后的字典写入到json文件中
            dumpData(DBfilename,atomDict)   # 见上，将更新后的原子组成保存到json文件中
            print('已添加的新的化合物原子构成字典',plusDict)
            print('写入的文件名为：',DBfilename)
            print('----------原子组成数据库更新后包含的化合物种类----------：',sorted(list(atomDict.keys())))  # 打印出更新后字典中的化合物化学式   
        else:
            print('未添加新的化合物原子构成',plusDict)
    print('\n')
    return atomDict,chemSubList    # 返回更新后的化合物组成字典,以及所有输入的化合物分子式列表，二者位于一个列表中




# 04函数，输入两个字典和一个列表，返回一个字典，输入的字典包括化合物原子组成字典和相对原子质量字典，输入的列表是待计算相对分子质量的分子式，输出字典为化合物的相对分子质量字典
# 例如，atomMassDict = {'H': ['1', 'Hydrogen', 'H', '1.00794', '1', '1'], 'He': ['2', 'Helium', 'He', '4.002602', '18', '1']}
# 例如，moleCompDict = {'SiO2': {'Si': '1', 'O': '2', 'total': 3}, 'CaO': {'Ca': '1', 'O': '1', 'total': 2}, 'B2O3': {'B': '2', 'O': '3', 'total': 5}}
# 例如，molecuList = [CaO,SiO2,B2O3,TiO2]，待计算相对分子质量的列表
def moleMassCalc(atomMassDict,moleCompDict,molecuList):   # 04函数，atomMassDict是一个原子相对质量字典，moleCompDict是一个分子的原子组成字典，参考如上
    '''
    3个形式参数，相对原子质量数据库字典，最新的原子组成数据库字典，待计算相对分子质量的分子式列表
    该函数内部没有调用其他函数，该函数每次运行都会被调用，返回一个化合物相对分子质量字典，都是输入组元化合物
    '''
    print('|----------------------------------------调用函数：moleMassCalc')
    moleMassDict = {}   
    for i,j in enumerate(molecuList):        # 遍历待计算相对分子质量的分子式列表
        moleMassList = []                    # 每一次循环都要重置为空
        moleMass = 0
        for k in list(moleCompDict[j].keys()):
            if k != 'total':
                moleMass += float(moleCompDict[j][k]) * float(atomMassDict[k][3])    # 3代表列表中索引为3的元素为相对原子质量
        moleMassList = [i+1]+['null']+[j]+[moleMass]    # 列表相加，列表包含四个元素，注意相对分子质量字典的值列表数据结构
        moleMassDict[j] = moleMassList
    print('---*-*-*-*-*-*-*-*-*-*-*-*计算出的相对分子质量字典：',moleMassDict)
    print('\n')
    return moleMassDict  # return 返回化合物的相对分子质量字典，例如，moleMassDict = {'SiO2': ['1', 'null', 'SiO2', '60.0843'], 'CaO': ['2', 'null', 'CaO', '56.077400000000004']}




"""
下面是字典合并的一个语法
x = {}
y= {}
z = {**x,**y}  # 字典合并
"""


# 09函数，基于factsage计算化合物密度,loadFileName是相对原子质量字典
def ChemDensityCalc(atomicMassSingleDict,MoleMakeupDict,chemSpecieList):      # 该方法是输入一个化合物字符串，提示输入factsage计算的该种化合物的密度
    '''
    提示输入factsage计算的1mol化合物体积
    调用了 01函数loadData返回原子组成字典
    调用了04函数moleMassCalc计算相对分子质量，即需要相对原子质量字典和化合物原子组成字典
    共3个形参，分别为相对原子质量字典，chemSpecieList待计算密度的化合物列表，MoleMakeupDict 为最新版原子组成字典
    返回组元
    '''
    print('|----------------------------------------调用函数：ChemDensityCalc')
    # NA = 6.0221415*1e23                   # 阿伏伽德罗常数，Avogadro constant, 6.0221367×10²³ mol⁻¹  
    print('正在基于factsage计算的化合物为：',chemSpecieList)
    # MoleMakeupDict = loadData('38_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json') # 调用01函数，加载json文件，数据库中必定有这些化合物的原子组成
    # MoleMakeupDict = loadData(loadFileName)                   # 调用了01函数,加载原子组成字典
    moleRelativeMassDict = moleMassCalc(atomicMassSingleDict,MoleMakeupDict,chemSpecieList)    # 调用04函数，返回某些化合物相对分子质量字典 {'SiO2': ['1', 'null', 'SiO2', '60.0843'], 'CaO': ['2', 'null', 'CaO', '56.077400000000004']}
    print('请依次输入factsage计算的 1800K 左右对应 1 mol每种液态化合物的体积，单位:L，用英文逗号隔开, 如 0.014516,0.047673 ，物质列表为：',chemSpecieList)
    volFactInput = [float(i) for i in input().split(',')]     # 将输入的体积数据转化为浮点型
    if len(chemSpecieList) != len(volFactInput):
        print('输入的体积数据个数不等于化合物数量！')
        sys.exit("404")                  # 输入错误，中断程序
    densityDict = {}                        # 初始化临时列表，储存factsage计算出来的密度
    for n,v in zip(chemSpecieList,volFactInput):               # 同时遍历两个列表
        relativeMassValue = moleRelativeMassDict[n][3]         # 计算1mol相对分子质量
        densityMixFactsage = relativeMassValue/v/1000          # 摩尔质量除以摩尔体积，得到密度，除以1000得到cm3单位
        tempList = [densityMixFactsage] + ['g/cm3', 'null']+['factsage_09function'] + ['null', 'null', 'null']
        #  tempList = ['2.335', 'g/cm3', 'null', 'SiO2', 'null', 'null', 'null']
        densityDict[n] = tempList
    print('返回基于factsage计算的化合物密度字典',densityDict)
    return densityDict     # 返回计算出来的化合物密度字典，{'SiO2': ['2.335', 'g/cm3', 'null', 'SiO2', 'null', 'null', 'null'],'CaO': ['2.8581', 'g/cm3', 'null', 'CaO', 'null', 'null', 'null'],'B2O3': ['2.55', 'g/cm3', 'null', 'B2O3', 'null', 'null', 'null'],'V2O5': ['3.357', 'g/cm3', 'null', 'V2O5', 'null', 'null', 'null'],'MnO2': ['5.2', 'g/cm3', 'null', 'MnO2', 'null', 'null', 'null'],'Fe2O3': ['5.277', 'g/cm3', 'null', 'Fe2O3', 'null', 'null', 'null']}


# 14函数，基于factsage计算单质密度，需要传入单质的相对原子质量字典atomMassDict和单质化学符号列表danZhiList。
def danZhiDensityCalc(atomMassDict,danZhiList):
    print('|----------------------------------------调用函数：danZhiDensityCalc')
    # atomMassDict = {'H': ['1', 'Hydrogen', 'H', '1.00794', '1', '1'], 'He': ['2', 'Helium', 'He', '4.002602', '18', '1'], 
    moleRelativeMassDict = atomMassDict
    print('请依次输入factsage计算的 1800K 左右对应 1 mol每种液态物质的体积，单位:L，用英文逗号隔开, 如 0.014516,0.047673 ，物质列表为：',danZhiList)
    volFactInput = [float(i) for i in input().split(',')]     # 将输入的体积数据转化为浮点型
    if len(danZhiList) != len(volFactInput):
        print('输入的体积数据个数不等于化合物数量！')
        sys.exit("404")                  # 输入错误，中断程序
    densityDict = {}                        # 初始化临时列表，储存factsage计算出来的密度
    for n,v in zip(danZhiList,volFactInput):               # 同时遍历两个列表
        relativeMassValue = float(moleRelativeMassDict[n][3])         # 计算1mol相对原子质量
        densityMixFactsage = relativeMassValue/v/1000          # 摩尔质量除以摩尔体积，得到密度，除以1000得到cm3单位
        tempList = [densityMixFactsage] + ['g/cm3', 'null']+['factsage_09function'] + ['null', 'null', 'null']
        #  tempList = ['2.335', 'g/cm3', 'null', 'SiO2', 'null', 'null', 'null']
        densityDict[n] = tempList
    print('返回基于factsage计算的化合物密度字典',densityDict)
    return densityDict 


# 11函数，手动录入化合物密度字典
# chemSpecieList是一个待手动录入密度的化合物分子式列表，用英文逗号隔开
def molDensityInput(chemSpecieList):
    '''
    该函数提需要传入化合物列表，返回化合物密度字典
    '''
    print('|----------------------------------------调用函数：molDensityInput')
    print('请求手动录入密度的化合物分子式列表为：',chemSpecieList)
    print('请依次输入1个或多个密度值，对应上述化合物的密度，用英文逗号隔开，单位 g/cm3，如 2.3,1.0 等，注意此处不需要输入分子式。')
    denInputList = input().split(',')
    if len(denInputList) != len(chemSpecieList):
        print('输入的密度数据个数不等于化合物数量！')
        sys.exit("404")                  # 输入错误，中断程序
    densityDict = {} 
    for n,v in zip(chemSpecieList,denInputList):
        densityDict[n] = [v] + ['g/cm3', 'null']+['manual_11function'] + ['null', 'null', 'null']
    print('返回基于factsage计算的化合物密度字典',densityDict)
    return densityDict



# 08函数用于判断输入的组元是否都存在于密度数据库中，对于不在的提示基于factsage计算密度或手动录入密度
# pureDensityDict 是单质的密度字典，densityFile是化合物密度字典的json文件名，elementDict是输入的组元字典，包括单质和化合物
# MoleMakeupDict是化合物的原子组成字典，atomicMassSingleDict是相对原子质量字典
def whetherInDatabase(pureDensityDict,densityFile,atomicMassSingleDict,MoleMakeupDict,elementDict): 
    '''
    调用了09函数
    '''
    print('|----------------------------------------调用函数：whetherInDatabase')
    chemDensityDict = loadData(densityFile)   # densityFile是化合物密度数据库json文件名
    simpleSubList = []                        # 用于储存单质的列表
    jsonMoleList = []                         # 用于储存位于json文件中的化合物的列表
    missMoleList = []                         # 该列表用于储存输入的而数据库中缺少原子组成的化学符号
    for i in list(elementDict.keys()):        # 下面是将elementDict的键进行分类，判断是单质还是化合物
        if i in list(pureDensityDict.keys()):       # 判断输入的物质是否为单质
            simpleSubList.append(i)
            print('该化学符号在单质数据库中 ',i)
        elif i in list(chemDensityDict.keys()):      # 判断输入的物质是否存在于json文件中
            jsonMoleList.append(i)            # 已经存在于json文件中的化合物分子式
            print('该化学符号在json化合物密度数据库中 ',i)
        else:         # 剩下的肯定是json文件中没有的分子式                            
            print('该纯物质未在json化合物密度数据库中，请添加化合物密度 ',i)
            missMoleList.append(i)            # 储存输入字典中不在json文件中的分子式
    # chemSubList = jsonMoleList + missMoleList               # 该列表用于储存输入的所有化合物的分子式
    
    if len(missMoleList) == 0:
        print('~~~~~~~~~所有化合物的密度均在数据库中：',sorted(list(chemDensityDict.keys()))) # json文件中的数据
    else:                                     # 如果有需要添加的新的分子式，则会要求输入原子组成，更新文件
        print('-----部分化合物密度不在数据库中，请为以下化合物添加密度-----：',missMoleList)
        print('请选择密度添加方式，1代表factsage计算，2代表手动录入（书籍或文献值）')
        choose = input()
        if choose == '1':
            plusDict = ChemDensityCalc(atomicMassSingleDict,MoleMakeupDict,missMoleList)  # 09函数，基于factsage计算化合物密度,loadFileName是相对原子质量字典
            # plusDict = {'SiO2': {'Si': '1', 'O': '2', 'total': 3}, 'CaO': {'Ca': '1', 'O': '1', 'total': 2}, 'B2O3': {'B': '2', 'O': '3', 'total': 5}}
        elif choose == '2':
            plusDict = molDensityInput(missMoleList)   # 11函数，手动录入化合物密度字典
        else:
            print('选择错误，请重新输入！')
            sys.exit('404')

        chemDensityDict = { **chemDensityDict, **plusDict } # 将字典进行拼接并更新，该字典是一个包含所有化合物的原子组成的字典
        print('是否将新的化合物密度添加到json数据库中？不添加不影响本次计算，但下次需重新输入化合物密度。默认Enter键为添加，F或f为不添加。')
        inputChose = input()
        if inputChose == '':
            dumpData( densityFile,chemDensityDict)   # 调用02函数，将更新后的字典写入到json文件中
            print('已添加的新的化合物密度',plusDict)
            print('----------化合物密度数据库更新后包含的化合物种类----------：',sorted(list(chemDensityDict.keys())))  # 打印出更新后字典中的化合物化学式   
        else:
            print('未添加新的化合物原子构成',plusDict)   
    return chemDensityDict   # 返回更新后的化合物密度数据库



# 06函数，用于计算多组元混合体系的密度，需要输入3个字典，分别为相对原子质量字典atomicMassDict，各纯组元密度字典pureDensityDict，混合组元的种类及数量字典elementDict
# 06函数返回一个字典saveDict，字典包含混合体系的密度，混合体系以正方体计的盒子体积和边长
def densityMixCalc(atomicMassDict,pureDensityDict,elementDict):
    print('|----------------------------------------调用函数：densityMixCalc')
    elementKindNumber = len(list(elementDict.keys()))            # 组元数量即输入的元组字典键的数量
    print("组元种类数量(单质和化合物): ",elementKindNumber)
    print("凝聚态混合体系构成: ",elementDict)   
    """
    element1 = elementListDict["element"+str(i)]
    elementNumber1 =  elementNumberDict["elementNumber"+str(i)]
    ρ1 =  ρDict["ρ"+str(i)]
    m1 =  mDict["m"+str(i)]
    """    
    elementListDict = {}     # 组元种类字典
    elementNumberDict = {}   # 各组元数量字典
    ρDict = {}               # 各组元密度字典
    ρNameDensityDict = {}    # 与ρDict一样，但键是组元符号
    mDict = {}               # 各组元总相对分子质量字典
    mNameDensityDict = {}    # 与mDict一样，但键是组元符号
    for i in range(1,int(elementKindNumber)+1):       # 将各组元种类写入到字典
        elementListDict["element"+str(i)] = list(elementDict.keys())[i-1]    
    # print("混合体系组元种类：",elementListDict)        # # {'element1': 'Si', 'element2': 'V', 'element3': 'B'}
    for i in range(1,int(elementKindNumber)+1):       # 将各组元数量写入到字典
        elementNumberDict["elementNumber"+str(i)] = list(elementDict.values())[i-1]   # {'elementNumber1': '170', 'elementNumber2': '10', 'elementNumber3': '20'}
    # print("体系各组元数量",elementNumberDict)  
    for i in range(1,int(elementKindNumber)+1):       # 将各组元密度写入到字典
        ρDict["ρ"+str(i)] = float(pureDensityDict[elementListDict["element"+str(i)]][0])
        ρNameDensityDict[list(elementDict.keys())[i-1]] = float(pureDensityDict[elementListDict["element"+str(i)]][0])
    print("|-----------体系各纯组元密度-------------------|", ρNameDensityDict, '单位:g/cm3') 
    for i in range(1,int(elementKindNumber)+1):       # 各组元相对分子质量和总的相对质量写入到字典
        mDict["m"+str(i)]  = float(elementNumberDict["elementNumber"+str(i)])*float(atomicMassDict[elementListDict["element"+str(i)]][3])
        mNameDensityDict[list(elementDict.keys())[i-1]] = float(atomicMassDict[elementListDict["element"+str(i)]][3])
    # print("|-----------体系各组元总相对质量----------------|", mDict)  # 总的相对质量就是 个数*相对原子(分子)质量
    print("|-----------体系各相对原子、分子相对质量---------|", mNameDensityDict)
    ρMultipl = 1  # initial value，连乘的初始值可设为1
    for i in range(1,int(elementKindNumber)+1):
        ρMultipl = ρDict["ρ"+str(i)]*ρMultipl     # ρ1*ρ2*ρ3*ρ4*ρ5，分子的第一部分
    print("ρi连乘 ∏ρi", ρMultipl)
    mSum = 0      # 求和初始值可以设为0
    for i in range(1,int(elementKindNumber)+1):   # 计算体系总的相对分子质量，每种组元相对质量*数量求和
        mSum = mSum + mDict["m"+str(i)]           # (m1+m2+m3+m4+m5)，分子的第二部分
    print("mi求和 ∑mi,即混合体系总的相对分子质量", mSum)
    atomicNumberSum = 0                           # 计算体系的总原子数，初始化为0
    for i in range(1,int(elementKindNumber)+1):   # 统计每一种组元数量，并求和
        atomicNumberSum = atomicNumberSum + float(elementNumberDict["elementNumber"+str(i)])
    print("体系总原子和分子数求和 ∑Ni", atomicNumberSum)
    
    """
    混合密度计算
    """
    mρMixMultiList = []      # 列表，用于储存分母的所有部分，m1*ρ2*ρ3*ρ4*ρ5, m2*ρ1*ρ3*ρ4*ρ5, m3*ρ1*ρ2*ρ4*ρ5, m4*ρ1*ρ2*ρ3*ρ5, m5*ρ1*ρ2*ρ3*ρ4, ...
    for i in range(1,int(elementKindNumber)+1):
        elementKindNumberList = list(range(1,int(elementKindNumber)+1))    # 初始化一个原子种类数列表 [1,2,3,4,...]
        tranElementKindNumberList = elementKindNumberList                  # 复制上述列表
        # print("tranElementKindNumberList", tranElementKindNumberList)      # 打印复制后的列表
        tranElementKindNumberList.remove(i)                                # 每次从列表中移除遍历的序号
        modifiedList = tranElementKindNumberList                           # 复制移除序号后的列表
        # print("modifiedList", modifiedList)
        mρMixMulti = mDict["m"+str(i)]                                     # 查找对应遍历序号组元的总相对质量（个数*相对原子(分子)质量），并将其初始化为该值
        for j in modifiedList:                                             # 遍历移除序号后的列表      
            mρMixMulti = mρMixMulti*ρDict["ρ"+str(j)]                      # 构造分母的每一部分，如 m1*ρ2*ρ3*ρ4*ρ5
        mρMixMultiList.append(mρMixMulti)                                  # 将分母的每一部分添加到列表中
    mρMixMultiSum = sum(mρMixMultiList)   # 对列表中分母的每一部分进行求和，m1*ρ2*ρ3*ρ4*ρ5 + m2*ρ1*ρ3*ρ4*ρ5+m3*ρ1*ρ2*ρ4*ρ5+m4*ρ1*ρ2*ρ3*ρ5+m5*ρ1*ρ2*ρ3*ρ4
    densityMix = ρMultipl*mSum/mρMixMultiSum                               # 计算体系的混合密度      
    print('|-----------基于等体积混合计算的密度------------|',int(elementKindNumber),"种组元混合密度：",round(densityMix,5),'单位:g/cm3\n')
    '''
    计算混合体系以正方体计的盒子体积和边长
    '''
    NA = 6.0221415*1e23                # 阿伏伽德罗常数，Avogadro constant, 6.0221367×10²³ mol⁻¹
    volumnCell = mSum/NA/densityMix    # (m1+m2+m3+m4+m5)/NA/densityMix, 单位cm3
    print("正方体盒子体积",volumnCell,'单位:cm3')
    sizeCell = math.pow(volumnCell,1/3)*1e8    # 单位cm到Å, *10e8
    print("基于原子等体积混合计算的正方体盒子尺寸",round(sizeCell,5),'单位:Å')
    """
    各元素质量百分数
    """
    massPercentDict = {}
    for i in range(1,int(elementKindNumber)+1):
        # massPercent1 = m1/(m1+m2+m3+m4+m5)*100
        massPercentDict[elementListDict["element"+str(i)]] = mDict["m"+str(i)]/mSum*100
    print("各组元质量百分数%",massPercentDict)      
    """
    各组元摩尔百分数
    """
    molPercentDict = {}
    for i in range(1,int(elementKindNumber)+1):
    #   molPercent1 = float(elementNumber1)/(float(elementNumber1)+float(elementNumber2)+float(elementNumber3)+float(elementNumber4)+float(elementNumber5))*100
        molPercentDict[elementListDict["element"+str(i)]] = float(elementNumberDict["elementNumber"+str(i)])/atomicNumberSum*100
    print("各组元摩尔百分数%",molPercentDict)
    # relativeAtomicMass = mSum
    # print("混合体系相对分子质量为",relativeAtomicMass,"体系构成：",elementDict)

    saveDict = {}                        # 初始化一个字典，用于储存06函数的计算结果
    saveDict['densityMix'] = densityMix    # 将混合密度保存到字典中
    saveDict['volumnCell'] = volumnCell    # 将混合体积保存到字典中
    saveDict['sizeCell']   = sizeCell      # 将盒子边长保存到字典中
    saveDict['mSum'] = mSum
    return saveDict                      # 06函数返回一个字典


# 07函数，基于factsage计算混合密度
def factDensityCalc(saveDict):   
    print('|----------------------------------------调用函数：factDensityCalc')
    mSum = saveDict['mSum']                # 总的相对分子质量
    densityMix = saveDict['densityMix']    # 等体积混合计算的密度
    sizeCell = saveDict['sizeCell']        # 等体积混合计算的盒子尺寸
    NA = 6.0221415*1e23                # 阿伏伽德罗常数，Avogadro constant, 6.0221367×10²³ mol⁻¹  
    """
    Factsage密度,注意factsage输入的原子数量单位是mol，不是个，给出的体积是基于原子mol数计算的
    """
    print("是否需要基于Factsage体积数据计算混合体系密度？输入Enter代表 True，F或f代表 False")
    factsageJudge = input()
    if factsageJudge == '':
        print("请输入Factsage计算的相同原子数量下的混合体系体积，单位:L，如 2.2745")
        factsageVolume = float(input())      # 注意这个体积是输入的摩尔体积，而不是以个数计的原子和分子体积
        sizeCellFactsage = math.pow(factsageVolume/NA*1000,1/3)*1e8   #   单位Å,
        print("Factsage计算的盒子尺寸: ",round(sizeCellFactsage,5), '单位:Å' )
        densityMixFactsage = mSum/factsageVolume/1000                 # 摩尔质量除以摩尔体积，得到密度，除以1000得到cm3单位
        print("|-----------基于Factsage计算的混合密度---------|",round(densityMixFactsage,5), ' 单位:g/cm3')
        densityDifference = densityMix-densityMixFactsage     # 比较两种方法计算的密度差值
        # print("------两种密度差值,densityMix-densityMixFactsage--------",round(densityDifference,6),' 单位:g/cm3')
        if abs(densityDifference) <= 0.001:
            print('|-----------密度计算差值 < 0.001')
        else:
            print('|-----------密度计算差值 > 0.001','差值为：',abs(round(densityDifference,4)))
        sizeCellDifference = sizeCell-sizeCellFactsage
        print("两种盒子尺寸差值,sizeCell-sizeCellFactsage",round(sizeCellDifference,6),' 单位:Å')
    else:
        print('未基于factsage计算混合密度！')
        

# 12函数，对密度数据库dataBaseFile2进行添加、删除、修改等操作。注意前11个函数对应功能4
def modifyDensityDB(dataBaseFile2):   # dataBaseFile2是形参
    print('|----------------------------------------调用函数：modifyDensityDB')
    print("进行数据修改或删除的数据库为：",dataBaseFile2)
    chemDenDict = loadData(dataBaseFile2)   # 密度数据库字典
    print('请选择操作类型，1代表删除数据，2代表修改化合物的密度，3代表向数据库中添加新的化合物密度')
    choose = input()
    if choose == '1':
        print('请依次输入需要删除密度的化合物分子式，用英文逗号隔开')
        chemSpecies = input().split(',')
        for i in chemSpecies:
            if i not in list(chemDenDict.keys()):
                print('!!!!!!!!!!!!警告：数据库中不存在分子式: ',i,'但程序仍会执行并删除剩余的化合物分子式!!!!!!!!!!!!\n')
        chemDenDict = { i:chemDenDict[i] for i in list(chemDenDict.keys()) if i not in chemSpecies}
        savefile = '49_[扩展-2化合物密度数据库-删除]单质或化合物或多相混合体系密度计算.json'
        print('修改后的字典键列表：',sorted(list(chemDenDict.keys())))
    elif choose == '2':
        print('请依次输入需要修改密度的化合物分子式和新的密度值，用英文逗号隔开')
        chemKeyValue = input().split(',')
        if len(chemKeyValue)%2 != 0:
            print('输入的语法错误，请重新输入！')
            sys.exit('404')   
        for i in range(0,len(chemKeyValue),2):
            if chemKeyValue[i] not in list(chemDenDict.keys()):
                print('!!!!!!!!!!!!警告：数据库中不存在该分子式: ',i,'但程序会添加该分子式密度数据!!!!!!!!!!!!\n')                  
            print('修改的化合物及新密度',chemKeyValue[i],chemKeyValue[i+1])
            # print(chemDenDict[chemKeyValue[i]])
            chemDenDict[chemKeyValue[i]] = [chemKeyValue[i+1]] + ['g/cm3', 'null']+['modified'] + ['null', 'null', 'null']
        print('修改后的密度字典：',chemDenDict)
        savefile = '49_[扩展-2化合物密度数据库-修改]单质或化合物或多相混合体系密度计算.json'
    elif choose == '3':
        print('请依次输入需要添加密度的化合物分子式和密度值，用英文逗号隔开，如： SiO2,2.33 ')
        chemKeyValue = input().split(',')
        if len(chemKeyValue)%2 != 0:
            print('输入的语法错误，请重新输入！')
            sys.exit('404')   
        for i in range(0,len(chemKeyValue),2):
            if chemKeyValue[i] in list(chemDenDict.keys()):
                print('!!!!!!!!!!!!警告：数据库中已经存在分子式: ',i,'程序会覆盖该分子式已有的密度数据!!!!!!!!!!!!\n')  
            print('添加的新的化合物及新密度',chemKeyValue[i],chemKeyValue[i+1])
            # print(chemDenDict[chemKeyValue[i]])
            chemDenDict[chemKeyValue[i]] = [chemKeyValue[i+1]] + ['g/cm3', 'null']+['modified_12function'] + ['null', 'null', 'null']
        print('修改后的密度字典：',chemDenDict)
        savefile = '49_[扩展-2化合物密度数据库-添加]单质或化合物或多相混合体系密度计算.json'            
    else:
        print('选择错误，请重新选择！')
        sys.exit('404')

    print('是否需要将修改后的数据库字典进行保存？Enter键为另存为新文件，F或f为不保存，d或者D为覆盖原文件。')
    saveChose = input()
    if saveChose == '':
        dumpData(savefile,chemDenDict)   # 另存为json文件
        print('保存的文件名为：', savefile,'存储方式为另存为新文件')
    elif saveChose == 'd' or 'D':
        dumpData(dataBaseFile2,chemDenDict)
        print('保存的文件名为：', dataBaseFile2,'存储方式为覆盖原文件保存')
    else:
        print('修改后的数据未保存！')


# 13函数，对化合物原子组成数据库进行添加、删除、修改等操作。
# 该函数内部调用了03函数，输入一个原子组成未知的化合物列表，返回该列表化合物的原子组成字典
def  modifyMakeupDB(atomMassDict,chemMakeupFile):
    print('|----------------------------------------调用函数：modifyMakeupDB')
    print("进行数据修改或删除的数据库为：",chemMakeupFile)
    chemMakeupDict = loadData(chemMakeupFile)   # 化合物原子组成数据库字典
    print('请选择操作类型，1代表删除数据，2代表修改化合物的原子组成，3代表向数据库中添加新的化合物原子组成')
    opChoose = input()
    
    print('请依次输入需要进行操作的化合物分子式，用英文逗号隔开，如 CaO,SiO2 ')
    chemSymbList = input().split(',')
    atomList   = []          # 统计输入的原子符号，基于相对原子质量字典判断
    chemExistList  = []          # 统计已经数据库中存在的化合物分子式
    chemMissList   = []          # 统计已经数据库中缺少的化合物分子式
    for i in chemSymbList:
        if i in list(atomMassDict.keys()):  # 判断是否为原子符号
            atomList.append(i)              # 添加到原子符号列表
        elif i in list(chemMakeupDict.keys()):  # 判断是否在化合物组成数据库中
            chemExistList.append(i)         # 添加到已经存在的化合物分子式列表
        else:
            chemMissList.append(i)          # 数据库不存在的化合物分子式列表
    if len(atomList) != 0:
        print('输入的组元包含有单质，单质的元素符号列表为：',atomList,'输入错误，请重新输入！')
        sys.exit('404')
    else:
        print('输入的组元中不包含有单质！')
    if len(chemExistList) != 0:
        print('输入的部分化合物已存在于原子组成数据库中，该部分化合物为：',chemExistList)
    else:
        print('输入的组元中不包含有原子组成已知的化合物！')
    if len(chemMissList) == 0:
        print('输入的组元中不含原子组成未知的化合物！')
    else :
        print('输入组元中含有原子组成未知的化合物为：',chemMissList)
    # 下面是对数据库字典进行操作
    if opChoose == '1':        # 删除键值对
        if len(chemExistList) == 0 :
            print('数据库中不存在想要删除的键，请检查后重新输入！')
            sys.exit('404')
        elif len(chemMissList) != 0 :
            print('输入中存在原子组成未知的新键，请检查后重新输入！键为：',chemMissList)
            sys.exit('404')            
        else:
            plusDict = {}               # 初始化空字典，储存被删掉的键值对
            for i in chemExistList:
                plusDict[i] = chemMakeupDict[i]
                del chemMakeupDict[i]    # 删除键值对
            atomDict = chemMakeupDict
    elif opChoose == '2':                  # 修改化合物的原子组成
        if len(chemExistList) == 0 :
            print('数据库中不存在想要修改的键，请检查后重新输入！')
            sys.exit('404')
        elif len(chemMissList) != 0 :
            print('输入中存在原子组成未知的新键，请检查后重新输入！键为：',chemMissList)
            sys.exit('404')  
        else:
            for i in chemExistList:
                del chemMakeupDict[i]    # 先对要修改的的键值对进行删除
            plusDict = chemicalsSplit(chemExistList)      # 调用03函数，输入一个原子组成未知的化合物列表，返回该列表化合物的原子组成字典
            atomDict = { **chemMakeupDict, **plusDict } # 将字典进行拼接并更新，该字典是一个包含所有化合物的原子组成的字典
    elif opChoose == '3':                  # 添加新的化合物的原子组成
        if len(chemExistList) != 0 :
            print('数据库中已存在想要添加的键，键为：',chemExistList,'请检查后重新输入！')
            sys.exit('404')
        elif len(chemMissList) == 0 :
            print('输入中不存在原子组成未知的新键，请检查后重新输入！')
            sys.exit('404')  
        else:
            plusDict = chemicalsSplit(chemMissList)      # 调用03函数，输入一个原子组成未知的化合物列表，返回该列表化合物的原子组成字典
            # plusDict = {'SiO2': {'Si': '1', 'O': '2', 'total': 3}, 'CaO': {'Ca': '1', 'O': '1', 'total': 2}, 'B2O3': {'B': '2', 'O': '3', 'total': 5}}
            atomDict = { **chemMakeupDict, **plusDict } # 将字典进行拼接并更新，该字典是一个包含所有化合物的原子组成的字典
    else:
        print('操作选择错误，请重新输入！')
        sys.exit('404')
    print('操作后的化合物原子组成字典为：',atomDict)
    print('是否将操作后的新化合物原子构成添加到json数据库中？不添加不影响本次计算，但下次需重新输入化合物原子构成。默认Enter键为添加，F或f为不添加。')
    inputChose = input()
    if inputChose == '':
        # dumpData('38_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json',atomDict)   # 调用02函数，将更新后的字典写入到json文件中
        dumpData(chemMakeupFile,atomDict)   # 见上，将更新后的原子组成保存到json文件中
        print('已完成删除、添加或修改的新化合物原子构成字典',plusDict)
        print('写入的文件名为：',chemMakeupFile)
        print('----------原子组成数据库更新后包含的化合物种类----------：',sorted(list(atomDict.keys())))  # 打印出更新后字典中的化合物化学式   
    else:
        print('未写入文件的新化合物原子构成',plusDict)        


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
        print("请输出需要处理的文件名,本例中为json格式，如 49_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json ")     # 提示命令行输入
        txtName = input()              # 注意字符串输入变量的数据类型转换
    return txtName


if __name__ == '__main__':
    
    print('''
  本脚本的功能如下:
      01: 查看数据库内容
      02: 手动修改、添加或删除化合物原子组成数据库中的数据
      03: 手动修改、添加或删除密度数据库中密度数据，并保存为新的数据库文件
      04: 基于factsage体积数据计算单组元密度
      05: 计算多组元混合体系密度
      
      -1: 测试
           
          ''')    
    
    print("请选择功能，输入Enter默认为-1测试")     # 提示选择功能
    defChoose = input()
    
    if   defChoose == "01":
        print('请选择数据库！')
        DBfilename = inputFunction()   # F01函数
        allDataDict = loadData(DBfilename)
    
    elif defChoose == "02":        # 对应于13函数
        print('请选择需要要进行添加、删除或者修改的化合物原子组成数据库！')
        DBfilename = '49_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json'
        atomMassDict = {'H': ['1', 'Hydrogen', 'H', '1.00794', '1', '1'], 'He': ['2', 'Helium', 'He', '4.002602', '18', '1'], 'Li': ['3', 'Lithium', 'Li', '6.941', '1', '2'], 'Be': ['4', 'Beryllium', 'Be', '9.012182', '2', '2'], 'B': ['5', 'Boron', 'B', '10.811', '13', '2'], 'C': ['6', 'Carbon', 'C', '12.0107', '14', '2'], 'N': ['7', 'Nitrogen', 'N', '14.0067', '15', '2'], 'O': ['8', 'Oxygen', 'O', '15.9994', '16', '2'], 'F': ['9', 'Fluorine', 'F', '18.9984032', '17', '2'], 'Ne': ['10', 'Neon', 'Ne', '20.1797', '18', '2'], 'Na': ['11', 'Sodium', 'Na', '22.98976928', '1', '3'], 'Mg': ['12', 'Magnesium', 'Mg', '24.3050', '2', '3'], 'Al': ['13', 'Aluminium', 'Al', '26.9815386', '13', '3'], 'Si': ['14', 'Silicon', 'Si', '28.0855', '14', '3'], 'P': ['15', 'Phosphorus', 'P', '30.973762', '15', '3'], 'S': ['16', 'Sulfur', 'S', '32.065', '16', '3'], 'Cl': ['17', 'Chlorine', 'Cl', '35.453', '17', '3'], 'Ar': ['18', 'Argon', 'Ar', '39.948', '18', '3'], 'K': ['19', 'Potassium', 'K', '39.0983', '1', '4'], 'Ca': ['20', 'Calcium', 'Ca', '40.078', '2', '4'], 'Sc': ['21', 'Scandium', 'Sc', '44.955912', '3', '4'], 'Ti': ['22', 'Titanium', 'Ti', '47.867', '4', '4'], 'V': ['23', 'Vanadium', 'V', '50.9415', '5', '4'], 'Cr': ['24', 'Chromium', 'Cr', '51.9961', '6', '4'], 'Mn': ['25', 'Manganese', 'Mn', '54.938045', '7', '4'], 'Fe': ['26', 'Iron', 'Fe', '55.845', '8', '4'], 'Co': ['27', 'Cobalt', 'Co', '58.933195', '9', '4'], 'Ni': ['28', 'Nickel', 'Ni', '58.6934', '10', '4'], 'Cu': ['29', 'Copper', 'Cu', '63.546', '11', '4'], 'Zn': ['30', 'Zinc', 'Zn', '65.409', '12', '4'], 'Ga': ['31', 'Gallium', 'Ga', '69.723', '13', '4'], 'Ge': ['32', 'Germanium', 'Ge', '72.64', '14', '4'], 'As': ['33', 'Arsenic', 'As', '74.92160', '15', '4'], 'Se': ['34', 'Selenium', 'Se', '78.96', '16', '4'], 'Br': ['35', 'Bromine', 'Br', '79.904', '17', '4'], 'Kr': ['36', 'Krypton', 'Kr', '83.798', '18', '4'], 'Rb': ['37', 'Rubidium', 'Rb', '85.4678', '1', '5'], 'Sr': ['38', 'Strontium', 'Sr', '87.62', '2', '5'], 'Y': ['39', 'Yttrium', 'Y', '88.90585', '3', '5'], 'Zr': ['40', 'Zirconium', 'Zr', '91.224', '4', '5'], 'Nb': ['41', 'Niobium', 'Nb', '92.90638', '5', '5'], 'Mo': ['42', 'Molybdenum', 'Mo', '95.94', '6', '5'], 'Tc': ['43', 'Technetium', 'Tc', '98', '7', '5'], 'Ru': ['44', 'Ruthenium', 'Ru', '101.07', '8', '5'], 'Rh': ['45', 'Rhodium', 'Rh', '102.905', '9', '5'], 'Pd': ['46', 'Palladium', 'Pd', '106.42', '10', '5'], 'Ag': ['47', 'Silver', 'Ag', '107.8682', '11', '5'], 'Cd': ['48', 'Cadmium', 'Cd', '112.411', '12', '5'], 'In': ['49', 'Indium', 'In', '114.818', '13', '5'], 'Sn': ['50', 'Tin', 'Sn', '118.710', '14', '5'], 'Sb': ['51', 'Antimony', 'Sb', '121.760', '15', '5'], 'Te': ['52', 'Tellurium', 'Te', '127.60', '16', '5'], 'I': ['53', 'Iodine', 'I', '126.904', '47', '17', '5'], 'Xe': ['54', 'Xenon', 'Xe', '131.293', '18', '5'], 'Cs': ['55', 'Caesium', 'Cs', '132.9054519', '1', '6'], 'Ba': ['56', 'Barium', 'Ba', '137.327', '2', '6'], 'La': ['57', 'Lanthanum', 'La', '138.90547', 'n/a', '6'], 'Ce': ['58', 'Cerium', 'Ce', '140.116', 'n/a', '6'], 'Pr': ['59', 'Praseodymium', 'Pr', '140.90765', 'n/a', '6'], 'Nd': ['60', 'Neodymium', 'Nd', '144.242', 'n/a', '6'], 'Pm': ['61', 'Promethium', 'Pm', '145', 'n/a', '6'], 'Sm': ['62', 'Samarium', 'Sm', '150.36', 'n/a', '6'], 'Eu': ['63', 'Europium', 'Eu', '151.964', 'n/a', '6'], 'Gd': ['64', 'Gadolinium', 'Gd', '157.25', 'n/a', '6'], 'Tb': ['65', 'Terbium', 'Tb', '158.92535', 'n/a', '6'], 'Dy': ['66', 'Dysprosium', 'Dy', '162.500', 'n/a', '6'], 'Ho': ['67', 'Holmium', 'Ho', '164.930', '32', 'n/a', '6'], 'Er': ['68', 'Erbium', 'Er', '167.259', 'n/a', '6'], 'Tm': ['69', 'Thulium', 'Tm', '168.93421', 'n/a', '6'], 'Yb': ['70', 'Ytterbium', 'Yb', '173.04', 'n/a', '6'], 'Lu': ['71', 'Lutetium', 'Lu', '174.967', '3', '6'], 'Hf': ['72', 'Hafnium', 'Hf', '178.49', '4', '6'], 'Ta': ['73', 'Tantalum', 'Ta', '180.94788', '5', '6'], 'W': ['74', 'Tungsten', 'W', '183.84', '6', '6'], 'Re': ['75', 'Rhenium', 'Re', '186.207', '7', '6'], 'Os': ['76', 'Osmium', 'Os', '190.23', '8', '6'], 'Ir': ['77', 'Iridium', 'Ir', '192.217', '9', '6'], 'Pt': ['78', 'Platinum', 'Pt', '195.084', '10', '6'], 'Au': ['79', 'Gold', 'Au', '196.966569', '11', '6'], 'Hg': ['80', 'Mercury', 'Hg', '200.59', '12', '6'], 'Tl': ['81', 'Thallium', 'Tl', '204.3833', '13', '6'], 'Pb': ['82', 'Lead', 'Pb', '207.2', '14', '6'], 'Bi': ['83', 'Bismuth', 'Bi', '208.98040', '15', '6'], 'Po': ['84', 'Polonium', 'Po', '210', '16', '6'], 'At': ['85', 'Astatine', 'At', '210', '17', '6'], 'Rn': ['86', 'Radon', 'Rn', '220', '18', '6'], 'Fr': ['87', 'Francium', 'Fr', '223', '1', '7'], 'Ra': ['88', 'Radium', 'Ra', '226', '2', '7'], 'Ac': ['89', 'Actinium', 'Ac', '227', 'n/a', '7'], 'Th': ['90', 'Thorium', 'Th', '232.03806', 'n/a', '7'], 'Pa': ['91', 'Protactinium', 'Pa', '231.03588', 'n/a', '7'], 'U': ['92', 'Uranium', 'U', '238.02891', 'n/a', '7'], 'Np': ['93', 'Neptunium', 'Np', '237', 'n/a', '7'], 'Pu': ['94', 'Plutonium', 'Pu', '244', 'n/a', '7'], 'Am': ['95', 'Americium', 'Am', '243', 'n/a', '7'], 'Cm': ['96', 'Curium', 'Cm', '247', 'n/a', '7'], 'Bk': ['97', 'Berkelium', 'Bk', '247', 'n/a', '7'], 'Cf': ['98', 'Californium', 'Cf', '251', 'n/a', '7'], 'Es': ['99', 'Einsteinium', 'Es', '252', 'n/a', '7'], 'Fm': ['100', 'Fermium', 'Fm', '257', 'n/a', '7'], 'Md': ['101', 'Mendelevium', 'Md', '258', 'n/a', '7'], 'No': ['102', 'Nobelium', 'No', '259', 'n/a', '7'], 'Lr': ['103', 'Lawrencium', 'Lr', '262', '3', '7'], 'Rf': ['104', 'Rutherfordium', 'Rf', '261', '4', '7'], 'Db': ['105', 'Dubnium', 'Db', '262', '5', '7'], 'Sg': ['106', 'Seaborgium', 'Sg', '266', '6', '7'], 'Bh': ['107', 'Bohrium', 'Bh', '264', '7', '7'], 'Hs': ['108', 'Hassium', 'Hs', '277', '8', '7'], 'Mt': ['109', 'Meitnerium', 'Mt', '268', '9', '7'], 'Ds': ['110', 'Darmstadtium', 'Ds', '271', '10', '7'], 'Rg': ['111', 'Roentgenium', 'Rg', '272', '11', '7'], 'Uub': ['112', 'Ununbium', 'Uub', '285', '12', '7'], 'Uut': ['113', 'Ununtrium', 'Uut', '284', '13', '7'], 'Uuq': ['114', 'Ununquadium', 'Uuq', '289', '14', '7'], 'Uup': ['115', 'Ununpentium', 'Uup', '288', '15', '7'], 'Uuh': ['116', 'Ununhexium', 'Uuh', '292', '16', '7'], 'Uuo': ['118', 'Ununoctium', 'Uuo', '294', '18', '7']}
        modifyMakeupDB(atomMassDict,DBfilename) # atomMassDict 是相对原子质量字典
        
    elif defChoose == "03":                # 对应于12函数
        # dataBaseFile1 = '49_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json'
        print('请选择需要要进行添加、删除或者修改的密度数据库！')
        # DBfilename = inputFunction()     # F01函数  
        DBfilename = '49_[扩展-2化合物密度数据库]单质或化合物或多相混合体系密度计算.json'
        # dataBaseFile2 = '49_[扩展-2化合物密度数据库]单质或化合物或多相混合体系密度计算.json'
        modifyDensityDB(DBfilename)        # 调用12函数

    elif defChoose == "04":
        atomMassDict = {'H': ['1', 'Hydrogen', 'H', '1.00794', '1', '1'], 'He': ['2', 'Helium', 'He', '4.002602', '18', '1'], 'Li': ['3', 'Lithium', 'Li', '6.941', '1', '2'], 'Be': ['4', 'Beryllium', 'Be', '9.012182', '2', '2'], 'B': ['5', 'Boron', 'B', '10.811', '13', '2'], 'C': ['6', 'Carbon', 'C', '12.0107', '14', '2'], 'N': ['7', 'Nitrogen', 'N', '14.0067', '15', '2'], 'O': ['8', 'Oxygen', 'O', '15.9994', '16', '2'], 'F': ['9', 'Fluorine', 'F', '18.9984032', '17', '2'], 'Ne': ['10', 'Neon', 'Ne', '20.1797', '18', '2'], 'Na': ['11', 'Sodium', 'Na', '22.98976928', '1', '3'], 'Mg': ['12', 'Magnesium', 'Mg', '24.3050', '2', '3'], 'Al': ['13', 'Aluminium', 'Al', '26.9815386', '13', '3'], 'Si': ['14', 'Silicon', 'Si', '28.0855', '14', '3'], 'P': ['15', 'Phosphorus', 'P', '30.973762', '15', '3'], 'S': ['16', 'Sulfur', 'S', '32.065', '16', '3'], 'Cl': ['17', 'Chlorine', 'Cl', '35.453', '17', '3'], 'Ar': ['18', 'Argon', 'Ar', '39.948', '18', '3'], 'K': ['19', 'Potassium', 'K', '39.0983', '1', '4'], 'Ca': ['20', 'Calcium', 'Ca', '40.078', '2', '4'], 'Sc': ['21', 'Scandium', 'Sc', '44.955912', '3', '4'], 'Ti': ['22', 'Titanium', 'Ti', '47.867', '4', '4'], 'V': ['23', 'Vanadium', 'V', '50.9415', '5', '4'], 'Cr': ['24', 'Chromium', 'Cr', '51.9961', '6', '4'], 'Mn': ['25', 'Manganese', 'Mn', '54.938045', '7', '4'], 'Fe': ['26', 'Iron', 'Fe', '55.845', '8', '4'], 'Co': ['27', 'Cobalt', 'Co', '58.933195', '9', '4'], 'Ni': ['28', 'Nickel', 'Ni', '58.6934', '10', '4'], 'Cu': ['29', 'Copper', 'Cu', '63.546', '11', '4'], 'Zn': ['30', 'Zinc', 'Zn', '65.409', '12', '4'], 'Ga': ['31', 'Gallium', 'Ga', '69.723', '13', '4'], 'Ge': ['32', 'Germanium', 'Ge', '72.64', '14', '4'], 'As': ['33', 'Arsenic', 'As', '74.92160', '15', '4'], 'Se': ['34', 'Selenium', 'Se', '78.96', '16', '4'], 'Br': ['35', 'Bromine', 'Br', '79.904', '17', '4'], 'Kr': ['36', 'Krypton', 'Kr', '83.798', '18', '4'], 'Rb': ['37', 'Rubidium', 'Rb', '85.4678', '1', '5'], 'Sr': ['38', 'Strontium', 'Sr', '87.62', '2', '5'], 'Y': ['39', 'Yttrium', 'Y', '88.90585', '3', '5'], 'Zr': ['40', 'Zirconium', 'Zr', '91.224', '4', '5'], 'Nb': ['41', 'Niobium', 'Nb', '92.90638', '5', '5'], 'Mo': ['42', 'Molybdenum', 'Mo', '95.94', '6', '5'], 'Tc': ['43', 'Technetium', 'Tc', '98', '7', '5'], 'Ru': ['44', 'Ruthenium', 'Ru', '101.07', '8', '5'], 'Rh': ['45', 'Rhodium', 'Rh', '102.905', '9', '5'], 'Pd': ['46', 'Palladium', 'Pd', '106.42', '10', '5'], 'Ag': ['47', 'Silver', 'Ag', '107.8682', '11', '5'], 'Cd': ['48', 'Cadmium', 'Cd', '112.411', '12', '5'], 'In': ['49', 'Indium', 'In', '114.818', '13', '5'], 'Sn': ['50', 'Tin', 'Sn', '118.710', '14', '5'], 'Sb': ['51', 'Antimony', 'Sb', '121.760', '15', '5'], 'Te': ['52', 'Tellurium', 'Te', '127.60', '16', '5'], 'I': ['53', 'Iodine', 'I', '126.904', '47', '17', '5'], 'Xe': ['54', 'Xenon', 'Xe', '131.293', '18', '5'], 'Cs': ['55', 'Caesium', 'Cs', '132.9054519', '1', '6'], 'Ba': ['56', 'Barium', 'Ba', '137.327', '2', '6'], 'La': ['57', 'Lanthanum', 'La', '138.90547', 'n/a', '6'], 'Ce': ['58', 'Cerium', 'Ce', '140.116', 'n/a', '6'], 'Pr': ['59', 'Praseodymium', 'Pr', '140.90765', 'n/a', '6'], 'Nd': ['60', 'Neodymium', 'Nd', '144.242', 'n/a', '6'], 'Pm': ['61', 'Promethium', 'Pm', '145', 'n/a', '6'], 'Sm': ['62', 'Samarium', 'Sm', '150.36', 'n/a', '6'], 'Eu': ['63', 'Europium', 'Eu', '151.964', 'n/a', '6'], 'Gd': ['64', 'Gadolinium', 'Gd', '157.25', 'n/a', '6'], 'Tb': ['65', 'Terbium', 'Tb', '158.92535', 'n/a', '6'], 'Dy': ['66', 'Dysprosium', 'Dy', '162.500', 'n/a', '6'], 'Ho': ['67', 'Holmium', 'Ho', '164.930', '32', 'n/a', '6'], 'Er': ['68', 'Erbium', 'Er', '167.259', 'n/a', '6'], 'Tm': ['69', 'Thulium', 'Tm', '168.93421', 'n/a', '6'], 'Yb': ['70', 'Ytterbium', 'Yb', '173.04', 'n/a', '6'], 'Lu': ['71', 'Lutetium', 'Lu', '174.967', '3', '6'], 'Hf': ['72', 'Hafnium', 'Hf', '178.49', '4', '6'], 'Ta': ['73', 'Tantalum', 'Ta', '180.94788', '5', '6'], 'W': ['74', 'Tungsten', 'W', '183.84', '6', '6'], 'Re': ['75', 'Rhenium', 'Re', '186.207', '7', '6'], 'Os': ['76', 'Osmium', 'Os', '190.23', '8', '6'], 'Ir': ['77', 'Iridium', 'Ir', '192.217', '9', '6'], 'Pt': ['78', 'Platinum', 'Pt', '195.084', '10', '6'], 'Au': ['79', 'Gold', 'Au', '196.966569', '11', '6'], 'Hg': ['80', 'Mercury', 'Hg', '200.59', '12', '6'], 'Tl': ['81', 'Thallium', 'Tl', '204.3833', '13', '6'], 'Pb': ['82', 'Lead', 'Pb', '207.2', '14', '6'], 'Bi': ['83', 'Bismuth', 'Bi', '208.98040', '15', '6'], 'Po': ['84', 'Polonium', 'Po', '210', '16', '6'], 'At': ['85', 'Astatine', 'At', '210', '17', '6'], 'Rn': ['86', 'Radon', 'Rn', '220', '18', '6'], 'Fr': ['87', 'Francium', 'Fr', '223', '1', '7'], 'Ra': ['88', 'Radium', 'Ra', '226', '2', '7'], 'Ac': ['89', 'Actinium', 'Ac', '227', 'n/a', '7'], 'Th': ['90', 'Thorium', 'Th', '232.03806', 'n/a', '7'], 'Pa': ['91', 'Protactinium', 'Pa', '231.03588', 'n/a', '7'], 'U': ['92', 'Uranium', 'U', '238.02891', 'n/a', '7'], 'Np': ['93', 'Neptunium', 'Np', '237', 'n/a', '7'], 'Pu': ['94', 'Plutonium', 'Pu', '244', 'n/a', '7'], 'Am': ['95', 'Americium', 'Am', '243', 'n/a', '7'], 'Cm': ['96', 'Curium', 'Cm', '247', 'n/a', '7'], 'Bk': ['97', 'Berkelium', 'Bk', '247', 'n/a', '7'], 'Cf': ['98', 'Californium', 'Cf', '251', 'n/a', '7'], 'Es': ['99', 'Einsteinium', 'Es', '252', 'n/a', '7'], 'Fm': ['100', 'Fermium', 'Fm', '257', 'n/a', '7'], 'Md': ['101', 'Mendelevium', 'Md', '258', 'n/a', '7'], 'No': ['102', 'Nobelium', 'No', '259', 'n/a', '7'], 'Lr': ['103', 'Lawrencium', 'Lr', '262', '3', '7'], 'Rf': ['104', 'Rutherfordium', 'Rf', '261', '4', '7'], 'Db': ['105', 'Dubnium', 'Db', '262', '5', '7'], 'Sg': ['106', 'Seaborgium', 'Sg', '266', '6', '7'], 'Bh': ['107', 'Bohrium', 'Bh', '264', '7', '7'], 'Hs': ['108', 'Hassium', 'Hs', '277', '8', '7'], 'Mt': ['109', 'Meitnerium', 'Mt', '268', '9', '7'], 'Ds': ['110', 'Darmstadtium', 'Ds', '271', '10', '7'], 'Rg': ['111', 'Roentgenium', 'Rg', '272', '11', '7'], 'Uub': ['112', 'Ununbium', 'Uub', '285', '12', '7'], 'Uut': ['113', 'Ununtrium', 'Uut', '284', '13', '7'], 'Uuq': ['114', 'Ununquadium', 'Uuq', '289', '14', '7'], 'Uup': ['115', 'Ununpentium', 'Uup', '288', '15', '7'], 'Uuh': ['116', 'Ununhexium', 'Uuh', '292', '16', '7'], 'Uuo': ['118', 'Ununoctium', 'Uuo', '294', '18', '7']}
        danZhiDensityDict = {'H': ['0.0899', 'g/L', 'Hydrogen', 'H', '1', '氢', '气'], 'Li': ['0.534', 'g/cc', 'Lithium', 'Li', '3', '锂'], 'Be': ['1.848', 'g/cc', 'Beryllium', 'Be', '4', '铍'], 'B': ['2.34', 'g/cc', 'Boron', 'B', '5', '硼'], 'C': ['2.26', 'g/cc', 'Carbon', 'C', '6', '碳'], 'N': ['1.2506', 'g/L', 'Nitrogen', 'N', '7', '氮', '气'], 'O': ['1.429', 'g/L', 'Oxygen', 'O', '8', '氧', '气'], 'F': ['1.696', 'g/L', 'Fluorine', 'F', '9', '氟', '气'], 'Ne': ['0.9', 'g/L', 'Neon', 'Ne', '10', '氖', '气'], 'Na': ['0.971', 'g/cc', 'Sodium', 'Na', '11', '钠'], 'Mg': ['1.738', 'g/cc', 'Magnesium', 'Mg', '12', '镁'], 'Al': ['2.702', 'g/cc', 'Aluminum', 'Al', '13', '铝'], 'Si': ['2.33', 'g/cc', 'Silicon', 'Si', '14', '硅'], 'P': ['1.82', 'g/cc', 'Phosphorus', 'P', '15', '磷'], 'S': ['2.07', 'g/cc', 'Sulfur', 'S', '16', '硫'], 'Cl': ['3.214', 'g/L', 'Chlorine', 'Cl', '17', '氯', '气'], 'Ar': ['1.7824', 'g/L', 'Argon', 'Ar', '18', '氩', '气'], 'K': ['0.862', 'g/cc', 'Potassium', 'K', '19', '钾'], 'Ca': ['1.55', 'g/cc', 'Calcium', 'Ca', '20', '钙'], 'Sc': ['2.99', 'g/cc', 'Scandium', 'Sc', '21', '钪'], 'Ti': ['4.54', 'g/cc', 'Titanium', 'Ti', '22', '钛'], 'V': ['6.11', 'g/cc', 'Vanadium', 'V', '23', '钒'], 'Cr': ['7.19', 'g/cc', 'Chromium', 'Cr', '24', '铬'], 'Mn': ['7.43', 'g/cc', 'Manganese', 'Mn', '25', '锰'], 'Fe': ['7.874', 'g/cc', 'Iron', 'Fe', '26', '铁'], 'Co': ['8.9', 'g/cc', 'Cobalt', 'Co', '27', '钴'], 'Ni': ['8.9', 'g/cc', 'Nickel', 'Ni', '28', '镍'], 'Cu': ['8.96', 'g/cc', 'Copper', 'Cu', '29', '铜'], 'Zn': ['7.13', 'g/cc', 'Zinc', 'Zn', '30', '锌'], 'Ga': ['5.907', 'g/cc', 'Gallium', 'Ga', '31', '镓'], 'Ge': ['5.323', 'g/cc', 'Germanium', 'Ge', '32', '锗'], 'As': ['5.72', 'g/cc', 'Arsenic', 'As', '33', '砷'], 'Se': ['4.79', 'g/cc', 'Selenium', 'Se', '34', '硒'], 'Br': ['3.119', 'g/cc', 'Bromine', 'Br', '35', '溴'], 'Kr': ['3.75', 'g/L', 'Krypton', 'Kr', '36', '氪', '气'], 'Rb': ['1.63', 'g/cc', 'Rubidium', 'Rb', '37', '铷'], 'Sr': ['2.54', 'g/cc', 'Strontium', 'Sr', '38', '锶'], 'Y': ['4.47', 'g/cc', 'Yttrium', 'Y', '39', '钇'], 'Zr': ['6.51', 'g/cc', 'Zirconium', 'Zr', '40', '锆'], 'Nb': ['8.57', 'g/cc', 'Niobium', 'Nb', '41', '铌'], 'Mo': ['10.22', 'g/cc', 'Molybdenum', 'Mo', '42', '钼'], 'Tc': ['11.5', 'g/cc', 'Technetium', 'Tc', '43', '锝'], 'Ru': ['12.37', 'g/cc', 'Ruthenium', 'Ru', '44', '钌'], 'Rh': ['12.41', 'g/cc', 'Rhodium', 'Rh', '45', '铑'], 'Pd': ['12.02', 'g/cc', 'Palladium', 'Pd', '46', '钯'], 'Ag': ['10.5', 'g/cc', 'Silver', 'Ag', '47', '银'], 'Cd': ['8.65', 'g/cc', 'Cadmium', 'Cd', '48', '镉'], 'In': ['7.31', 'g/cc', 'Indium', 'In', '49', '铟'], 'Sn': ['7.31', 'g/cc', 'Tin', 'Sn', '50', '锡'], 'Sb': ['6.684', 'g/cc', 'Antimony', 'Sb', '51', '锑'], 'Te': ['6.24', 'g/cc', 'Tellurium', 'Te', '52', '碲'], 'I': ['4.93', 'g/cc', 'Iodine', 'I', '53', '碘'], 'Xe': ['5.9', 'g/L', 'Xenon', 'Xe', '54', '氙(xian)', '气'], 'Cs': ['1.873', 'g/cc', 'Cesium', 'Cs', '55', '铯'], 'Ba': ['3.59', 'g/cc', 'Barium', 'Ba', '56', '钡'], 'La': ['6.15', 'g/cc', 'Lanthanum', 'La', '57', '镧'], 'Ce': ['6.77', 'g/cc', 'Cerium', 'Ce', '58', '铈'], 'Pr': ['6.77', 'g/cc', 'Praseodymium', 'Pr', '59', '镨'], 'Nd': ['7.01', 'g/cc', 'Neodymium', 'Nd', '60', '钕'], 'Pm': ['7.3', 'g/cc', 'Promethium', 'Pm', '61', '钷'], 'Sm': ['7.52', 'g/cc', 'Samarium', 'Sm', '62', '钐'], 'Eu': ['5.24', 'g/cc', 'Europium', 'Eu', '63', '铕'], 'Gd': ['7.895', 'g/cc', 'Gadolinium', 'Gd', '64', '钆'], 'Tb': ['8.23', 'g/cc', 'Terbium', 'Tb', '65', '铽'], 'Dy': ['8.55', 'g/cc', 'Dysprosium', 'Dy', '66', '镝'], 'Ho': ['8.8', 'g/cc', 'Holmium', 'Ho', '67', '钬'], 'Er': ['9.07', 'g/cc', 'Erbium', 'Er', '68', '铒'], 'Tm': ['9.32', 'g/cc', 'Thulium', 'Tm', '69', '铥'], 'Yb': ['6.9', 'g/cc', 'Ytterbium', 'Yb', '70', '镱'], 'Lu': ['9.84', 'g/cc', 'Lutetium', 'Lu', '71', '镥'], 'Hf': ['13.31', 'g/cc', 'Hafnium', 'Hf', '72', '铪(ha)'], 'Ta': ['16.65', 'g/cc', 'Tantalum', 'Ta', '73', '钽'], 'W': ['19.35', 'g/cc', 'Tungsten', 'W', '74', '钨'], 'Re': ['21.04', 'g/cc', 'Rhenium', 'Re', '75', '铼'], 'Os': ['22.6', 'g/cc', 'Osmium', 'Os', '76', '锇(e)'], 'Ir': ['22.4', 'g/cc', 'Iridium', 'Ir', '77', '铱'], 'Pt': ['21.45', 'g/cc', 'Platinum', 'Pt', '78', '铂'], 'Au': ['19.32', 'g/cc', 'Gold', 'Au', '79', '金'], 'Hg': ['13.546', 'g/cc', 'Mercury', 'Hg', '80', '汞'], 'Tl': ['11.85', 'g/cc', 'Thallium', 'Tl', '81', '铊(ta)'], 'Pb': ['11.35', 'g/cc', 'Lead', 'Pb', '82', '铅'], 'Bi': ['9.75', 'g/cc', 'Bismuth', 'Bi', '83', '铋'], 'Po': ['9.3', 'g/cc', 'Polonium', 'Po', '84', '钋(po)'], 'Rn': ['9.73', 'g/L', 'Radon', 'Rn', '86', '氡(dong)', '气'], 'Ra': ['5.5', 'g/cc', 'Radium', 'Ra', '88', '镭'], 'Ac': ['10.07', 'g/cc', 'Actinium', 'Ac', '89', '锕'], 'Th': ['11.724', 'g/cc', 'Thorium', 'Th', '90', '钍(tu)'], 'Pa': ['15.4', 'g/cc', 'Protactinium', 'Pa', '91', '镤(pu)'], 'U': ['18.95', 'g/cc', 'Uranium', 'U', '92', '铀'], 'Np': ['20.2', 'g/cc', 'Neptunium', 'Np', '93', '镎(na)'], 'Pu': ['19.84', 'g/cc', 'Plutonium', 'Pu', '94', '钚(bu)'], 'Am': ['13.67', 'g/cc', 'Americium', 'Am', '95', '镅(mei)'], 'Cm': ['13.5', 'g/cc', 'Curium', 'Cm', '96', '锔(ju)'], 'Bk': ['14.78', 'g/cc', 'Berkelium', 'Bk', '97', '锫(pei)'], 'Cf': ['15.1', 'g/cc', 'Californium', 'Cf', '98', '锎(kai)']}
        dataBaseFile1 = '49_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json'
        dataBaseFile2 = '49_[扩展-2化合物密度数据库]单质或化合物或多相混合体系密度计算.json'
        MoleMakeupDict = loadData(dataBaseFile1)   # 化合物原子组成数据库字典
        chemDensityDict = loadData(dataBaseFile2)  # 化合物密度数据库
        print('请输入想要基于factsage计算密度的化合物分子式，用英文逗号隔开，如 SiO2,CaO')
        compList = input().split(',')
        chemSpecieList = [i for i in compList if i not in list(atomMassDict.keys())]
        danZhiList = [i for i in compList if i in list(atomMassDict.keys())]
        print('输入的化合物和单质组元分别为：',chemSpecieList,danZhiList)
        if len(chemSpecieList) != 0:
            densityDict1 = ChemDensityCalc(atomMassDict,MoleMakeupDict,chemSpecieList)  # 09函数，基于factsage计算化合物密度,loadFileName是相对原子质量字典
        else:
            print('输入组元中不含化合物。')
            densityDict1 = {}
        if len(danZhiList) != 0:
            densityDict2 = danZhiDensityCalc(atomMassDict,danZhiList)  # 14函数，基于factsage计算单质密度，需要传入单质的相对原子质量字典atomMassDict和单质化学符号列表danZhiList。
        else:
            print('输入组元中不含单质。')
            densityDict2 = {}
        densityDict = {**densityDict1,**densityDict2}  # 单质密度字典和化合物密度字典进行拼接
        for i in list(densityDict.keys()):
            print('基于factsage体积数据计算的密度值为:',i,densityDict[i][0])
        for i in list(densityDict.keys()):
            if i in list(chemDensityDict.keys()):
                print('化合物密度数据库中存在该化合物密度数据',i,chemDensityDict[i][0])
            elif i in list(danZhiDensityDict.keys()):
                print('单质密度数据库中存在该化合物密度数据',i,danZhiDensityDict[i][0])
            else:
                print('单质和化合物密度数据库中均不存在该物质密度数据。',i)

    elif defChoose == "05":
        '''
        设置化合物原子组成喝密度数据库对应的json文件名
        '''
        dataBaseFile1 = '49_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json'
        dataBaseFile2 = '49_[扩展-2化合物密度数据库]单质或化合物或多相混合体系密度计算.json'

        """
        以下是氧化物和单质的相对原子质量和相对分子质量，相对原子质量的数据库是完善的，而相对分子质量的数据库是是根据相对原子质量数据库计算出来的
        """
        # 相对原子质量数据库,m1
        atomicMassSingleDict = {'H': ['1', 'Hydrogen', 'H', '1.00794', '1', '1'], 'He': ['2', 'Helium', 'He', '4.002602', '18', '1'], 'Li': ['3', 'Lithium', 'Li', '6.941', '1', '2'], 'Be': ['4', 'Beryllium', 'Be', '9.012182', '2', '2'], 'B': ['5', 'Boron', 'B', '10.811', '13', '2'], 'C': ['6', 'Carbon', 'C', '12.0107', '14', '2'], 'N': ['7', 'Nitrogen', 'N', '14.0067', '15', '2'], 'O': ['8', 'Oxygen', 'O', '15.9994', '16', '2'], 'F': ['9', 'Fluorine', 'F', '18.9984032', '17', '2'], 'Ne': ['10', 'Neon', 'Ne', '20.1797', '18', '2'], 'Na': ['11', 'Sodium', 'Na', '22.98976928', '1', '3'], 'Mg': ['12', 'Magnesium', 'Mg', '24.3050', '2', '3'], 'Al': ['13', 'Aluminium', 'Al', '26.9815386', '13', '3'], 'Si': ['14', 'Silicon', 'Si', '28.0855', '14', '3'], 'P': ['15', 'Phosphorus', 'P', '30.973762', '15', '3'], 'S': ['16', 'Sulfur', 'S', '32.065', '16', '3'], 'Cl': ['17', 'Chlorine', 'Cl', '35.453', '17', '3'], 'Ar': ['18', 'Argon', 'Ar', '39.948', '18', '3'], 'K': ['19', 'Potassium', 'K', '39.0983', '1', '4'], 'Ca': ['20', 'Calcium', 'Ca', '40.078', '2', '4'], 'Sc': ['21', 'Scandium', 'Sc', '44.955912', '3', '4'], 'Ti': ['22', 'Titanium', 'Ti', '47.867', '4', '4'], 'V': ['23', 'Vanadium', 'V', '50.9415', '5', '4'], 'Cr': ['24', 'Chromium', 'Cr', '51.9961', '6', '4'], 'Mn': ['25', 'Manganese', 'Mn', '54.938045', '7', '4'], 'Fe': ['26', 'Iron', 'Fe', '55.845', '8', '4'], 'Co': ['27', 'Cobalt', 'Co', '58.933195', '9', '4'], 'Ni': ['28', 'Nickel', 'Ni', '58.6934', '10', '4'], 'Cu': ['29', 'Copper', 'Cu', '63.546', '11', '4'], 'Zn': ['30', 'Zinc', 'Zn', '65.409', '12', '4'], 'Ga': ['31', 'Gallium', 'Ga', '69.723', '13', '4'], 'Ge': ['32', 'Germanium', 'Ge', '72.64', '14', '4'], 'As': ['33', 'Arsenic', 'As', '74.92160', '15', '4'], 'Se': ['34', 'Selenium', 'Se', '78.96', '16', '4'], 'Br': ['35', 'Bromine', 'Br', '79.904', '17', '4'], 'Kr': ['36', 'Krypton', 'Kr', '83.798', '18', '4'], 'Rb': ['37', 'Rubidium', 'Rb', '85.4678', '1', '5'], 'Sr': ['38', 'Strontium', 'Sr', '87.62', '2', '5'], 'Y': ['39', 'Yttrium', 'Y', '88.90585', '3', '5'], 'Zr': ['40', 'Zirconium', 'Zr', '91.224', '4', '5'], 'Nb': ['41', 'Niobium', 'Nb', '92.90638', '5', '5'], 'Mo': ['42', 'Molybdenum', 'Mo', '95.94', '6', '5'], 'Tc': ['43', 'Technetium', 'Tc', '98', '7', '5'], 'Ru': ['44', 'Ruthenium', 'Ru', '101.07', '8', '5'], 'Rh': ['45', 'Rhodium', 'Rh', '102.905', '9', '5'], 'Pd': ['46', 'Palladium', 'Pd', '106.42', '10', '5'], 'Ag': ['47', 'Silver', 'Ag', '107.8682', '11', '5'], 'Cd': ['48', 'Cadmium', 'Cd', '112.411', '12', '5'], 'In': ['49', 'Indium', 'In', '114.818', '13', '5'], 'Sn': ['50', 'Tin', 'Sn', '118.710', '14', '5'], 'Sb': ['51', 'Antimony', 'Sb', '121.760', '15', '5'], 'Te': ['52', 'Tellurium', 'Te', '127.60', '16', '5'], 'I': ['53', 'Iodine', 'I', '126.904', '47', '17', '5'], 'Xe': ['54', 'Xenon', 'Xe', '131.293', '18', '5'], 'Cs': ['55', 'Caesium', 'Cs', '132.9054519', '1', '6'], 'Ba': ['56', 'Barium', 'Ba', '137.327', '2', '6'], 'La': ['57', 'Lanthanum', 'La', '138.90547', 'n/a', '6'], 'Ce': ['58', 'Cerium', 'Ce', '140.116', 'n/a', '6'], 'Pr': ['59', 'Praseodymium', 'Pr', '140.90765', 'n/a', '6'], 'Nd': ['60', 'Neodymium', 'Nd', '144.242', 'n/a', '6'], 'Pm': ['61', 'Promethium', 'Pm', '145', 'n/a', '6'], 'Sm': ['62', 'Samarium', 'Sm', '150.36', 'n/a', '6'], 'Eu': ['63', 'Europium', 'Eu', '151.964', 'n/a', '6'], 'Gd': ['64', 'Gadolinium', 'Gd', '157.25', 'n/a', '6'], 'Tb': ['65', 'Terbium', 'Tb', '158.92535', 'n/a', '6'], 'Dy': ['66', 'Dysprosium', 'Dy', '162.500', 'n/a', '6'], 'Ho': ['67', 'Holmium', 'Ho', '164.930', '32', 'n/a', '6'], 'Er': ['68', 'Erbium', 'Er', '167.259', 'n/a', '6'], 'Tm': ['69', 'Thulium', 'Tm', '168.93421', 'n/a', '6'], 'Yb': ['70', 'Ytterbium', 'Yb', '173.04', 'n/a', '6'], 'Lu': ['71', 'Lutetium', 'Lu', '174.967', '3', '6'], 'Hf': ['72', 'Hafnium', 'Hf', '178.49', '4', '6'], 'Ta': ['73', 'Tantalum', 'Ta', '180.94788', '5', '6'], 'W': ['74', 'Tungsten', 'W', '183.84', '6', '6'], 'Re': ['75', 'Rhenium', 'Re', '186.207', '7', '6'], 'Os': ['76', 'Osmium', 'Os', '190.23', '8', '6'], 'Ir': ['77', 'Iridium', 'Ir', '192.217', '9', '6'], 'Pt': ['78', 'Platinum', 'Pt', '195.084', '10', '6'], 'Au': ['79', 'Gold', 'Au', '196.966569', '11', '6'], 'Hg': ['80', 'Mercury', 'Hg', '200.59', '12', '6'], 'Tl': ['81', 'Thallium', 'Tl', '204.3833', '13', '6'], 'Pb': ['82', 'Lead', 'Pb', '207.2', '14', '6'], 'Bi': ['83', 'Bismuth', 'Bi', '208.98040', '15', '6'], 'Po': ['84', 'Polonium', 'Po', '210', '16', '6'], 'At': ['85', 'Astatine', 'At', '210', '17', '6'], 'Rn': ['86', 'Radon', 'Rn', '220', '18', '6'], 'Fr': ['87', 'Francium', 'Fr', '223', '1', '7'], 'Ra': ['88', 'Radium', 'Ra', '226', '2', '7'], 'Ac': ['89', 'Actinium', 'Ac', '227', 'n/a', '7'], 'Th': ['90', 'Thorium', 'Th', '232.03806', 'n/a', '7'], 'Pa': ['91', 'Protactinium', 'Pa', '231.03588', 'n/a', '7'], 'U': ['92', 'Uranium', 'U', '238.02891', 'n/a', '7'], 'Np': ['93', 'Neptunium', 'Np', '237', 'n/a', '7'], 'Pu': ['94', 'Plutonium', 'Pu', '244', 'n/a', '7'], 'Am': ['95', 'Americium', 'Am', '243', 'n/a', '7'], 'Cm': ['96', 'Curium', 'Cm', '247', 'n/a', '7'], 'Bk': ['97', 'Berkelium', 'Bk', '247', 'n/a', '7'], 'Cf': ['98', 'Californium', 'Cf', '251', 'n/a', '7'], 'Es': ['99', 'Einsteinium', 'Es', '252', 'n/a', '7'], 'Fm': ['100', 'Fermium', 'Fm', '257', 'n/a', '7'], 'Md': ['101', 'Mendelevium', 'Md', '258', 'n/a', '7'], 'No': ['102', 'Nobelium', 'No', '259', 'n/a', '7'], 'Lr': ['103', 'Lawrencium', 'Lr', '262', '3', '7'], 'Rf': ['104', 'Rutherfordium', 'Rf', '261', '4', '7'], 'Db': ['105', 'Dubnium', 'Db', '262', '5', '7'], 'Sg': ['106', 'Seaborgium', 'Sg', '266', '6', '7'], 'Bh': ['107', 'Bohrium', 'Bh', '264', '7', '7'], 'Hs': ['108', 'Hassium', 'Hs', '277', '8', '7'], 'Mt': ['109', 'Meitnerium', 'Mt', '268', '9', '7'], 'Ds': ['110', 'Darmstadtium', 'Ds', '271', '10', '7'], 'Rg': ['111', 'Roentgenium', 'Rg', '272', '11', '7'], 'Uub': ['112', 'Ununbium', 'Uub', '285', '12', '7'], 'Uut': ['113', 'Ununtrium', 'Uut', '284', '13', '7'], 'Uuq': ['114', 'Ununquadium', 'Uuq', '289', '14', '7'], 'Uup': ['115', 'Ununpentium', 'Uup', '288', '15', '7'], 'Uuh': ['116', 'Ununhexium', 'Uuh', '292', '16', '7'], 'Uuo': ['118', 'Ununoctium', 'Uuo', '294', '18', '7']}
        elementDict = strToDict()                                              # 调用05函数，提示输入相应字符串，转化为对应字典
        atomMakeupDict_result = atomMakeupDict(atomicMassSingleDict,dataBaseFile1,elementDict)   # 调用10函数，返回所有json以及新添加的化合物组成字典
        atomDict = atomMakeupDict_result[0]                                    # 返回更新后的化合物原子组成字典
        chemSubList = atomMakeupDict_result[1]                                 # 返回输入的化合物分子式列表
        
        # 接下来是调用04函数moleMassCalc()计算输入的所有化合物的相对分子质量
        # atomicMassOxideDict是相对分子质量数据库字典，形式如下一行所示，该数据库是建立在相对原子质量数据库的基础之上，通过调用04函数moleMassCalc()实现。
        # atomicMassOxideDict = {'SiO2': ['1', 'null', 'SiO2', '60.0843'], 'CaO': ['2', 'null', 'CaO', '56.077400000000004'], 'MgO': ['3', 'null', 'MgO', '40.3044'], 'Al2O3': ['4', 'null', 'Al2O3', '101.9612772'], 'B2O3': ['5', 'null', 'B2O3', '69.6202'], 'Fe2O3': ['6', 'null', 'Fe2O3', '159.6882'], 'Na2O': ['7', 'null', 'Na2O', '61.97893856'], 'CaF2': ['8', 'null', 'CaF2', '78.0748064'], 'TiO2': ['9', 'null', 'TiO2', '79.8658'], 'ZrO2': ['10', 'null', 'ZrO2', '123.2228'], 'NaF': ['11', 'null', 'NaF', '41.98817248'], 'P2O5': ['12', 'null', 'P2O5', '141.944524'], 'MnO2': ['13', 'null', 'MnO2', '86.936845'], 'K2O': ['14', 'null', 'K2O', '94.196'], 'V2O5': ['15', 'null', 'V2O5', '181.88'], 'CuO': ['16', 'null', 'CuO', '79.5454'], 'Li2O': ['17', 'null', 'Li2O', '29.8814'], 'Cr2O3': ['18', 'null', 'Cr2O3', '151.9904']}
        # 实参chemSubList是输入的化合物分子式列表
        atomicMassOxideDict = moleMassCalc(atomicMassSingleDict,atomDict,chemSubList)            # 调用04函数，返回化合物的相对分子质量字典,即对应chemSubList列表中化合物的相对分子质量字典
        
        # 相对原子质量和相对分子质量混合数据库
        mixOxideSimpleSubstanceAtomicMassDict = {**atomicMassSingleDict,**atomicMassOxideDict}   # 上述两种字典的组合，相对原子质量和相对分子质量混合数据库
        # mixOxideSimpleSubstanceAtomicMassDict = {**atomicMassSingleDict,**atomDict}  # 氧化物的相对分子质量字典暂时用氧化物的原子构成字典替代
    
        '''
        以下是单质和化合物密度数据库
        '''
    
        # 请注意pureDensityGasDict纯物质密度数据库中 H,N,O,F,Ne,Cl,Ar,Kr,Xe,Rn为气态密度
        # 数据库1
        pureDensityGasDict = {'H': ['0.0899', 'g/L', 'Hydrogen', 'H', '1', '氢', '气'], 'Li': ['0.534', 'g/cc', 'Lithium', 'Li', '3', '锂'], 'Be': ['1.848', 'g/cc', 'Beryllium', 'Be', '4', '铍'], 'B': ['2.34', 'g/cc', 'Boron', 'B', '5', '硼'], 'C': ['2.26', 'g/cc', 'Carbon', 'C', '6', '碳'], 'N': ['1.2506', 'g/L', 'Nitrogen', 'N', '7', '氮', '气'], 'O': ['1.429', 'g/L', 'Oxygen', 'O', '8', '氧', '气'], 'F': ['1.696', 'g/L', 'Fluorine', 'F', '9', '氟', '气'], 'Ne': ['0.9', 'g/L', 'Neon', 'Ne', '10', '氖', '气'], 'Na': ['0.971', 'g/cc', 'Sodium', 'Na', '11', '钠'], 'Mg': ['1.738', 'g/cc', 'Magnesium', 'Mg', '12', '镁'], 'Al': ['2.702', 'g/cc', 'Aluminum', 'Al', '13', '铝'], 'Si': ['2.33', 'g/cc', 'Silicon', 'Si', '14', '硅'], 'P': ['1.82', 'g/cc', 'Phosphorus', 'P', '15', '磷'], 'S': ['2.07', 'g/cc', 'Sulfur', 'S', '16', '硫'], 'Cl': ['3.214', 'g/L', 'Chlorine', 'Cl', '17', '氯', '气'], 'Ar': ['1.7824', 'g/L', 'Argon', 'Ar', '18', '氩', '气'], 'K': ['0.862', 'g/cc', 'Potassium', 'K', '19', '钾'], 'Ca': ['1.55', 'g/cc', 'Calcium', 'Ca', '20', '钙'], 'Sc': ['2.99', 'g/cc', 'Scandium', 'Sc', '21', '钪'], 'Ti': ['4.54', 'g/cc', 'Titanium', 'Ti', '22', '钛'], 'V': ['6.11', 'g/cc', 'Vanadium', 'V', '23', '钒'], 'Cr': ['7.19', 'g/cc', 'Chromium', 'Cr', '24', '铬'], 'Mn': ['7.43', 'g/cc', 'Manganese', 'Mn', '25', '锰'], 'Fe': ['7.874', 'g/cc', 'Iron', 'Fe', '26', '铁'], 'Co': ['8.9', 'g/cc', 'Cobalt', 'Co', '27', '钴'], 'Ni': ['8.9', 'g/cc', 'Nickel', 'Ni', '28', '镍'], 'Cu': ['8.96', 'g/cc', 'Copper', 'Cu', '29', '铜'], 'Zn': ['7.13', 'g/cc', 'Zinc', 'Zn', '30', '锌'], 'Ga': ['5.907', 'g/cc', 'Gallium', 'Ga', '31', '镓'], 'Ge': ['5.323', 'g/cc', 'Germanium', 'Ge', '32', '锗'], 'As': ['5.72', 'g/cc', 'Arsenic', 'As', '33', '砷'], 'Se': ['4.79', 'g/cc', 'Selenium', 'Se', '34', '硒'], 'Br': ['3.119', 'g/cc', 'Bromine', 'Br', '35', '溴'], 'Kr': ['3.75', 'g/L', 'Krypton', 'Kr', '36', '氪', '气'], 'Rb': ['1.63', 'g/cc', 'Rubidium', 'Rb', '37', '铷'], 'Sr': ['2.54', 'g/cc', 'Strontium', 'Sr', '38', '锶'], 'Y': ['4.47', 'g/cc', 'Yttrium', 'Y', '39', '钇'], 'Zr': ['6.51', 'g/cc', 'Zirconium', 'Zr', '40', '锆'], 'Nb': ['8.57', 'g/cc', 'Niobium', 'Nb', '41', '铌'], 'Mo': ['10.22', 'g/cc', 'Molybdenum', 'Mo', '42', '钼'], 'Tc': ['11.5', 'g/cc', 'Technetium', 'Tc', '43', '锝'], 'Ru': ['12.37', 'g/cc', 'Ruthenium', 'Ru', '44', '钌'], 'Rh': ['12.41', 'g/cc', 'Rhodium', 'Rh', '45', '铑'], 'Pd': ['12.02', 'g/cc', 'Palladium', 'Pd', '46', '钯'], 'Ag': ['10.5', 'g/cc', 'Silver', 'Ag', '47', '银'], 'Cd': ['8.65', 'g/cc', 'Cadmium', 'Cd', '48', '镉'], 'In': ['7.31', 'g/cc', 'Indium', 'In', '49', '铟'], 'Sn': ['7.31', 'g/cc', 'Tin', 'Sn', '50', '锡'], 'Sb': ['6.684', 'g/cc', 'Antimony', 'Sb', '51', '锑'], 'Te': ['6.24', 'g/cc', 'Tellurium', 'Te', '52', '碲'], 'I': ['4.93', 'g/cc', 'Iodine', 'I', '53', '碘'], 'Xe': ['5.9', 'g/L', 'Xenon', 'Xe', '54', '氙(xian)', '气'], 'Cs': ['1.873', 'g/cc', 'Cesium', 'Cs', '55', '铯'], 'Ba': ['3.59', 'g/cc', 'Barium', 'Ba', '56', '钡'], 'La': ['6.15', 'g/cc', 'Lanthanum', 'La', '57', '镧'], 'Ce': ['6.77', 'g/cc', 'Cerium', 'Ce', '58', '铈'], 'Pr': ['6.77', 'g/cc', 'Praseodymium', 'Pr', '59', '镨'], 'Nd': ['7.01', 'g/cc', 'Neodymium', 'Nd', '60', '钕'], 'Pm': ['7.3', 'g/cc', 'Promethium', 'Pm', '61', '钷'], 'Sm': ['7.52', 'g/cc', 'Samarium', 'Sm', '62', '钐'], 'Eu': ['5.24', 'g/cc', 'Europium', 'Eu', '63', '铕'], 'Gd': ['7.895', 'g/cc', 'Gadolinium', 'Gd', '64', '钆'], 'Tb': ['8.23', 'g/cc', 'Terbium', 'Tb', '65', '铽'], 'Dy': ['8.55', 'g/cc', 'Dysprosium', 'Dy', '66', '镝'], 'Ho': ['8.8', 'g/cc', 'Holmium', 'Ho', '67', '钬'], 'Er': ['9.07', 'g/cc', 'Erbium', 'Er', '68', '铒'], 'Tm': ['9.32', 'g/cc', 'Thulium', 'Tm', '69', '铥'], 'Yb': ['6.9', 'g/cc', 'Ytterbium', 'Yb', '70', '镱'], 'Lu': ['9.84', 'g/cc', 'Lutetium', 'Lu', '71', '镥'], 'Hf': ['13.31', 'g/cc', 'Hafnium', 'Hf', '72', '铪(ha)'], 'Ta': ['16.65', 'g/cc', 'Tantalum', 'Ta', '73', '钽'], 'W': ['19.35', 'g/cc', 'Tungsten', 'W', '74', '钨'], 'Re': ['21.04', 'g/cc', 'Rhenium', 'Re', '75', '铼'], 'Os': ['22.6', 'g/cc', 'Osmium', 'Os', '76', '锇(e)'], 'Ir': ['22.4', 'g/cc', 'Iridium', 'Ir', '77', '铱'], 'Pt': ['21.45', 'g/cc', 'Platinum', 'Pt', '78', '铂'], 'Au': ['19.32', 'g/cc', 'Gold', 'Au', '79', '金'], 'Hg': ['13.546', 'g/cc', 'Mercury', 'Hg', '80', '汞'], 'Tl': ['11.85', 'g/cc', 'Thallium', 'Tl', '81', '铊(ta)'], 'Pb': ['11.35', 'g/cc', 'Lead', 'Pb', '82', '铅'], 'Bi': ['9.75', 'g/cc', 'Bismuth', 'Bi', '83', '铋'], 'Po': ['9.3', 'g/cc', 'Polonium', 'Po', '84', '钋(po)'], 'Rn': ['9.73', 'g/L', 'Radon', 'Rn', '86', '氡(dong)', '气'], 'Ra': ['5.5', 'g/cc', 'Radium', 'Ra', '88', '镭'], 'Ac': ['10.07', 'g/cc', 'Actinium', 'Ac', '89', '锕'], 'Th': ['11.724', 'g/cc', 'Thorium', 'Th', '90', '钍(tu)'], 'Pa': ['15.4', 'g/cc', 'Protactinium', 'Pa', '91', '镤(pu)'], 'U': ['18.95', 'g/cc', 'Uranium', 'U', '92', '铀'], 'Np': ['20.2', 'g/cc', 'Neptunium', 'Np', '93', '镎(na)'], 'Pu': ['19.84', 'g/cc', 'Plutonium', 'Pu', '94', '钚(bu)'], 'Am': ['13.67', 'g/cc', 'Americium', 'Am', '95', '镅(mei)'], 'Cm': ['13.5', 'g/cc', 'Curium', 'Cm', '96', '锔(ju)'], 'Bk': ['14.78', 'g/cc', 'Berkelium', 'Bk', '97', '锫(pei)'], 'Cf': ['15.1', 'g/cc', 'Californium', 'Cf', '98', '锎(kai)']}
        # 请注意pureDensitySolidDict纯物质密度数据库中 H,N,O,F,Ne,Cl,Ar为固态密度
        # 数据库2
        pureDensitySolidDict = {'H': ['0.0899', 'g/L', 'Hydrogen', 'H', '1', '氢', '气'], 'Li': ['0.534', 'g/cc', 'Lithium', 'Li', '3', '锂'], 'Be': ['1.848', 'g/cc', 'Beryllium', 'Be', '4', '铍'], 'B': ['2.34', 'g/cc', 'Boron', 'B', '5', '硼'], 'C': ['2.26', 'g/cc', 'Carbon', 'C', '6', '碳'], 'N': ['1.2506', 'g/L', 'Nitrogen', 'N', '7', '氮', '气'], 'O': ['1.429', 'g/L', 'Oxygen', 'O', '8', '氧', '气'], 'F': ['1.696', 'g/L', 'Fluorine', 'F', '9', '氟', '气'], 'Ne': ['0.9', 'g/L', 'Neon', 'Ne', '10', '氖', '气'], 'Na': ['0.971', 'g/cc', 'Sodium', 'Na', '11', '钠'], 'Mg': ['1.738', 'g/cc', 'Magnesium', 'Mg', '12', '镁'], 'Al': ['2.702', 'g/cc', 'Aluminum', 'Al', '13', '铝'], 'Si': ['2.33', 'g/cc', 'Silicon', 'Si', '14', '硅'], 'P': ['1.82', 'g/cc', 'Phosphorus', 'P', '15', '磷'], 'S': ['2.07', 'g/cc', 'Sulfur', 'S', '16', '硫'], 'Cl': ['3.214', 'g/L', 'Chlorine', 'Cl', '17', '氯', '气'], 'Ar': ['1.7824', 'g/L', 'Argon', 'Ar', '18', '氩', '气'], 'K': ['0.862', 'g/cc', 'Potassium', 'K', '19', '钾'], 'Ca': ['1.55', 'g/cc', 'Calcium', 'Ca', '20', '钙'], 'Sc': ['2.99', 'g/cc', 'Scandium', 'Sc', '21', '钪'], 'Ti': ['4.54', 'g/cc', 'Titanium', 'Ti', '22', '钛'], 'V': ['6.11', 'g/cc', 'Vanadium', 'V', '23', '钒'], 'Cr': ['7.19', 'g/cc', 'Chromium', 'Cr', '24', '铬'], 'Mn': ['7.43', 'g/cc', 'Manganese', 'Mn', '25', '锰'], 'Fe': ['7.874', 'g/cc', 'Iron', 'Fe', '26', '铁'], 'Co': ['8.9', 'g/cc', 'Cobalt', 'Co', '27', '钴'], 'Ni': ['8.9', 'g/cc', 'Nickel', 'Ni', '28', '镍'], 'Cu': ['8.96', 'g/cc', 'Copper', 'Cu', '29', '铜'], 'Zn': ['7.13', 'g/cc', 'Zinc', 'Zn', '30', '锌'], 'Ga': ['5.907', 'g/cc', 'Gallium', 'Ga', '31', '镓'], 'Ge': ['5.323', 'g/cc', 'Germanium', 'Ge', '32', '锗'], 'As': ['5.72', 'g/cc', 'Arsenic', 'As', '33', '砷'], 'Se': ['4.79', 'g/cc', 'Selenium', 'Se', '34', '硒'], 'Br': ['3.119', 'g/cc', 'Bromine', 'Br', '35', '溴'], 'Kr': ['3.75', 'g/L', 'Krypton', 'Kr', '36', '氪', '气'], 'Rb': ['1.63', 'g/cc', 'Rubidium', 'Rb', '37', '铷'], 'Sr': ['2.54', 'g/cc', 'Strontium', 'Sr', '38', '锶'], 'Y': ['4.47', 'g/cc', 'Yttrium', 'Y', '39', '钇'], 'Zr': ['6.51', 'g/cc', 'Zirconium', 'Zr', '40', '锆'], 'Nb': ['8.57', 'g/cc', 'Niobium', 'Nb', '41', '铌'], 'Mo': ['10.22', 'g/cc', 'Molybdenum', 'Mo', '42', '钼'], 'Tc': ['11.5', 'g/cc', 'Technetium', 'Tc', '43', '锝'], 'Ru': ['12.37', 'g/cc', 'Ruthenium', 'Ru', '44', '钌'], 'Rh': ['12.41', 'g/cc', 'Rhodium', 'Rh', '45', '铑'], 'Pd': ['12.02', 'g/cc', 'Palladium', 'Pd', '46', '钯'], 'Ag': ['10.5', 'g/cc', 'Silver', 'Ag', '47', '银'], 'Cd': ['8.65', 'g/cc', 'Cadmium', 'Cd', '48', '镉'], 'In': ['7.31', 'g/cc', 'Indium', 'In', '49', '铟'], 'Sn': ['7.31', 'g/cc', 'Tin', 'Sn', '50', '锡'], 'Sb': ['6.684', 'g/cc', 'Antimony', 'Sb', '51', '锑'], 'Te': ['6.24', 'g/cc', 'Tellurium', 'Te', '52', '碲'], 'I': ['4.93', 'g/cc', 'Iodine', 'I', '53', '碘'], 'Xe': ['5.9', 'g/L', 'Xenon', 'Xe', '54', '氙(xian)', '气'], 'Cs': ['1.873', 'g/cc', 'Cesium', 'Cs', '55', '铯'], 'Ba': ['3.59', 'g/cc', 'Barium', 'Ba', '56', '钡'], 'La': ['6.15', 'g/cc', 'Lanthanum', 'La', '57', '镧'], 'Ce': ['6.77', 'g/cc', 'Cerium', 'Ce', '58', '铈'], 'Pr': ['6.77', 'g/cc', 'Praseodymium', 'Pr', '59', '镨'], 'Nd': ['7.01', 'g/cc', 'Neodymium', 'Nd', '60', '钕'], 'Pm': ['7.3', 'g/cc', 'Promethium', 'Pm', '61', '钷'], 'Sm': ['7.52', 'g/cc', 'Samarium', 'Sm', '62', '钐'], 'Eu': ['5.24', 'g/cc', 'Europium', 'Eu', '63', '铕'], 'Gd': ['7.895', 'g/cc', 'Gadolinium', 'Gd', '64', '钆'], 'Tb': ['8.23', 'g/cc', 'Terbium', 'Tb', '65', '铽'], 'Dy': ['8.55', 'g/cc', 'Dysprosium', 'Dy', '66', '镝'], 'Ho': ['8.8', 'g/cc', 'Holmium', 'Ho', '67', '钬'], 'Er': ['9.07', 'g/cc', 'Erbium', 'Er', '68', '铒'], 'Tm': ['9.32', 'g/cc', 'Thulium', 'Tm', '69', '铥'], 'Yb': ['6.9', 'g/cc', 'Ytterbium', 'Yb', '70', '镱'], 'Lu': ['9.84', 'g/cc', 'Lutetium', 'Lu', '71', '镥'], 'Hf': ['13.31', 'g/cc', 'Hafnium', 'Hf', '72', '铪(ha)'], 'Ta': ['16.65', 'g/cc', 'Tantalum', 'Ta', '73', '钽'], 'W': ['19.35', 'g/cc', 'Tungsten', 'W', '74', '钨'], 'Re': ['21.04', 'g/cc', 'Rhenium', 'Re', '75', '铼'], 'Os': ['22.6', 'g/cc', 'Osmium', 'Os', '76', '锇(e)'], 'Ir': ['22.4', 'g/cc', 'Iridium', 'Ir', '77', '铱'], 'Pt': ['21.45', 'g/cc', 'Platinum', 'Pt', '78', '铂'], 'Au': ['19.32', 'g/cc', 'Gold', 'Au', '79', '金'], 'Hg': ['13.546', 'g/cc', 'Mercury', 'Hg', '80', '汞'], 'Tl': ['11.85', 'g/cc', 'Thallium', 'Tl', '81', '铊(ta)'], 'Pb': ['11.35', 'g/cc', 'Lead', 'Pb', '82', '铅'], 'Bi': ['9.75', 'g/cc', 'Bismuth', 'Bi', '83', '铋'], 'Po': ['9.3', 'g/cc', 'Polonium', 'Po', '84', '钋(po)'], 'Rn': ['9.73', 'g/L', 'Radon', 'Rn', '86', '氡(dong)', '气'], 'Ra': ['5.5', 'g/cc', 'Radium', 'Ra', '88', '镭'], 'Ac': ['10.07', 'g/cc', 'Actinium', 'Ac', '89', '锕'], 'Th': ['11.724', 'g/cc', 'Thorium', 'Th', '90', '钍(tu)'], 'Pa': ['15.4', 'g/cc', 'Protactinium', 'Pa', '91', '镤(pu)'], 'U': ['18.95', 'g/cc', 'Uranium', 'U', '92', '铀'], 'Np': ['20.2', 'g/cc', 'Neptunium', 'Np', '93', '镎(na)'], 'Pu': ['19.84', 'g/cc', 'Plutonium', 'Pu', '94', '钚(bu)'], 'Am': ['13.67', 'g/cc', 'Americium', 'Am', '95', '镅(mei)'], 'Cm': ['13.5', 'g/cc', 'Curium', 'Cm', '96', '锔(ju)'], 'Bk': ['14.78', 'g/cc', 'Berkelium', 'Bk', '97', '锫(pei)'], 'Cf': ['15.1', 'g/cc', 'Californium', 'Cf', '98', '锎(kai)']}
        # 纯氧化物密度数据库
        # 数据库3，(纯固态氧化物密度数据库)，参考手册 The Oxide Handbook，HRC等，该方法计算出来的密度偏大
        pureSolidOxideDensityDict = {'SiO2': ['2.32', 'g/cm3', 'null', 'SiO2', 'null', 'null', 'null'], 'CaO': ['3.4', 'g/cm3', 'null', 'CaO', 'null', 'null', 'null'], 'MgO': ['3.65', 'g/cm3', 'null', 'MgO', 'null', 'null', 'null'], 'Al2O3': ['3.97', 'g/cm3', 'null', 'Al2O3', 'null', 'null', 'null'], 'B2O3': ['1.844', 'g/cm3', 'null', 'B2O3', 'null', 'null', 'null'], 'Fe2O3': ['5.24', 'g/cm3', 'null', 'Fe2O3', 'null', 'null', 'null'], 'Na2O2': ['2.805', 'g/cm3', 'null', 'Na2O2', 'null', 'null', 'null'], 'CaF2': ['null', 'g/cm3', 'null', 'CaF2', 'null', 'null', 'null'], 'TiO2': ['4.17', 'g/cm3', 'null', 'TiO2', 'null', 'null', 'null'], 'ZrO2': ['5.56', 'g/cm3', 'null', 'ZrO2', 'null', 'null', 'null'], 'NaF': ['null', 'g/cm3', 'null', 'NaF', 'null', 'null', 'null'], 'P2O5': ['null', 'g/cm3', 'null', 'P2O5', 'null', 'null', 'null'], 'MnO2': ['5.026', 'g/cm3', 'null', 'MnO2', 'null', 'null', 'null'], 'K2O': ['2.32', 'g/cm3', 'null', 'K2O', 'null', 'null', 'null'], 'V2O5': ['3.32', 'g/cm3', 'null', 'V2O5', 'null', 'null', 'null'], 'CuO': ['6.4', 'g/cm3', 'null', 'CuO', 'null', 'null', 'null'], 'Li2O': ['null', 'g/cm3', 'null', 'Li2O', 'null', 'null', 'null'], 'Cr2O3': ['5.21', 'g/cm3', 'null', 'Cr2O3', 'null', 'null', 'null']}  # 参考手册
    
        # 数据库4 (纯液态氧化物密度数据库,编号：d4), 源于factsage倒推修正,1800k，数据库4的内容对应于json化合物密度数据
        # pureLiquidOxideDensityFactsageDict ={'SiO2': ['2.335', 'g/cm3', 'null', 'SiO2', 'null', 'null', 'null'],'CaO': ['2.8581', 'g/cm3', 'null', 'CaO', 'null', 'null', 'null'],'B2O3': ['2.55', 'g/cm3', 'null', 'B2O3', 'null', 'null', 'null'],'V2O5': ['3.357', 'g/cm3', 'null', 'V2O5', 'null', 'null', 'null'],'MnO2': ['5.2', 'g/cm3', 'null', 'MnO2', 'null', 'null', 'null'],'Fe2O3': ['5.277', 'g/cm3', 'null', 'Fe2O3', 'null', 'null', 'null']}
        # pureLiquidOxideDensityFactsageDict = loadData(dataBaseFile2)  # 调用化合物密度字典数据库json
    
        # 数据库5，暂时为空
        pureOxideDensityMSDict = {}
        
        # 调用08函数 whetherInDatabase()判断输入的组元是否都存在于密度数据库中（单质或化合物数据库），对于不在的提示基于factsage计算密度或手动录入密度
        pureDensityDict = pureDensityGasDict            # 选择单质数据库1
        densityFile = dataBaseFile2 
        # 实参elementDict 是函数05返回的字典，即输入的组元组成字典
        pureLiquidOxideDensityFactsageDict = whetherInDatabase(pureDensityDict,densityFile,atomicMassSingleDict,atomDict,elementDict)
        
        # 数据库6 金属和氧化物混合体系密度数据库, 源于数据库1和4组合，数据库4是调用08函数返回的化合物密度字典，主要源于json文件
        mixOxideSimpleSubstanceDensityDict = {**pureDensityGasDict,**pureLiquidOxideDensityFactsageDict}   # 这个是单质和化合物混合密度数据库
    
        print('\n--------------------------------------------------------------------')
    
        print("""
        请选择单质数据库，1 2, or 3?  
        1= pureDensityGasDict                  (单质密度数据库，适用于合金熔体体系，暂不能计算含有H,N,O,F,Cl,Ar等元素的混合体系密度),
        2= pureDensitySolidDict                (单质密度数据库，适用于熔体体系中含有H,N,O,F,Cl,Ar等非金属元素体系)，非金属元素的密度基于氧化物密度倒推校正获得，暂不完善
    
        3= pureSolidOxideDensityDict           (纯固态氧化物密度数据库)，参考手册 The Oxide Handbook，HRC等
        4= pureLiquidOxideDensityFactsageDict  (纯液态氧化物密度数据库), 源于factsage倒退修正,1800k,数据库位于json文件中
        5= pureOxideDensityMSDict              (纯固态氧化物密度数据库),参考 Material Project晶体结构数据库
    
        6= mixOxideSimpleSubstanceDensityDict  (金属和氧化物混合体系密度数据库，适合两相混合体系计算，参考1和4)，推荐使用该数据库
        注意：合金混合体系相对分子质量计算和Factsage密度计算可以任选1和2数据库,单质和化合物混合体系使用数据库6, 数据库5暂时不要用
              """)
        databaseChoice = int(input())
    
        if databaseChoice == 1:                       # 单质密度数据库
            pureDensityDict = pureDensityGasDict
            atomicMassDict = atomicMassSingleDict
        elif databaseChoice == 2:                     # 单质密度数据库
            pureDensityDict = pureDensitySolidDict
            atomicMassDict = atomicMassSingleDict
        elif databaseChoice == 3:                     # 纯固态氧化物密度数据库
            pureDensityDict = pureSolidOxideDensityDict
            atomicMassDict = atomicMassOxideDict      # 分子化学式的相对分子质量
        elif databaseChoice == 4:                     # 纯液态氧化物密度数据库
            pureDensityDict = pureLiquidOxideDensityFactsageDict
            atomicMassDict = atomicMassOxideDict      # 分子化学式的相对分子质量
        elif databaseChoice == 5:                     # 纯固态氧化物密度数据库
            pureDensityDict = pureOxideDensityMSDict
            atomicMassDict = atomicMassOxideDict      # 分子化学式的相对分子质量
        elif databaseChoice == 6:                                  
            pureDensityDict = mixOxideSimpleSubstanceDensityDict   # 金属和氧化物混合体系密度数据库 
            atomicMassDict = mixOxideSimpleSubstanceAtomicMassDict # 相对原子质量和相对分子质量混合数据库
        else:
            print("您选择的数据库超出范围，请重新选择")
            sys.exit("404")
    
    
        saveDict = densityMixCalc(atomicMassDict,pureDensityDict,elementDict)   # 调用06函数，计算混合体系密度，需要知道所有组元的相对质量和密度
        factDensityCalc(saveDict)  # 调用07函数，基于factsage计算混合密度

    
    else:
        print("提示：您选择的功能正在开发，请重新选择！")






