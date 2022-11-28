# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 15:31:11 2021

@author: sun78
"""

#任务需求：在给定编号原子周围半径r范围内的原子变化
#对于真实连续原子轨迹坐标应该同样适用
import os
import sys
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
print("请输出需要处理的文件名,多帧xyz文件格式")     # 提示命令行输入
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


print("请输入想要提取的原子编号，用英文逗号间隔 :")     # 提示命令行输入
atom = input()              # 注意字符串输入变量的数据类型转换
print("已输入原子编号： ", atom)           # 显示输入的内容

numbers = atom.split(",")           # 把字符串分开
aaa = len(numbers)                  # 列表的元素个数
print("原子个数为： ", aaa )           # 显示输入的内容

print("请输入截断半径rc：")     # 提示命令行输入
rc = float(input())              # 注意字符串输入变量的数据类型转换

print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容


dict_r = {}    #新建一个字典

en = [] #帧数,m1
el = [] #通过文本行数来标记原子,n1
em = [] #统计总共有多少个原子,uu
x1 = [] #x分坐标,px
y1 = [] #y分坐标,py
z1 = [] #z分坐标,pz


pp = 0     #行数
uu = 0
                   
with open(na, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pp += 1           #行数
            zhen = math.ceil(pp/(int(x+2)))      #通过行数判断处于哪一帧，floor是向下取整,ceil为向上取整
            print("帧数为:",zhen,"文本行数为：",pp)
            
            for number in numbers:
                value = (zhen-1)*(x+2)+int(number)+2
                print ("原子编号：", number)
                print ("行数为：", value)
                if pp == value:
                    uu += 1
                    em.append(uu)
                    
                if pp == value:
                    m1 = zhen   #帧数
                    px = float(line.split( )[1])
                    py = float(line.split( )[2])
                    pz = float(line.split( )[3])
                    
                    en.append(m1)
                    el.append(pp)   #行数
                    x1.append(px)
                    y1.append(py)
                    z1.append(pz)
                    break   # break 打破了最小封闭for或while循环

print("帧数列表：",en)                    
print("行数列表：",el)  
print("原子数列表：",em)  
print("x分坐标列表：",x1)  

print("-------------")  



#接下来这一部分是为了筛选出符合条件的原子坐标

pp = 0

qq = 0

dict_r = {}    #新建一个字典


with open(na, 'r') as f1:
        lines = f1.readlines()
        for line in lines:
            pp += 1           #行数
            zhen = math.ceil(pp/(int(x+2)))      #通过行数判断处于哪一帧，floor是向下取整,ceil为向上取整
            print("帧数为:",zhen,"文本行数为：",qq)
            if (pp != (int(x+2)*(zhen-1)+1)) and (pp != (int(x+2)*(zhen-1)+2))  :
                
                px = float(line.split( )[1])
                py = float(line.split( )[2])
                pz = float(line.split( )[3])
                
                ts = aaa*(zhen-1)+1   #定位列表相应元素位置
                te = aaa*zhen
                i = ts
                print("列表原子数的检索范围：",ts,"——",te,"此时i:",i)
                
                while i >= ts and i <= te:
                    distance = math.sqrt( ((px-x1[i-1])**2)+((py-y1[i-1])**2)+((pz-z1[i-1])**2) )
                    print("分坐标x1[i-1],y1[i-1],z1[i-1]分别为： ", x1[i-1],y1[i-1],z1[i-1])
                    print("实际距离是 ",distance) 
                    if rc >= distance:
                        print("文本行数pp满足条件，行数为： ", pp) 
                        qq += 1
                        break # break 打破了最小封闭for或while循环。
                    i += 1                        

                    
            if pp == (int(x+2)*(zhen-1)+x+2) :    #通过行数判断是否到了每一帧的最后一行
                print("正在写入键:",zhen,"值为：",qq)
                number = zhen              #记下帧数
                element = qq
                dict_r[number] = element
                print("---------------")
                qq = 0 
                
print("每一帧符合条件的原子数 ", dict_r)           # 显示输入的内容



#sys.exit(404)

                
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
                px = float(line.split( )[1])
                py = float(line.split( )[2])
                pz = float(line.split( )[3])
                ts = aaa*(zhen-1)+1   #定位列表相应元素位置
                te = aaa*zhen
                i = ts
                print("---------------")
                while i >= ts and i <= te:
                    distance = math.sqrt( ((px-x1[i-1])**2)+((py-y1[i-1])**2)+((pz-z1[i-1])**2) )
                    print("实际距离是 ",distance) 
                    if rc >= distance:
                        print("文本行数pp满足条件，行数为： ", pp) 
                        qq += 1
                        print("开始写入筛选行",line)
                        new_file.write(line)                        
                        break # break 打破了最小封闭for或while循环。
                    i += 1  #没找到需要继续循环

print("每一帧符合条件的原子数 ", dict_r)           # 显示输入的内容
print("任务完成!")
print("---------------")

# 以下是计时程序
yy = datetime.datetime.now()
zz = yy-xx
print("共耗时",zz ,"时:分:秒:毫秒")           # 显示输入的内容






  
            
            
            
            
            
            
            
            
            
            
            
            
            
