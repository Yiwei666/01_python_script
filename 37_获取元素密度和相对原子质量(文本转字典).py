# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:35:53 2022

@author: sun78
"""

from numpy import *
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import json

# 该脚本用于将txt文本的每一行转换成列表然后存于字典中，尤其是相对原子质量，密度等,推荐使用的文本格式如下
"""
元素密度
    Density	Unit	Name		Symbol	AtomicNumber ChineseName State
    0.0899 	g/L		Hydrogen	H	1   气
    0.1785 	g/L		Helium		He	2   气
    0.534 	g/cc	Lithium		Li	3
    1.848 	g/cc	Beryllium	Be	4
    2.34 	g/cc	Boron		B	5
"""
"""
相对原子质量
AtomicNumber	Name	Symbol	RelativeAtomicMass	    Group	 Period
1	Hydrogen		H	1.00794		1	1
2	Helium		    He	4.002602	18	1
3	Lithium		    Li	6.941		1	2
4	Beryllium		Be	9.012182	2	2
"""
"""
AtomicNumber	Name	Symbol	RelativeAtomicMass	    
1	null		SiO2	60.0843		
2	null		CaO	    56.077400000000004	
3	null		MgO	    40.3044	
"""

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
    print("请输出需要处理的文件名,txt格式")     # 提示命令行输入
    txtName = input()              # 注意字符串输入变量的数据类型转换

# 单个矩阵是atomNumber*5
lineSymbolDict = {}
numberSymbolDict = {}
pp = 0
tt = 0
# 注意前两行不是有效数据
with open(txtName, 'r',encoding = 'utf -8') as f:
    lines = f.readlines()
    txtLength = len(lines)
    print("文本行数",txtLength )
    print("文本首行内容",lines[0])
    for line in lines:
        pp += 1
        if pp > 1 :
            listColumn = line.split( )
            columnNmuber=len(listColumn)
            print("文本列数",txtLength )
            # 0.534 	g/cc	Lithium		Li	3
            """
            针对不同的字典格式需求，下面两行需要进行相应调整
            """
            lineSymbolDict[listColumn[3]]= listColumn
            # numberSymbolDict[listColumn[4]]= listColumn[3]
print(lineSymbolDict)
# print(numberSymbolDict)
            
                    