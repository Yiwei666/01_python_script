# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:31:22 2023

@author: sun78
"""

# 1. 需要考虑不同列的行数可能不一样，通过将空行替换为“--”来解决该问题

import os


def float_or_dash(value):       # 将值转换为浮点数，如果是'--'，则设置为0.0
    return float(value) if value != '--' else 0.0


def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = [list(map(float_or_dash, line.strip().split())) for line in lines]
    # print(data)
    return data                 # 返回一个列表，列表中的每个元素是一个列表，[[1.654, 0.983, 3.382, 0.033, 1.76, 1.656], [1.656, 1.493, 2.936, 0.04, 1.756, 1.028], [1.566, 1.075, 3.137, 0.036, 1.887, 0.722], 


def calculate_sums(data):
    sums = []
    for i in range(1, len(data[0]), 2):  # 从第二列开始，步长为2取偶数列
        column_sum = sum(float_or_dash(row[i]) for row in data)      # 对指定的每一列进行求和
        sums.append(column_sum)          # 
    print(sums)
    
    return sums


def main(file_path, box_length):
    # file_path = 'your_txt_file.txt'
    
    data = read_txt_file(file_path)
    
    # data = [[1.654, 0.983, 3.382, 0.033, 1.76, 1.656], [1.656, 1.493, 2.936, 0.04, 1.756, 1.028], [1.566, 1.075, 3.137, 0.036, 1.887, 0.722], 

    even_sums = calculate_sums(data)
    
    total_sum = sum(even_sums)

    percentages = [round(sum_n / total_sum*100,2) for sum_n in even_sums]

    print("各偶数列的和:", even_sums)
    print("总和:", total_sum)
    print("各偶数列的和占总和的百分比:", percentages)
    print("体系中各化学键的键序密度：", [ round(i/(box_length ** 3),4) for i in even_sums ] )
    print("总键序密度：", round(total_sum/(box_length ** 3),4))

    return even_sums, total_sum           # 


if __name__ == "__main__":
    
    # 获取当前文件夹下的所有文件名
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # 打印文件名（不包括子文件夹）
    for file in files:
        print(file)
    
    # 提示用户输入txt文件名
    input_file = input('请输入要处理的键级txt文件名: ')
    box_length = float(input('请输入电子结构计算的立方模型盒子边长，单位, Å：'))

    main(input_file, box_length)


