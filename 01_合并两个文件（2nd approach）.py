# https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
# Python program to
# demonstrate merging of
# two files

import datetime                      # 导入时间模块
x = datetime.datetime.now()          # 显示时间
print("此刻时间：",x)


# Creating a list of filenames

print("请输出需要合并的文件1名,txt/xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

print("请输出需要合并的文件2名,txt/xyz格式")     # 提示命令行输入
ma = input()              # 注意字符串输入变量的数据类型转换

filenames = [ na, ma ]

print("请输出合并后的文件名3,txt/xyz格式")     # 提示命令行输入
ba = input()              # 注意字符串输入变量的数据类型转换
  
# Open file3 in write mode
with open( ba, 'w') as outfile:
  
    # Iterate through list
    for names in filenames:
  
        # Open each file in read mode
        with open(names) as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())
  
        # Add '\n' to enter data of file2
        # from next line
        # outfile.write("\n") 注意此处把换行给注释掉了

print("已完成文件 ", ba, " 的合并")           # 显示输入的内容


# 以下是计时程序
y = datetime.datetime.now()
z = y-x
print("共耗时",z ,"时:分:秒:毫秒")           # 显示输入的内容
