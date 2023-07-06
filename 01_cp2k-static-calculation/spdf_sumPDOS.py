# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:05:09 2023

@author: sun78
"""

import os


def process_data_file(filename):
    # 读取数据文件
    with open(filename, 'r') as file:
        lines = file.readlines()

    # 过滤第一行，并处理数据列
    data = []
    for line in lines[1:]:  # 从第二行开始读取数据
        line_data = line.strip().split()
        if len(line_data) == 2 or len(line_data) == 5 or len(line_data) == 10 or len(line_data) == 17:
            if len(line_data) == 17:
                processed_data = [
                    line_data[0],
                    line_data[1],
                    sum(map(float, line_data[2:5])),
                    sum(map(float, line_data[5:10])),
                    sum(map(float, line_data[10:17]))
                ]
            elif len(line_data) == 10:
                processed_data = [
                    line_data[0],
                    line_data[1],
                    sum(map(float, line_data[2:5])),
                    sum(map(float, line_data[5:10]))
                ]
            elif len(line_data) == 5:
                processed_data = [
                    line_data[0],
                    line_data[1],
                    sum(map(float, line_data[2:5]))
                ]
            else:
                processed_data = line_data

            data.append(processed_data)

    # 将处理后的数据保存到新的txt文件
    output_filename = 'processed_' + filename
    with open(output_filename, 'w') as output_file:
        if len(data) > 0:
            num_columns = len(data[0])
            if num_columns == 2:
                header = 'Energy_[eV]\ts\n'
            elif num_columns == 5:
                header = 'Energy_[eV]\ts\tp\td\tf\n'
            elif num_columns == 10:
                header = 'Energy_[eV]\ts\tp\td\tf\n'
            elif num_columns == 17:
                header = 'Energy_[eV]\ts\tp\td\tf\n'

            output_file.write(header)
            for line_data in data:
                output_file.write('\t'.join(map(str, line_data)) + '\n')

    print('数据处理完成，结果已保存到文件:', output_filename)


# 获取当前文件夹下的所有文件名
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# 打印文件名（不包括子文件夹）
for file in files:
    print(file)

# 提示用户输入txt文件名
filename = input('请输入要处理的txt文件名: ')
process_data_file(filename)
