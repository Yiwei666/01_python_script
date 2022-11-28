# 源码https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
# Python program to
# demonstrate merging
# of two files

import datetime                      # 导入时间模块
x = datetime.datetime.now()          # 显示时间
print("此刻时间：",x)

  
data = data2 = ""

print("请输出需要合并的文件1名,txt/xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

# Reading data from file1
with open( na ) as fp:
    data = fp.read()

print("请输出需要合并的文件2名,txt/xyz格式")     # 提示命令行输入
ma = input()              # 注意字符串输入变量的数据类型转换

# Reading data from file2
with open( ma ) as fp:
    data2 = fp.read()
  
# Merging 2 files
# To add the data of file2
# from next line

#data += "\n", 把换行删掉了，注意换行语句怎么写
data += data2
  
print("请输出合并后的文件名3,txt/xyz格式")     # 提示命令行输入
ba = input()              # 注意字符串输入变量的数据类型转换

with open ( ba , 'w') as fp:
    fp.write(data)


print("已完成文件 ", ba, " 的合并")           # 显示输入的内容


# 以下是计时程序
y = datetime.datetime.now()
z = y-x
print("共耗时",z ,"时 分 秒 毫秒")           # 显示输入的内容



