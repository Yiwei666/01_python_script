# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:05:42 2022

@author: sun78
"""
"""
每次使用前注意查看1和2的提示
"""

# '': {'':'','':'','total':''}

#################################################################
"""
1. 每次使用前需要添加化合物组成信息
"""

atomDict = {
    'CaO': {'Ca':'1','O':'1','total':'2'},
    'SiO2': {'Si':'1','O':'2','total':'3'},
    'B2O3':{'B':'2','O':'3','total':'5'},
    'P2O5':{'P':'2','O':'5','total':'7'}
    
    }
#################################################################

#################################################################
"""
2. 每次使用前需要更新渣系的组成信息，直接从38.py脚本输出结果里找
"""
compoundDict = {'CaO': '11', 'SiO2': '10', 'B2O3': '1'}
#################################################################


comList = list(compoundDict.keys())  # ['CaO', 'SiO2', 'B2O3']
comValList = list(compoundDict.values())  # ['11', '10', '1']
print(comList)
print(comValList)
totalAtomNumList = []
for i, j in zip(comList,comValList):
    valueTotal = float(atomDict[i]['total'])
    totalAtomNum = valueTotal*float(j)
    totalAtomNumList.append(totalAtomNum) 
print("总原子数",sum(totalAtomNumList))

comTotalList = []
for i, j in zip(comList,comValList):
    print(atomDict[i],j)
    # atomDict[i]
    """
    {'Ca': '1', 'O': '1', 'total': '2'} 11
    ['Ca', 'O', 'total'] ['1', '1', '2']
    """
    atomDictKeysList =  list(atomDict[i].keys())
    atomDictvaluesList =  list(atomDict[i].values())
    print(atomDictKeysList,atomDictvaluesList)
    temList = []
    for m,n in zip(atomDictKeysList,atomDictvaluesList):
        Mulatom = float(n)*float(j)
        print(Mulatom)
        temList.append(Mulatom)
    print(temList)
    dictTemp = {}
    for x,y in zip(atomDictKeysList,temList):
        dictTemp[x]=y
    print(dictTemp)
    comTotalList.append(dictTemp)
    print("--------------")
print(comTotalList)   
# comTotalList = [{'Ca': 11.0, 'O': 11.0, 'total': 22.0}, {'Si': 10.0, 'O': 20.0, 'total': 30.0}, {'B': 2.0, 'O': 3.0, 'total': 5.0}]


def dict_Sum(ini_dict):   
    result = {}
    for d in ini_dict:
        for k in d.keys():
            result[k] = result.get(k, 0) + d[k]     
    print("Constitute_dictionary : ", str(result))


"""
调用上述函数
"""  
dict_Sum(comTotalList) 
    

    



