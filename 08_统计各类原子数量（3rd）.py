# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 09:55:44 2021

@author: sun78
"""
# 任务需求：写一个脚本来统计一帧xyz文件中的各类原子数，通过输入原子种类来实现
# 注意该脚本是使用list.count(obj)来统计元素的种类和数量


import datetime                      # 导入时间模块
x = datetime.datetime.now()          # 显示时间
print("此刻时间：",x)


print("请输出需要处理的文件名,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

#下面是把文本中的每一行转换成列表中的字符串
mylines = []                                # Declare an empty list.
with open ( na , 'rt') as myfile:    # Open lorem.txt for reading text.
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.rstrip('\n')) # strip newline and add to list.
        
for element in mylines: # 对于列表中的每个元素，
    print(element) # 打印它。


print("请输入文本中所有的元素符号,如Si,Ca,O,B等: ")     # 提示命令行输入
bb = input()              # 注意字符串输入变量的数据类型转换
print("已输入元素大写首字母", bb)           # 显示输入的内容
ele = bb.split(",")
number = len(ele)
print ("元素种类数为：",number)
print ("元素种类为：",ele)

# 建一个新的列表用来存储第二行之后每行的首个元素

values = []  
pp=0


for line in mylines:          # 外循环遍历整个文本
    pp += 1
    if pp > 2:           # 从第三行开始
        p2 = line.split( ) # 将每一行用空格分离
        print ("这是行数：",pp ,"p2分开后是：", p2)
        values.append(str(p2[0]))   #追加元素
        
#list.count(obj)  #统计某个元素在列表中出现的次数


#value_cnt = {}
for el in ele:
    tn = values.count(el) #统计列表中每种元素的数量
    print("元素和数量分别为：", el,":",tn)
    # value_cnt[value] = value_cnt.get(value,0) + 1
    # 用字典来统计列表各元素数量非常巧妙


#遍历字典中的所有键
#for key, value in value_cnt.items():


# 以下是计时程序
y = datetime.datetime.now()
z = y-x
print("共耗时",z ,"时:分:秒:毫秒")           # 显示输入的内容


print("-------------")