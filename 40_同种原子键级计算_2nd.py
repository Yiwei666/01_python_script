# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:52:40 2023

@author: sun78
"""

import os

def filter_and_save_data(input_file, output_file):
    retained_data = []
    discarded_data = []
    seen = set()

    with open(input_file, 'r') as file:
        lines = file.readlines()
        
    i = 0
    j = 0
    
    for line in lines:
        a_b, col_2, col_3 = line.strip().split()
        a, b = map(int, a_b.split(':'))
        # col_2, col_3 = b, a

        if a != b and (b, a) not in seen:
            retained_data.append(line)
            seen.add((a, b))
            i = i + 1
        else:
            discarded_data.append(line)
            j = j + 1

    with open(output_file, 'w') as file:
        
        file.writelines(retained_data)
        file.write("Retained Data:"+ str(i) + '\n')
        
        file.write("----------------------\n")
        
        file.writelines(discarded_data)
        file.write("Discarded Data:" + str(j) + '\n')


if __name__ == "__main__":
    
    # 获取当前文件夹下的所有文件名
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # 打印文件名（不包括子文件夹）
    for file in files:
        print(file)
    
    # 提示用户输入txt文件名
    input_file_path = input('请输入要处理的txt文件名,如 bondOrder_Si-Si.txt: ')
    
    output_file_path = "bondOrder_retain_2nd.txt"

    filter_and_save_data(input_file_path, output_file_path)
    print("输出的数据保存在 bondOrder_retain_2nd.txt 文件中")
