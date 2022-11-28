# 该脚本的核心算法是计算两点间的距离，该距离小于半径则写入新文件中。
# https://www.w3resource.com/python-exercises/python-basic-exercise-40.php
# 
import os
import datetime                      # 导入时间模块
import math
x = datetime.datetime.now()          # 显示时间
print("此刻时间：",x)

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)

print("-------------")

print("请输出需要处理的文件名,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

#下面是把文本中的每一行转换成列表中的字符串
mylines = []                                # Declare an empty list.
with open ( na , 'rt') as myfile:    # Open lorem.txt for reading text.
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.rstrip('\n')) # strip newline and add to list.
        
for element in mylines: # 对于列表中的每个元素，
    print(element) # 打印它。


#a=input("enter first coordinate : ")
r = float(input("请输入球形半径，如"))  #a是浮点数
print("已输入球形半径: ",r)

a=input("请输入中心原子坐标，如 0,0,0  : ")
p1 = a.split(",")

#b=input("enter second coordinate : ")
#p2 = b.split(",")


print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容

m = open( name, "x")   # 创建新文本
m.close()


pp=0
nn = 0

for line in mylines:          # string to be searched
    pp += 1
    if pp > 2:
        p2 = line.split( )
        print ("这是行数：",pp ,"p2分开后是：", p2,)
        distance = math.sqrt( ((float(p1[0])-float(p2[1]))**2)+((float(p1[1])-float(p2[2]))**2)+((float(p1[2])-float(p2[3]))**2) )
        print("实际距离是 ",distance) 
        if distance < r:
            print("距离满足条件，进行写入 ",distance) 
            h = open(name , "a")
            h.write(line)
            h.write('\n')       #换行
            print(line)
            nn += 1
            h.close()


            
#下面是给首行添加原子数的语句
#We read the existing text from file in READ mode 
src = open(name,"r")
fline = str(nn)
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
print("共有",row_len ,"行" )
      




# 以下是计时程序
y = datetime.datetime.now()
z = y-x
print("共耗时",z ,"时:分:秒:毫秒")           # 显示输入的内容


print("-------------")
