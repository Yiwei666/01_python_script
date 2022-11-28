

import datetime 
import os                     # 导入时间模块
xx = datetime.datetime.now()          # 显示时间
print("此刻时间：",xx)

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
        
print("-------------")

print("请输出需要处理的文件命名,xyz格式")     # 提示命令行输入
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

print("请输入想要提取的起始帧数，z:")     # 提示命令行输入
z = int(input())              # 注意字符串输入变量的数据类型转换
print("已输入起始帧数： ", z)           # 显示输入的内容

print("请输入想要提取的截止帧数，g:")     # 提示命令行输入
g = int(input())              # 注意字符串输入变量的数据类型转换
print("已输入起始帧数： ", g)           # 显示输入的内容



e = (z-1)*(x+2)+1
f =  g*(x+2)

print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容

m = open( name, "x")   # 创建新文本
m.close()



lnum = 0
with open( na , 'r') as fd:           # 打开上述要处理的xyz源文件na
    print("-------------")
    for line in fd:
        lnum += 1;
        if (lnum >= e) & (lnum <= f):     # 打印的行数范围
            h = open(name , "a")
            h.write(line)
            h.close()
            line = line.strip()    # line.strip()把文本带有的'\n'移除
            print(line)
    print("-------------")

# 以下是计时程序
yy = datetime.datetime.now()
zz = yy-xx
print("共耗时",zz ,"时:分:秒:毫秒")           # 显示输入的内容
