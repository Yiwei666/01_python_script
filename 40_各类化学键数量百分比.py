# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:31:22 2023

@author: sun78
"""

# 1. 需要考虑不同列的行数可能不一样，通过将空行替换为“--”来解决该问题

import os

# 获取当前文件夹下的所有文件名
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# 打印文件名（不包括子文件夹）
for file in files:
    print(file)

# 提示用户输入txt文件名
input_file = input('请输入要处理的键级txt文件名: ')

# 打开txt数据文件
with open( input_file , 'r') as file:
    # 逐行读取数据并分割成列
    lines = file.readlines()
    columns = [line.strip().split() for line in lines]

# 转置矩阵以获取每一列
columns_transposed = list(map(list, zip(*columns)))

# 检查所有列的行数是否相同
num_rows = len(columns_transposed[0])
all_columns_same_length = all(len(column) == num_rows for column in columns_transposed)

bond_number = []      # 每一列键的数量
bond_percentage = []  # 偶数列键的百分比

if all_columns_same_length:
    # 统计每一列中"--"的个数
    num_dashes_per_column = [column.count("--") for column in columns_transposed]
    # 计算总行数
    total_rows = num_rows

    # 输出结果
    for i, num_dashes in enumerate(num_dashes_per_column):
        if i % 2 != 0:                 # 判断索引是否为奇数，即偶数列
            print(f"列{i + 1}中化学键的个数：{total_rows-num_dashes},  '--'的个数：{num_dashes}")
        bond_number.append(total_rows-num_dashes)
    print(f"每一列的总行数：{total_rows}")
else:
    print("不同列的行数不相同，无法进行统计。")

print("总的化学键数量为：", sum(bond_number)/2)
for i,j in enumerate(bond_number):
    if i % 2 != 0:                 # 判断索引是否为奇数
        print(f"列{i + 1}中化学键的百分比：{round(j/(sum(bond_number)/2)*100,2)} %")
        bond_percentage.append(round(j/(sum(bond_number)/2)*100,2))
for i in bond_percentage:
    print(i)
