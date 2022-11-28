# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:30:11 2021

@author: sun78
"""
# 在平移原子坐标脚本的基础上进行修改

import os
import datetime                      # 导入时间模块
#import math
x = datetime.datetime.now()          # 显示时间
print("此刻时间：",x)

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)

print("-------------")


print("请输出需要处理的文件名1,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换


#下面是把文本中的每一行转换成列表中的字符串
mylines = []                                # Declare an empty list.
with open ( na , 'rt') as myfile:    # Open lorem.txt for reading text.
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.rstrip('\n')) # strip newline and add to list.
        
for element in mylines: # 对于列表中的每个元素，
    print(element) # 打印它。


print("请输出需要处理的文件名2,xyz格式")     # 提示命令行输入
ma = input()              # 注意字符串输入变量的数据类型转换


#下面是把文本中的每一行转换成列表中的字符串
youlines = []                                # Declare an empty list.
with open ( ma , 'rt') as youfile:    # Open lorem.txt for reading text.
    for youline in youfile:                   # For each line in the file,
        youlines.append(youline.rstrip('\n')) # strip newline and add to list.
        
for element2 in youlines: # 对于列表中的每个元素，
    print(element2) # 打印它。
    
    

print("请为输出文件3命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容

#m = open( name, "x")   # 创建新文本
#m.close()



pp=0
nn = 0
qq = 0
mm = 0

with open(name, 'w') as new_file:
    # 下面是写入文件1的3-N行
    with open(na, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pp += 1
            if pp > 2:
                nn += 1
                new_file.write(line)
                print("写入第：",nn," 个元素") 
                print("-------------")
    # 下面是写入文件2的3-N行 
    with open(ma, 'r') as f2:
        lines2 = f2.readlines()
        for line2 in lines2:
            qq += 1
            if qq > 2:
                mm += 1
                new_file.write(line2)
                print("写入第：",nn+mm," 个元素") 
                print("-------------")
         


#for line in mylines:          # string to be searched
#    pp += 1
#    if pp > 2:
#        p3 = line.split( )  #把字符串line转换成了列表
#        print ("这是行数：",pp ,"原坐标分开后是：", p3)
#               
        #distance = math.sqrt( ((float(p1[0])-float(p2[1]))**2)+((float(p1[1])-float(p2[2]))**2)+((float(p1[2])-float(p2[3]))**2) )
#        print ("这是行数：",pp ,"变换后坐标分开后是：", p3) 
#        h = open(name , "a")
#        h.write(str(p3[0]))
#        h.write('\000')
#        h.write('\n')       #换行
#        print(p3)
#        nn += 1      #此处的nn用来统计原子数
#        h.close()

            
#下面是给首行添加原子数的语句
#We read the existing text from file in READ mode 

src = open(name,"r")
fline = str(nn+mm)   #此处是原子数
#fline = "newly added FIRST LINE\n"    #Prepending string 
oline = src.readlines() 
#Here, we prepend the string we want to on first line 
oline.insert(0,fline)
oline.insert(1,'\n') #首行换行
oline.insert(2,'\n') #第二行换行空格
src.close()
#We again open the file in WRITE mode  
src=open(name,"w") 
src.writelines(oline) 
src.close() 


#统计输出文件的行数
fobj = open( name ,'r')
row_len = len(fobj.readlines())
print("共有",row_len ,"行","原子数为 :",nn+mm)
      

# 以下是计时程序
y = datetime.datetime.now()
z = y-x
print("共耗时",z ,"时:分:秒:毫秒")           # 显示输入的内容


print("-------------")