# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:59:36 2022

@author: sun78
"""
# 将.cell文件转换为同名的.xyz文件，统计各原子的数量，保留晶胞长度信息


# SiHfB.cell

import os
import tkinter as tk
from tkinter import filedialog
from collections import Counter

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
    print("请输出需要处理的.cell文件名（默认正或长方体盒子）,如SiHfB.cell格式,注意输出xyz文件名与输入cell文件名相同")     # 提示命令行输入
    txtName = input()              # 注意字符串输入变量的数据类型转换
xyzFileName = txtName.split(".")[0]+".xyz"
pp = 0
tt = 0
with open(txtName, 'r') as f:
    lines = f.readlines()
    txtLength = len(lines) # The last two line of cell file is blank, txtLength is one bigger that actual value
    print("文本行数",txtLength )
    # The first number of the second line is the length of cell.
    cellLength = lines[1].split( )[0]
    cellWidth = lines[2].split( )[1]
    cellHeight = lines[3].split( )[2]
    # A(Xa, Ya, Za)
    # B(Xb, Yb, Zb)
    # C(Xc, Yc, Zc)
    Xa = float(lines[1].split( )[0])
    Ya = float(lines[1].split( )[1])
    Za = float(lines[1].split( )[2])
    Xb = float(lines[2].split( )[0])
    Yb = float(lines[2].split( )[1])
    Zb = float(lines[2].split( )[2])
    Xc = float(lines[3].split( )[0])
    Yc = float(lines[3].split( )[1])
    Zc = float(lines[3].split( )[2])
    print("cell长宽高分别为：",cellLength,cellWidth,cellHeight)
    # The index of the coordinate starting line is 7    
    # Determine the ending line of the coordinate in order to compute the all kinds atoms numbers.
    iIndex = 6 # i is index from 6, and index 6 is "%BLOCK POSITIONS_FRAC"
    while iIndex < txtLength-2 : 
        # Ending line is "%ENDBLOCK POSITIONS_FRAC"
        if lines[iIndex].split( )[0]== "%ENDBLOCK" and lines[iIndex].split( )[1] == "POSITIONS_FRAC":           
            print("原子坐标起始、结束行的index分别为：",7,iIndex-1,"\n","原子坐标开始和结束标志分别为：\n",lines[6],lines[iIndex])
            endingLineIndex = iIndex-1 #  最后一行原子坐标的index
            atomNumber = iIndex-6-1    # 原子数
            print("体系原子数：",atomNumber)
            break
        iIndex += 1
    with open(xyzFileName, 'w') as new_file:  # 追加用a
        new_file.write(str(atomNumber)+"\n")
        # Tv_1: 7.426 0.0 0.0 Tv_2: 3.6 6 6.40 0.0 Tv_3: 0.0 0.0 10.0
        new_file.write("Tv_1: "+ str(cellLength)+ " 0.0 0.0 Tv_2: 0.0 "+ str(cellWidth) + " 0.0 Tv_3: 0.0 0.0 "+ str(cellHeight)+"\n")
    with open(xyzFileName, 'a') as new_file:  # 追加用a       
        atomList = []
        atomIndex = 7 # The index of starting line of atom coordinate is 7 and the ending index is endingLineIdex.
        while atomIndex <= endingLineIndex:  # "endingLineIndex-1" is the index of last line of atom coordinate.
            lineFirstElement = lines[atomIndex].split( )[0]
            atomList.append(lineFirstElement)
            # Xcar=Xa*x+Xb*y+Xc*z
            # Ycar=Ya*x+Yb*y+Yc*z
            # Zcar=Za*x+Zb*y+Zc*z            
            xCoordinate = float(lines[atomIndex].split( )[1])
            yCoordinate = float(lines[atomIndex].split( )[2])
            zCoordinate = float(lines[atomIndex].split( )[3])
            Xcar = Xa*xCoordinate+Xb*yCoordinate+Xc*zCoordinate
            Ycar = Ya*xCoordinate+Yb*yCoordinate+Yc*zCoordinate
            Zcar = Za*xCoordinate+Zb*yCoordinate+Zc*zCoordinate
            carContent = lineFirstElement+" "+str(Xcar)+" "+str(Ycar)+" "+str(Zcar)+"\n"
            new_file.write(carContent)
            atomIndex += 1 
    print (len(atomList),"体系中各原子数量",Counter(atomList))

