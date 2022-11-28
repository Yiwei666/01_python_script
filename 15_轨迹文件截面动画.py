# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 09:54:39 2021

@author: sun78
"""
#任务需求：在给定x轴，y轴或z轴截面方向上原子的演化情况
#输入一帧或多帧xyz文件
import os
import math
import datetime                      # 导入时间模块
xx = datetime.datetime.now()          # 显示时间
print("此刻时间：",xx)

# 列出当前路径的所有文件名

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)  

# 通过上述文件名列表找到要处理的文件
print("---------------")
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


print("请输入x轴截断值x,如6，将保留x>6空间的原子：")     # 提示命令行输入
xc = float(input())              # 注意字符串输入变量的数据类型转换
print("请输入y轴截断值y,最好取负值,如-6,将保留y>-6空间的原子：")     # 提示命令行输入
yc = float(input())              # 注意字符串输入变量的数据类型转换
print("请输入z轴截断值z,如-8,将保留z>-8空间的原子：")     # 提示命令行输入
zc = float(input())              # 注意字符串输入变量的数据类型转换
print("已输入x,y,z轴截断值：", xc,yc,zc)           # 显示输入的内容



print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容

dict_r = {}    #新建一个字典

pp = 0     #行数
nn = 0     #原子数
                   
with open(na, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pp += 1           #行数
            zhen = math.ceil(pp/(int(x+2)))      #通过行数判断处于哪一帧，floor是向下取整,ceil为向上取整
            print("帧数为:",zhen,"行数为：",pp)
            if (pp != (int(x+2)*(zhen-1)+1)) and (pp != (int(x+2)*(zhen-1)+2))  :
                print("条件分别为",int(x+2)*(zhen-1)+1,int(x+2)*(zhen-1)+2)
                print("此时的行数为:",pp,"值为：",line)
                p3x = float(line.split( )[1])
                p3y = float(line.split( )[2])
                p3z = float(line.split( )[3])
                if p3x >= xc and p3y >= yc and p3z >= zc : #筛选出满足条件的原子
                    nn += 1       #原子数
                    print("该行原子满足条件，行数为:",pp)
                    print("该行原子满足条件，值为:",line)
                    
            if pp == (int(x+2)*(zhen-1)+x+2) :    #通过行数判断是否到了新一帧
                print("条件筛选为,pp == (int(x+2)*(zhen-1)+x+2)",pp,int(x+2)*(zhen-1)+x+2)
                print("正在写入键:",zhen,"值为：",nn)
                number = zhen              #记下帧数
                element = nn
                dict_r[number] = element
                print("---------------")
                nn = 0 

print("每一帧符合条件的原子数 ", dict_r)           # 显示输入的内容
             
                
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
                print("开始写入主表头",str(dict_r[mm]))
            if pp == (int(x+2)*(zhen-1)+2) :
                new_file.write('This is number:'+ str(mm)+'\n')
                print("开始写入次表头",'This is number:'+ str(mm))
            if pp != (int(x+2)*(zhen-1)+1) and pp != (int(x+2)*(zhen-1)+2)  :
                p3x = float(line.split( )[1])
                p3y = float(line.split( )[2])
                p3z = float(line.split( )[3])
                if p3x >= xc and p3y >= yc and p3z >= zc : #筛选出满足条件的原子
                    print("开始写入筛选行",line)
                    new_file.write(line)

print("每一帧符合条件的原子数 ", dict_r)           # 显示输入的内容
print("任务完成，你超棒哦!")
print("---------------")

# 以下是计时程序
yy = datetime.datetime.now()
zz = yy-xx
print("共耗时",zz ,"时:分:秒:毫秒")           # 显示输入的内容

