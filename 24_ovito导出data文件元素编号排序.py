# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:42:49 2021

@author: sun78
"""
#234 3 0.0 4.2732740499 2.666998634   9.3232410641
# 52 2 0.0 3.2713486002 17.3391469318 11.0885046527
#第一列是序号，第二列是元素编号，第三列是价态，后三列是xyz分坐标
#先用ovito基于cell文件导出data文件并观察元素标号，将元素按照自己想要的顺序进行排列
import os
from collections import Counter
import datetime                      # 导入时间模块
xx = datetime.datetime.now()          # 显示时间
print("此刻时间：",xx)


for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)

print("-------------")

print("请输出需要处理的文件名,data文件格式，注意要删除表头")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

#注意如何输入字典

list1 = []

with open(na, 'r') as i:  # 打开文件
    lines = i.readlines()  # 读取所有行
    for line in lines:
        title1 = line.split( )[1] #Step Nr.  # 读取第二列
        list1.append(title1)
    result=Counter(list1)
    print("各元素标号的数量",result)
    
print("---------------")



print("先用ovito基于cell文件导出data文件并观察元素标号，将元素按照自己想要的顺序进行排列")
print("请按想要的顺序输入原文件原子编号，用英文逗号间隔，如3，1，2 :")     # 提示命令行输入
atom = input()              # 注意字符串输入变量的数据类型转换
print("已输入原子编号： ", atom)           # 显示输入的内容

numbers = atom.split(",")           # 把字符串分开，numbers变成了列表
aaa = len(numbers)                  # 列表的元素个数
print("原子个数为： ", aaa )           # 显示输入的内容


print("请为输出文件命名,data格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容

m = open( name, "x")   # 创建新文本
m.close()

            
with open(name, 'w') as new_file:
    with open(na, 'r') as f:
        lines = f.readlines()
        i = 1
        t = 0
        while i <= aaa:
            print("开始筛选元素编号为：",numbers[i-1],"的元素","并将其重构为：",i)
            r = 0
            for line in lines:
                p2 = line.split( )[1]
                if p2 == numbers[i-1]:
                    r += 1
                    t += 1
                    new_file.write(str(t) + '  ' + str(i) +'  '+ str(0) +'  '+ str(line.split( )[3])+'  '+ str(line.split( )[4])+'  '+ str(line.split( )[5])+ '\n')
                    print("写入：",str(t) + '  ' + str(i) +'  '+ str(0) +'  '+ str(line.split( )[3])+'  '+ str(line.split( )[4])+'  '+ str(line.split( )[5]))
            print("元素编号为：",numbers[i-1],"的元素共有：",r,"个，并将其元素编号重构为：",i)
            print("---------")
            i += 1    
        print("共有原子个数：",t)

print("各元素标号的数量",result)
print("文件转换已完成！")
            
# 以下是计时程序
yy = datetime.datetime.now()
zz = yy-xx
print("共耗时",zz ,"时:分:秒:毫秒")           # 显示输入的内容









