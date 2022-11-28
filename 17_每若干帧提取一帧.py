# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:54:11 2021

@author: sun78
"""
#任务需求：从第x帧开始，每n帧提取一帧


import os                     
import sys
import datetime # 导入时间模块
xx = datetime.datetime.now()          # 显示时间
print("此刻时间：",xx)

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)


print("-------------")

print("请输出需要处理的文件名,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

with open(na, 'r') as i:  # 打开文件
    lines = i.readlines()  # 读取所有行
    first_line = lines[0]  # 取第一行
    print ("打印首行，即原子数目：",first_line)

print("---------------")


fobj = open( na ,'r')
row_len = len(fobj.readlines()) # 统计文件行数
print("文件行数为",row_len)     # 提示命令行输入
print("请输入模型原子数,x:")     # 提示命令行输入
x = int(input())              # 注意字符串输入变量的数据类型转换
print("已输入原子数： ", x)           # 显示输入的内容
y = row_len/int(x+2)             # 计算帧数
print("一共",y,"帧")

print("请输入要截取的起始帧数y1：")
y1 = int(input()) 


print("每y2帧提取一帧，请输入y2：")
y2 = int(input()) 



print("提示！最多可获取的帧数为：",(y-y1+1)/y2)

print("请输入想要获取的总帧数y3：")
y3 = int(input()) 

if y3 > (y-y1+1)/y2 :
    print("想要获取的总帧数超过了能提供的总帧数：程序返回404退出")
    sys.exit(404)

print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容

pp = 0     #行数          
mm = 1

with open(name, 'w') as new_file:
    with open(na, 'r') as v:
        lines = v.readlines()
        for line in lines:
            pp += 1           #行数
            #zhen = math.ceil(pp/(int(x+2)))      #判断处于哪一帧，floor是向下取整
            if mm <= y3:
                if pp >= (int(x+2)*(y1-1)+1+y2*int(x+2)*(mm-1)) and pp <= (int(x+2)*y1+y2*int(x+2)*(mm-1)):    #通过行数判断是否到了新一帧
                    new_file.write(line)
                    if pp == (int(x+2)*(y1-1)+1+y2*int(x+2)*(mm-1)):
                        print ("开始写入帧数：",mm)
                    if pp == (int(x+2)*y1+y2*int(x+2)*(mm-1)):
                        mm += 1
            else:
                break

# 以下是计时程序
yy = datetime.datetime.now()
zz = yy-xx
print("共耗时",zz ,"时:分:秒:毫秒")           # 显示输入的内容







