# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:33:29 2023

@author: sun78
"""

import os

def get_integers():
    input_str = input("请依次输入O配位数 和 Si配位数 所在列数，用英文逗号隔开，列数从1开始计数: ")
    numbers = input_str.split(",")

    try:
        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())

        return num1, num2

    except ValueError:
        print("Invalid input. Please enter two integers separated by a comma.")
        return None, None


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
    print("倒数第二列数据的求和：", sum_col2, " %")
    print("倒数第四列数据的求和：", sum_col4)

    # 按照倒数第二列数据递减的顺序打印行
    filtered_data.sort(key=lambda x: float(x[-2]), reverse=True)
    print("按照倒数第二列数据递减的顺序打印：")
    for line in filtered_data:
        print(' '.join(line))
    print("------------------\n")


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
    print("倒数第二列数据的求和：", sum_col2, " %")
    print("倒数第四列数据的求和：", sum_col4)

    # 按照倒数第二列数据递减的顺序打印行
    filtered_data.sort(key=lambda x: float(x[-2]), reverse=True)
    print("按照倒数第二列数据递减的顺序打印：")
    for line in filtered_data:
        print(' '.join(line))
    print("------------------\n")



if __name__ == '__main__':

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

    # Call the function and retrieve the results
    num1, num2 = get_integers()

    if num1 is not None and num2 is not None:
        print("First number:", num1)
        print("Second number:", num2)

    # 调用函数并传入列数参数
    # column_number = int(input("请输入列数："))
    print("筛选X-O配位数为0行，位于硅相")
    column_number = num1               # O配位所在列数
    process_data(column_number)


    print("筛选X-Si配位数为0行，位于渣相")
    column_number = num2                  # Si配位所在列数
    process_data(column_number)


    print("筛选位于界面行数")
    small_column_number = num1    
    big_column_number = num2
    process_data_interface(small_column_number, big_column_number)


