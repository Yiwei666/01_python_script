# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:05:42 2022

@author: sun78
"""
"""
每次使用前注意查看1和2的提示
"""

# '': {'':'','':'','total':''}

import json
import sys


# 04函数，将数据从json文件读取到内存中
def loadData():                                # 将数据从json文件读取到内存中
    filename = '42_[扩展-数据库]化合物各类原子数统计.json' # 对应本脚本的数据库文件名字
    with open(filename,'r') as f:              # r 以只读方式打开文件。
        allData = json.load(f)
    print('从json文件中读取到内存的数据: ',allData)
    print('---------------从json文件中读取到内存的字典键---------------: ',list(allData.keys()))   # 注意是字典形式
    return allData                             # 返回被加载的数据

# 05函数，将数据写入到json文件中，数据可以是字典
def dumpData(writenData):                      # 将数据从内存写入到json文件中，会覆盖原有文件内容,传入的数据是需要写入的数据
    jsonData = writenData
    filename = '42_[扩展-数据库]化合物各类原子数统计.json'
    with open(filename,'w') as f:              # w 打开一个文件只用于写入。如果该文件已存在则覆盖。如果该文件不存在，创建新文件。。
        json.dump(jsonData,f)
    print('内存写入到json文件中的数据: ',jsonData)    # 文件的内容起始就是jsonData的内容，一摸一样

"""
1. 每次使用前需要添加化合物组成信息

atomDict = {
    'CaO': {'Ca':'1','O':'1','total':'2'},
    'SiO2': {'Si':'1','O':'2','total':'3'},
    'B2O3':{'B':'2','O':'3','total':'5'},
    'P2O5':{'P':'2','O':'5','total':'7'}
    
    }

