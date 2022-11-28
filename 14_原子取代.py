# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:49:15 2021

@author: sun78
"""
# https://blog.csdn.net/qq_41575507/article/details/95893007
# 该脚本主要用字典来处理
# 原子取代脚本，例如输入1,B,2,O,3,Si,4,Ca分别表示1号原子被取代为B,2号原子被取代为O，等等

import os

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)

print("-------------")

print("请输出需要处理的文件名,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

#注意如何输入字典

dict_r = {}
polling_active = True
while polling_active:
    number = input("请输入要取代的原子编号，如6：")
    element = input("请输入新的元素符号，如Si：")
 
    #原子编号和元素符号存入字典中
    dict_r[number] = element
 
    #判断是否继续输入
    print("是否继续输入?(y/n):")     # 提示命令行输入
    repeat = input()
    if repeat == 'n':
        polling_active = False
 
print("输入的元素编号为：",dict_r)


print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容



pp = 0     #行数
nn = 0     #原子数

                    
            
with open(name, 'w') as new_file:
    with open(na, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pp += 1           #行数
            if pp > 2:
                nn += 1       #原子数
                p3x = float(line.split( )[1])
                p3y = float(line.split( )[2])
                p3z = float(line.split( )[3])
                qq = 100          #给qq设置一个较大的初值是为了排除掉字典的长度刚好等于循环的次数
                for key, value in dict_r.items():   #不要忘记了.items
                    if  int(key) == nn:             #注意key在此处为字符串
                        new_file.write(value + '  ' + str(p3x)+'  '+ str(p3y)+'  '+ str(p3z)+ '\n')
                        print("取代原子编号为：",key,"新元素为：",value) 
                        break                       #打破了最小封闭for或while循环
                    qq += 1
                sum = len(dict_r)+100
                if  sum == qq :
                    new_file.write(line)
                        
                        

src = open(name,"r")
fline = str(nn)   #此处是原子数
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
print("共有",row_len ,"行","原子数为 :",row_len-2)

print("-------------")





