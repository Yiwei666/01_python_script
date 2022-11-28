# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:24:19 2022

@author: sun78
"""

# 输入三个原子坐标，确定晶面指数

import os
import sys
import math
import datetime                      # 导入时间模块
xx = datetime.datetime.now()          # 显示时间
print("此刻时间：",xx)

# 列出当前路径的所有文件名

# for root, dirs, files in os.walk("."):
#    for filename in files:
#        print(filename)  
        
        
print("请输入p1(x1 y1 z1)坐标，用逗号间隔 , 如 1,2,3")     # 提示命令行输入
p1 = input()              # 注意字符串输入变量的数据类型转换
# print("已输入p1(x1 y1 z1)坐标： ", p1)           # 显示输入的内容

print("请输入p2(x2 y2 z2)坐标，用逗号间隔 , 如 1,2,3")     # 提示命令行输入
p2 = input()              # 注意字符串输入变量的数据类型转换
# print("已输入p2(x2 y2 z2)坐标： ", p2)           # 显示输入的内容

print("请输入p3(x3 y3 z3)坐标，用逗号间隔 , 如 1,2,3")     # 提示命令行输入
p3 = input()              # 注意字符串输入变量的数据类型转换
# print("已输入p3(x3 y3 z3)坐标： ", p3)           # 显示输入的内容

print("请输入晶格常数a, 如1.1")     # 提示命令行输入
a = input()              # 注意字符串输入变量的数据类型转换
# print("请输入晶格常数： ", a)           # 显示输入的内容

numbers1 = p1.split(",")           # 把字符串分开

x1 = float(numbers1[0])
y1 = float(numbers1[1])
z1 = float(numbers1[2])

numbers2 = p2.split(",")           # 把字符串分开
x2 = float(numbers2[0])
y2 = float(numbers2[1])
z2 = float(numbers2[2])

numbers3 = p3.split(",")           # 把字符串分开
x3 = float(numbers3[0])
y3 = float(numbers3[1])
z3 = float(numbers3[2])

A = (y2 - y1)*(z3 - z1) - (z2 - z1)*(y3 - y1)
B = (x3 - x1)*(z2 - z1) - (x2 - x1)*(z3 - z1)
C = (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)
D = -(A * x1 + B * y1 + C * z1)

print("方程形式为 Ax+By+Cz+D=0", "A=",A,"B=",B,"C=",C,"D=",D)           # 显示输入的内容
print("方程形式为 Ax+By+Cz+D=0", "A=",round(A,8))           # round保留小数
print("方程形式为 Ax+By+Cz+D=0", "B=",round(B,8))           # round保留小数
print("方程形式为 Ax+By+Cz+D=0", "C=",round(C,8))           # round保留小数
print("方程形式为 Ax+By+Cz+D=0", "D=",round(D,8))           # round保留小数


xd = -D/A  # x轴截距
yd = -D/B  # y轴截距 
zd = -D/C  # z轴截距

h = round(1/xd,6 )   # 晶面指数h
k = round(1/yd,6 )   # 晶面指数k
l = round(1/zd,6 )   # 晶面指数l


print("晶面指数（h k l）： ", "h=",h,"k=",k,"l=",l )           # 显示输入的内容
print("晶面指数（h k l）： ", "h=",round(1/xd,6 ))
print("晶面指数（h k l）： ", "k=",round(1/yd,6 ))
print("晶面指数（h k l）： ", "l=",round(1/zd,6 ))

print("float(a)", float(a))

d = float(a)*1/math.sqrt(h*h+k*k+l*l) #立方晶系晶面间拒计算公式


r = abs(D)/math.sqrt(A*A+B*B+C*C)  # 原点到平面的距离, abs函数取绝对值

print("立方晶系晶面间距 d =", d)
print("原点到平面的距离 r =", r)

print("r/d =", round(r/d,6),"d")


print("任务完成!")
print("---------------")

# 以下是计时程序
yy = datetime.datetime.now()
zz = yy-xx
print("共耗时",zz ,"时:分:秒:毫秒")           # 显示输入的内容

        
        