2. 每次使用前需要更新渣系的组成信息，直接从38.py脚本输出结果里找
"""

# compoundDict = {'CaO': '11', 'SiO2': '10', 'B2O3': '1'}
# atomDict = {"CaO": {"Ca": "1", "O": "1", "total": "2"}, "SiO2": {"Si": "1", "O": "2", "total": "3"}, "B2O3": {"B": "2", "O": "3", "total": "5"}, "P2O5": {"P": "2", "O": "5", "total": "7"}}
# 02函数，结合具体的凝聚态体系，返回体系中每种化合物的原子构成和数量，以字典的形式，比如 [{'Ca': 11.0, 'O': 11.0, 'total': 22.0}, {'Si': 10.0, 'O': 20.0, 'total': 30.0}, {'B': 2.0, 'O': 3.0, 'total': 5.0}]
def atomCount(atomDict,compoundDict):         # atomDict 是个包含各种分子式原子组成的字典，是个数据库； compoundDict字典是要计算的化合物分子式组成字典
    comList = list(compoundDict.keys())       # ['CaO', 'SiO2', 'B2O3']
    comValList = list(compoundDict.values())  # ['11', '10', '1']
    print(comList)
    print(comValList)
    totalAtomNumList = []
    for i, j in zip(comList,comValList):
        valueTotal = float(atomDict[i]['total'])
        totalAtomNum = valueTotal*float(j)
        totalAtomNumList.append(totalAtomNum) 
    # print("总原子数",sum(totalAtomNumList),'\n')
    
    comTotalList = []
    for i, j in zip(comList,comValList):    # 同时遍历两个长度相等的列表
        # print(atomDict[i],j)
        # atomDict[i]
        """
        {'Ca': '1', 'O': '1', 'total': '2'} 11
        ['Ca', 'O', 'total'] ['1', '1', '2']
        """
        atomDictKeysList =  list(atomDict[i].keys())
        atomDictvaluesList =  list(atomDict[i].values())
        # print(atomDictKeysList,atomDictvaluesList)
        temList = []
        for m,n in zip(atomDictKeysList,atomDictvaluesList):
            Mulatom = float(n)*float(j)
            # print(Mulatom)
            temList.append(Mulatom)
        # print(temList)
        dictTemp = {}
        for x,y in zip(atomDictKeysList,temList):
            dictTemp[x]=y
        # print(dictTemp)
        comTotalList.append(dictTemp)
        # print("--------------")
    print('返回一个列表，列表元素为字典，每个字典是每种化合物的各原子构成：',comTotalList)   
    return comTotalList     # 返回的是列表，列表的元素是字典，包含了各种化合物的原子数量
    # comTotalList = [{'Ca': 11.0, 'O': 11.0, 'total': 22.0}, {'Si': 10.0, 'O': 20.0, 'total': 30.0}, {'B': 2.0, 'O': 3.0, 'total': 5.0}]

# 03函数，将列表中的多个字典进行合并
def dict_Sum(ini_dict):   # 将多个字典合并，键相同的值相加；ini_dict是一个列表，列表的元素是字典
# 比如： ini_dict = [{'Ca': 11.0, 'O': 11.0, 'total': 22.0}, {'Si': 10.0, 'O': 20.0, 'total': 30.0}, {'B': 2.0, 'O': 3.0, 'total': 5.0}]
    result = {}
    for d in ini_dict:
        for k in d.keys():
            result[k] = result.get(k, 0) + d[k]     
    print("------混合体系的原子组成字典: ", str(result))

# 01函数，获取分子式的原子组成，返回一个分子的组成字典
def chemicalsSplit():   # chemString = 'Si-1-O-2,Ca-1-O-1,B-2-O-3'
    print('请输入需要转换成字典的组分化学式，按照如下格式: Si-1-O-2,Ca-1-O-1,B-2-O-3 ,分子式用逗号隔开，元素用-隔开')
    compString = input()
    compList = compString.split(',')
    chemDict = {}
    for mol in compList:  # mol =  'Si-2-O-1'
        molList = mol.split('-') # 
        molFormula = ''
        oddList = [] # 计算原子数的列表
        for i,j in enumerate(molList):
            if (i%2) !=0:       # 第一个说明为奇数索引
                oddList.append(int(j))
                if int(j) == 1: # 判断是否为1
                    temp = ''
                else:
                    temp = j
            else:               # 全为偶数
                temp = j
            molFormula = molFormula + temp
        # print('化合物的化学式：',molFormula)
        chemDict[molFormula] = {}
        
        for k in range(0,int(len(molList)/2)):
            keyEle = molList[k*2]
            valueEle = molList[k*2+1]
            chemDict[molFormula][keyEle] = valueEle
        chemDict[molFormula]['total'] = sum(oddList)
    print('------化合物分子式的原子组成字典------：',chemDict)   # chemDict = {'SiO2': {'Si': '1', 'O': '2', 'total': 3}, 'CaO': {'Ca': '1', 'O': '1', 'total': 2}, 'B2O3': {'B': '2', 'O': '3', 'total': 5}}
    return chemDict                                    # 返回的字典是一个分子式的原子组成字典

# chemString = 'Si-1-O-2,Ca-1-O-1,B-2-O-3'


"""
调用上述函数
"""  
if __name__ == '__main__':
    print("请输入待处理字典，或字符串，如 {'CaO': '11', 'SiO2': '10', 'B2O3': '1'} 或 str,CaO,11,SiO2,10,B2O3,1  ,其中开头的 str 必不可少 ")
    inputContent = input()
    inputList = inputContent.split(',')
    inputDict = {}
    if inputList[0] == 'str':              # 判断输入的字符串类型是否为字符串，根据第一个字符串的内容 str 判断
        if (len(inputList)-1)%2 != 0:
            print('字符串输入有误，请重新输入！')
            sys.exit("404")
        for i in range(0, int((len(inputList)-1)/2 )):
             inputDict[inputList[2*i+1]] = inputList[2*i+2]
        print('----输入的字符串转化为字典----：',inputDict)
    else:                                 # 输入内容不是str,CaO,11,SiO2,10,B2O3,1 的情况
        inputDict = eval(inputContent)    # 将字符串转化为字典，inputDict = {'CaO': '11', 'SiO2': '10', 'B2O3': '1'}
    atomDict = loadData()                 # 调用04函数，加在json文件中的数据库，04函数返回一个字典
    # atomDict = chemicalsSplit()         # 调用01函数，该函数返回一个分子式的原子组成字典，如：{'SiO2': {'Si': '1', 'O': '2', 'total': 3}, 'CaO': {'Ca': '1', 'O': '1', 'total': 2}, 'B2O3': {'B': '2', 'O': '3', 'total': 5}}
    MissMoleList = []                     # 该字典用于储存需要添加分子式的化合物
    for j in list(inputDict.keys()):      # 判断输入的分子式的组成是否都在数据库中
        if j in list(atomDict.keys()):
            print(j,' 分子式的原子组成在数据库中',atomDict[j])
        else:
            print('------数据库中缺少相关分子式的原子组成，请为数据库添加该分子式的原子组成------',j)
            MissMoleList.append(j)
            # sys.exit("404")
    if len(MissMoleList) == 0:
        print('~~~~~~~~~凝聚态体系中所有化合物均在数据库中,数据库中化合物的种类如下：',list(atomDict.keys()))
    else:                                     # 如果有需要添加的新的分子式，则会要求输入原子组成，更新文件
        print('-----凝聚态体系中部分化合物不在数据库中，请为以下化合物添加原子组成-----：',MissMoleList)
        plusDict = chemicalsSplit()           # 调用01函数，为部分化合物添加原子组成，返回一个字典
        atomDict = { **atomDict, **plusDict } # 将字典进行更新
        dumpData(atomDict)                    # 调用05函数，将更新后的字典写入到json文件中
        print('----------数据库更新后包含的化合物种类----------：',list(atomDict.keys()))  # 打印出更新后字典中的化合物
    dict_Sum(atomCount(atomDict,inputDict)) # atomDict是一个分子式的原子组成数据库；atomCount是02函数，返回一个列表，列表元素是字典；dict_Sum是03函数，将列表中多个字典进行合并
    

    



