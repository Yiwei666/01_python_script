# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:48:11 2021

@author: sun78
"""
# 通过对列表的操作，将多个文件合并
# g(r)[Si,O ]/g(r)[Si,F ]/g(r)[Ca,O ]/g(r)[Ca,F ]/g(r)[O ,O ]/g(r)[Si,Ca]    
# g(r)[Ca,F ]/g(r)[Ca,O ]/g(r)[O ,O ]/g(r)[Si,Ca]/g(r)[Si,F ]/g(r)[Si,O ]    
# dn(r)[Ca,F ]/dn(r)[Ca,O ]/dn(r)[O ,O ]/dn(r)[Si,Ca]/dn(r)[Si,F ]/dn(r)[Si,O ]


import os


for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)  
        
print("-------------")
print("如果需要为g(r)曲线进行梯度增高变换，请输入梯度值，如3,将按照0*3,1*3,2*3,3*3等进行增高;如不需要，则输入0")     # 提示命令行输入
nu = float(input())              # 注意字符串输入变量的数据类型转换


print("请按顺序依次输入需要批量处理的文件名,用/号分隔，ISAACS导出的g(r)[Si,O]或dn(r)[Si,O]数据文件格式")     # 提示命令行输入
na_g = input()              # 注意字符串输入变量的数据类型转换

file_list = na_g.split("/")   # ['g(r)[Ca,F ]', 'g(r)[Ca,O ]', 'g(r)[O ,O ]', 'g(r)[Si,Ca]', 'g(r)[Si,F ]', 'g(r)[Si,O ]']
print ("输入的所有文件名为：",file_list)
length = len(file_list)

# 下面用循环创建多个列表并命名


list1 = []   #list1是所有列表名字集合
for i in range(length):  #注意range索引从0开始,1-5,共计6个数字
    name_x = "x"+ str(i) 
    name_y = "y"+ str(i)
    list1.append(name_x)
    list1.append(name_y)
#    [] = name_x 
#    [] = name_y 
print ("列表长度为:",length,"所有的列表名为:",list1)


list2 = []              # 所有空列表集合
for i in list1:  # ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']
    list1 = []
    list2.append(list1)
print ("空列表集合为:",list2)  # [[], [], [], [], [], [], [], [], [], [], [], []]


j  = 0

while j < length:
    pp = 0
    with open(file_list[j], 'r') as f:  # ['g(r)[Ca,F ]', 'g(r)[Ca,O ]', 'g(r)[O ,O ]', 'g(r)[Si,Ca]', 'g(r)[Si,F ]', 'g(r)[Si,O ]']
        print("-----")
        lines = f.readlines()
        for line in lines:
            pp += 1
#            x_f = "x"+ str(i)
#            y_f = "y"+ str(i)            
            if pp == 16:           #第16行的格式为: @    s0 legend  "dn\sij\N(r)[Si,O]"
                title = line.split( )[3] # @    s0 legend  "g\sij\N(r)[Si,O]" 
    #            title1 = title[1]+title[-10:-2]#
                list2[2*j].append("r")
                list2[2*j+1].append(title)
            if pp > 18:
    
                p3x1 = float(line.split( )[0])          
                p3y1 = float(line.split( )[1])+ nu*j
    
                list2[2*j].append(p3x1)
                list2[2*j+1].append(p3y1)
    j += 1
    print("索引",j)

#list_all = []
#for i in range(length):
#    x_f = "x"+ str(i)
#    y_f = "y"+ str(i)   
#    list_all.append(x_f)
#    list_all.append(y_f)
    
print("写入的多维列表为:",list2)

k = 0
while k < len(list2):
    len1 = len(list2[k])
    print("列表索引为",k,"时，该索引列表长度为:",len1)
    k += 1

f1 = []   # 每一行为一个列表

l = 0
while l < len(list2[0]):
    u = 0
    f = []
    while u < len(list2):
        f.append(list2[u][l])
        u += 1
    print ("每一行合并后的列表",f)
    f1.append(f)
    l += 1
print ("合并后的多维列表",f1)


print("请为输出文件命名,txt格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
#print("已输入文件名 ", name)           # 显示输入的内容


#print("已输入文件名 ", name)           # 显示输入的内容

with open(name, 'w') as new_file:  # 有则覆盖，没有则创建
    for li in f1:
        l1 = 0
        str1 = ""
        while l1 < len(li):  # ['r', '"g\\sij\\N(r)[Ca,F]"', 'r', '"g\\sij\\N(r)[Ca,O]"', 'r', '"g\\sij\\N(r)[O,O]"', 'r', '"g\\sij\\N(r)[Si,Ca]"', 'r', '"g\\sij\\N(r)[Si,F]"', 'r', '"g\\sij\\N(r)[Si,O]"']
            str1 += str(li[l1])+"     "
            l1   +=  1
        new_file.write(str1+"\n")



        
    




    
    