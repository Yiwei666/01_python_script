# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:33:29 2023

@author: sun78
"""

import os


# 获取当前文件夹下的所有文件名
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# 打印文件名（不包括子文件夹）
for file in files:
    print(file)

# 提示用户输入要处理的文件名
filename = input("请输入要处理的文件名：")

# 读取数据并打印
with open(filename, 'r') as file:
    data = file.readlines()
    for line in data:
        print(line.strip())


def process_data(column_number):
    
    # 存储满足条件的行
    filtered_data = []
    sum_col2 = 0
    sum_col4 = 0

    # 筛选并打印第二列数据为0的行
    print("筛选满足要求的行")
    for line in data:
        if line.strip() != '' and not line.startswith('#'):
            columns = line.split()
            if len(columns) >= column_number and float(columns[column_number-1]) == 0:
                print(line.strip())
                filtered_data.append(columns)
                sum_col2 += float(columns[-2])
                sum_col4 += float(columns[-4])

    # 打印倒数第二列数据和倒数第四列数据的求和
    print("倒数第二列数据的求和：", sum_col2)
    print("倒数第四列数据的求和：", sum_col4)

    # 按照倒数第二列数据递减的顺序打印行
    filtered_data.sort(key=lambda x: float(x[-2]), reverse=True)
    print("按照倒数第二列数据递减的顺序打印：")
    for line in filtered_data:
        print(' '.join(line))
    print("------------------\n")



# 调用函数并传入列数参数
# column_number = int(input("请输入列数："))
column_number = 2
process_data(column_number)

column_number = 3
process_data(column_number)


def process_data_interface(small_column_number, big_column_number):    # 列数，从1开始计数
    
    # 存储满足条件的行
    filtered_data = []
    sum_col2 = 0
    sum_col4 = 0

    # 筛选并打印第二列数据为0的行
    print("筛选满足要求的行")
    for line in data:
        if line.strip() != '' and not line.startswith('#'):
            columns = line.split()
            if len(columns) >= big_column_number and float(columns[small_column_number-1]) != 0 and float(columns[big_column_number-1]) != 0:
                print(line.strip())
                filtered_data.append(columns)
                sum_col2 += float(columns[-2])
                sum_col4 += float(columns[-4])

    # 打印倒数第二列数据和倒数第四列数据的求和
    print("倒数第二列数据的求和：", sum_col2)
    print("倒数第四列数据的求和：", sum_col4)

    # 按照倒数第二列数据递减的顺序打印行
    filtered_data.sort(key=lambda x: float(x[-2]), reverse=True)
    print("按照倒数第二列数据递减的顺序打印：")
    for line in filtered_data:
        print(' '.join(line))
    print("------------------\n")

small_column_number = 2    
big_column_number = 3
process_data_interface(small_column_number, big_column_number)


