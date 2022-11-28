# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:03:19 2021

@author: sun78
"""

# 对所有原子坐标进行整体平移
# 本脚本是文本某行特定值取代的一个比较典型的方法，注意参考
# 先通过for循环和if语句筛选出特定行，然后通过split语句将字符串分解，然后利用replace进行取代


import datetime                      # 导入时间模块
#import math
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



a=input("请输入原体系中心坐标，如 0,0,0  : ")
p1 = a.split(",")

b=input("请输入目标体系中心坐标，如 0,0,0  : ")
p2 = b.split(",")

#b=input("enter second coordinate : ")
#p2 = b.split(",")

dx=float(p2[0])-float(p1[0])
dy=float(p2[1])-float(p1[1])
dz=float(p2[2])-float(p1[2])


print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容

#m = open( name, "x")   # 创建新文本
#m.close()

pp=0
nn = 0


with open(name, 'w') as new_file:
    with open(na, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pp += 1
            if pp > 2:
                nn += 1
                p3x = float(line.split( )[1]) + dx # 对原分坐标x进行变换
                p3y = float(line.split( )[2]) + dy
                p3z = float(line.split( )[3]) + dz
                #下面一句是核心的语句，注意如何同时写入多个字符串变量，注意字符串的replace()方法；
                #new_file.write(line.replace(line.split( )[1]+line.split( )[2]+line.split( )[3], ' ' + str(p3x)+' '+ str(p3y)+' '+ str(p3z)))
                #其实可以不用取代，取代过于麻烦，直接写入，注意字符串+加号的妙用
                new_file.write(line.split( )[0]+ '  ' + str(p3x)+'  '+ str(p3y)+'  '+ str(p3z)+ '\n')
                print("变换差值为",dx,dy,dz) 
                print("原始坐标为",line.split( )[0],line.split( )[1],line.split( )[2],line.split( )[3])
                print("新的坐标为",line.split( )[0],p3x,p3y,p3z)
                #print("测试语句，原始坐标和新坐标",line.split( )[1]+' '+line.split( )[2]+' '+line.split( )[3], ' ' + str(p3x)+' '+ str(p3y)+' '+ str(p3z))
                #print("测试一下replace语句",line.replace(line.split( )[1]+line.split( )[2]+line.split( )[3], ' ' + str(p3x)+' '+ str(p3y)+' '+ str(p3z)))
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
fline = str(nn)   #此处的nn是原子数
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
print("共有",row_len ,"行","原子数为 :",nn)
      

# 以下是计时程序
y = datetime.datetime.now()
z = y-x
print("共耗时",z ,"时:分:秒:毫秒")           # 显示输入的内容


print("-------------")


