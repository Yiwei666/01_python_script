# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:03:00 2021

@author: sun78
"""
# 统计各类原子数量，首先输入元素种类，通过对比第2行以后每行首字母来判断
# 注意外循环是文本文件，内循环是元素种类
# 注意该脚本仅适用于12种元素以下的元素种类个数统计



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
    

# Locate and print all occurences of letter "e"

#substr = "B"                  # substring to search for.
#for line in mylines:          # string to be searched
#  index = 0                   # current index: character being compared
#  prev = 0                    # previous index: last character compared

#  while index < len(line):    # While index has not exceeded string length,
#    index = line.find(substr, index)  # set index to first occurrence of "e"
#    if index == -1:           # If nothing was found,
#      break                   # exit the while loop.
#    print(" " * (index - prev) + "e", end='')  # print spaces from previous
                                               # match, then the substring.
#    prev = index + len(substr)       # remember this position for next loop.
#    index += len(substr)      # increment the index by the length of substr.
                              # (Repeat until index > line length)
#  print('\n' + line);         # Print the original string under the e's


print("请输入文本中所有的元素符号,如Si,Ca,O,B等: ")     # 提示命令行输入
bb = input()              # 注意字符串输入变量的数据类型转换
print("已输入元素大写首字母", bb)           # 显示输入的内容
ele = bb.split(",")
number = len(ele)
print ("元素种类数为：",number)
print ("元素种类为：",ele)

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n10 = 0
n11 = 0
n12 = 0


pp=0

for line in mylines:          # 外循环遍历整个文本
    pp += 1
    if pp > 2:           # 从第三行开始
        p2 = line.split( ) # 将每一行用空格分离
        print ("这是行数：",pp ,"p2分开后是：", p2)
        nn = 0
        for el in ele:
            nn += 1
            if nn <= number:
#                if str(p2[0]) == str(el):
                if str(p2[0]) == str(el):
                    if nn == 1: #第1个元素
                        n1 += 1
                    if nn == 2: #第2个元素
                        n2 += 1
                    if nn == 3: #第3个元素
                        n3 += 1                        
                    if nn == 4: #第4个元素
                        n4 += 1                    
                    if nn == 5: #第5个元素
                        n5 += 1                    
                    if nn == 6: #第6个元素
                        n6 += 1
                    if nn == 7: #第7个元素
                        n7 += 1                        
                    if nn == 8: #第8个元素
                        n8 += 1                        
                    if nn == 9: #第9个元素
                        n9 += 1                        
                    if nn == 10: #第10个元素
                        n10 += 1                        
                    if nn == 11: #第11个元素
                        n11 += 1                       
                    if nn == 12: #第12个元素
                        n12 += 1  

print ("统计元素种类不能超过12个") 
print ("元素种类为：",ele)       
print("元素种类分别为：",bb)    
print("对应元素个数分别为：",n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12) 



# 以下是计时程序
y = datetime.datetime.now()
z = y-x
print("共耗时",z ,"时:分:秒:毫秒")           # 显示输入的内容


print("-------------")
