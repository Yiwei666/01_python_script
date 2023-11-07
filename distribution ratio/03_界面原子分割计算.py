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
    print("倒数第二列数据的求和：", sum_col2, " %")
    print("倒数第四列数据的求和：", sum_col4)

    # 按照倒数第二列数据递减的顺序打印行
    filtered_data.sort(key=lambda x: float(x[-2]), reverse=True)
    print("按照倒数第二列数据递减的顺序打印：")
    for line in filtered_data:
        print(' '.join(line))
    print("------------------\n")
    return sum_col4, sum_col2               # 依次返回倒数第4列和倒数第2列的值

    
def process_data_interface(small_column_number, big_column_number, XO_slag_ave, XSi_silicon_ave):    # 列数，从1开始计数，small是与O配位的列，big是与Si配位的列
    
    # 存储满足条件的行
    filtered_data = []
    sum_col2 = 0
    sum_col4 = 0
    sum_N_B_in_Si = 0
    sum_N_B_in_slag = 0
    
    
    # 筛选并打印第二列数据为0的行
    print("筛选满足要求的行")
    for line in data:
        if line.strip() != '' and not line.startswith('#'):
            columns = line.split()
            if len(columns) >= big_column_number and float(columns[small_column_number-1]) != 0 and float(columns[big_column_number-1]) != 0:
                total_CN = float(columns[0])   # 总配位数
                BO_CN = float(columns[small_column_number-1])  # 与O配位
                BSi_CN = float(columns[big_column_number-1])   # 与Si配位
                BO_slag_ave = XO_slag_ave
                BSi_silicon_ave = XSi_silicon_ave
                BO_ratio = BO_CN/BO_slag_ave / ( BO_CN/BO_slag_ave + BSi_CN/BSi_silicon_ave )
                BSi_ratio = BSi_CN/BSi_silicon_ave / ( BO_CN/BO_slag_ave + BSi_CN/BSi_silicon_ave )
                N_B_in_Si = float(columns[-4])*BSi_ratio
                N_B_in_slag = float(columns[-4])*BO_ratio
                string = "  BO_ratio: "+str(round(BO_ratio*100,3))+" %   N_B_in_slag: "+str(round(N_B_in_slag,3))+"   BSi_ratio: "+str(round(BSi_ratio*100,3))+" %   N_B_in_Si: "+str(round(N_B_in_Si,3))
                sum_N_B_in_Si += N_B_in_Si
                sum_N_B_in_slag += N_B_in_slag
                
                print(line.strip() + string)
                
                filtered_data.append(columns)
                sum_col2 += float(columns[-2])
                sum_col4 += float(columns[-4])

    # 打印倒数第二列数据和倒数第四列数据的求和
    print("倒数第二列数据的求和：", sum_col2, " %")
    print("倒数第四列数据的求和：", sum_col4)
    print("界面分配到硅相原子数sum_N_B_in_Si：",round(sum_N_B_in_Si,5))
    print("界面分配到渣相原子数sum_N_B_in_slag：",round(sum_N_B_in_slag,5))
    print("界面原子总数sum_N_B_in_Si + sum_N_B_in_slag：",round(sum_N_B_in_Si + sum_N_B_in_slag,5))
    # 按照倒数第二列数据递减的顺序打印行
    filtered_data.sort(key=lambda x: float(x[-2]), reverse=True)
    print("按照倒数第二列数据递减的顺序打印：")
    for line in filtered_data:
        print(' '.join(line))
    return sum_col4, sum_col2, sum_N_B_in_Si, sum_N_B_in_slag               # 依次返回倒数第4列和倒数第2列的值，界面分配到硅相原子数以及界面分配到渣相原子数


if __name__ == '__main__':
        
    input_str = input("请输入O配位数所在列数，Si配位数所在列数，渣中X-O平均配位数，硅中X-Si平均配位数，用英文逗号隔开：")
    numbers = input_str.split(",")  # 将输入的字符串按逗号分割成列表
    numbers = [float(num.strip()) for num in numbers]  # 将列表中的字符串转换为浮点数
    print(numbers)

    # small是与O配位的列，big是与Si配位的列
    small_column_number = int(numbers[0])    # 与O配位
    big_column_number = int(numbers[1])      # 与Si配位
    BO_slag_ave = numbers[2]         # 渣中B-O平均配位数
    BSi_silicon_ave = numbers[3]     # 硅中B-Si平均配位数

    print("【筛选O配位数为0列数，即位于Si相】")
    result_silicon = process_data(small_column_number)  # 筛选O配位数为0列数，即位于Si相
    sum_col4_silicon, sum_col2_silicon = result_silicon

    print("【筛选Si配位数为0列数，即位于渣相】")
    result_silicate = process_data(big_column_number)    # 筛选Si配位数为0列数，即位于渣相
    sum_col4_silicate, sum_col2_silicate = result_silicate

    print("【筛选O配位数以及Si配位数都不为0的列，即位于界面处】")
    result_interface = process_data_interface(small_column_number, big_column_number, BO_slag_ave, BSi_silicon_ave)     # 筛选O配位数以及Si配位数都不为0的列，即位于界面处
    sum_col4_interface, sum_col2_interface, sum_N_B_in_Si_interface, sum_N_B_in_slag_interface = result_interface

    print("------------------\n")
    print("考虑界面分割后位于硅相的X总原子数：", sum_col4_silicon, '+',sum_N_B_in_Si_interface, '=', round(sum_col4_silicon + sum_N_B_in_Si_interface,3))
    print("考虑界面分割后位于渣相的X总原子数：", sum_col4_silicate, '+',sum_N_B_in_slag_interface, '=', round(sum_col4_silicate + sum_N_B_in_slag_interface,3))
