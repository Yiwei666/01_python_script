# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:58:22 2023

@author: sun78
"""
import math
import sys
import json


import datetime
from numpy import *
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata


# F01函数，选择输入文件，F代表基础函数
def inputFunction():     # 打印出当前目录下的所有文件名
    print("默认打开当前目录，是否调用GUI获取文件路径?Yes=1,No=2, 直接输入Enter键默认为2")     # 提示命令行输入
    fileOpenStyle = input()
    if fileOpenStyle == '':
        fileOpenStyle = 2
    # fileOpen = int(input())              # 注意字符串输入变量的数据类型转换
    if fileOpenStyle == "1":
        root = tk.Tk()
        root.withdraw()
        f_path = filedialog.askopenfilename()
        txtName = f_path
        print('\n获取的文件地址：', f_path)
    else:
        for root, dirs, files in os.walk("."):
            for filename in files:
                print(filename)  
        print("请输出需要处理的文件名,本例中为json格式，如 49_[扩展-1化合物原子组成数据库]单质或化合物或多相混合体系密度计算.json ")     # 提示命令行输入
        txtName = input()              # 注意字符串输入变量的数据类型转换
    return txtName

# 01函数某列加个特定值
def add_constant_to_column(filename, column_index, constant, output_filename='new_data.txt'):
    row_count = 0  # initialize row count
    with open(filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line or line.startswith('#'):  # skip blank lines and comments
                continue
            row_count += 1  # increment row count
            cols = line.split(' ')  # assuming tab-separated columns
            cols[column_index] = str(float(cols[column_index]) + constant)  # add constant to selected column
            outfile.write(' '.join(cols) + '\n')  # write updated line to output file
    return row_count

# 02函数合并文件
def merge_files(filename1, filename2):
    # Read the contents of the first file into a list, ignoring comments and blank lines
    with open(filename1, 'r') as f1:
        lines1 = [line.strip() for line in f1 if line[0] != '#' and line.strip()]

    # Read the contents of the second file into a list, ignoring comments and blank lines
    with open(filename2, 'r') as f2:
        lines2 = [line.strip() for line in f2 if line[0] != '#' and line.strip()]

    # Combine the two lists and write them to a new file
    merged_lines = lines1 + lines2
    with open('merged.txt', 'w') as f:
        f.write('\n'.join(merged_lines))

    # Print the total number of rows in the merged file
    with open('merged.txt', 'r') as f:
        total_rows = sum(1 for line in f)
    print(f'Total number of rows in merged file: {total_rows}')

# 03函数大于等于
def get_filtered_indices(file_path, column_index, constant):
    """
    Reads a text file and returns a list of line indices where the value in the specified
    column is greater than or equal to the specified constant.

    Parameters:
    file_path (str): The path to the text file.
    column_index (int): The index of the column to filter (starting from 0).
    constant (float): The constant to use as the filter.

    Returns:
    list of int: The indices of the lines that passed the filter.
    """
    # open the text file for reading
    with open(file_path, 'r') as file:
        # read each line of the file and filter the data based on the constant
        filtered_indices = []
        for i, line in enumerate(file):
            if not line.startswith('#') and not line.isspace():
                try:
                    if float(line.split()[column_index]) >= constant:
                        filtered_indices.append(i)
                except ValueError:
                    # ignore lines that don't contain a valid number in the specified column
                    pass

    # return the indices of the filtered lines
    return filtered_indices


# 04函数小于等于
def get_filtered_indices_less(file_path, column_index, constant):
    """
    Reads a text file and returns a list of line indices where the value in the specified
    column is greater than or equal to the specified constant.

    Parameters:
    file_path (str): The path to the text file.
    column_index (int): The index of the column to filter (starting from 0).
    constant (float): The constant to use as the filter.

    Returns:
    list of int: The indices of the lines that passed the filter.
    """
    # open the text file for reading
    with open(file_path, 'r') as file:
        # read each line of the file and filter the data based on the constant
        filtered_indices = []
        for i, line in enumerate(file):
            if not line.startswith('#') and not line.isspace():
                try:
                    if float(line.split()[column_index]) <= constant:
                        filtered_indices.append(i)
                except ValueError:
                    # ignore lines that don't contain a valid number in the specified column
                    pass

    # return the indices of the filtered lines
    return filtered_indices


# 05函数 生成10000行自定义曲面函数的data.txt文件
# import numpy as np

def generate_surface_data(filename, function, x_range, y_range, num_rows):
    """
    Generate data for a 3D surface and save it to a file.
    
    Arguments:
    filename -- the name of the file to save the data to
    function -- the function to use for generating the surface data
    x_range -- a tuple (x_min, x_max) specifying the range of x values
    y_range -- a tuple (y_min, y_max) specifying the range of y values
    num_rows -- the number of rows of data to generate
    
    Returns:
    None
    """
    
    # Create the x, y meshgrid
    x = np.linspace(x_range[0], x_range[1], int(np.sqrt(num_rows)))
    y = np.linspace(y_range[0], y_range[1], int(np.sqrt(num_rows)))
    X, Y = np.meshgrid(x, y)

    # Evaluate the function over the meshgrid
    Z = function(X, Y)

    # Reshape the data to 1D arrays
    x_data = X.flatten()
    y_data = Y.flatten()
    z_data = Z.flatten()

    # Combine the data into a single array
    data = np.column_stack((x_data, y_data, z_data))

    # Save the data to a file
    np.savetxt(filename, data, delimiter=' ')


# 06函数 绘制3列（x,y,z）数据组成的曲面图及其二维填色图 
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from scipy.interpolate import griddata

def plot_fes(datafile, cmap='viridis', levels=40, offset=-25, figsize=(10,6)):
    # 设置 DPI，图像清晰度
    # 通常在 100 到 300 DPI 之间选择一个合适的值即可。如果需要更高的分辨率，可以考虑使用矢量格式的图像，如 PDF、SVG 等，它们不受 DPI 的限制，可以随意缩放而不会失去清晰度。
    plt.rcParams['figure.dpi'] = 600

    # 加载数据
    data = np.loadtxt(datafile)
    x = data[:, 0]
    y = data[:, 1]
    # z = data[:, 2]*4.3597*6.022*100
    z = data[:, 2]
    
    # 创建3D坐标轴
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')

    # 绘制曲面
    ax.plot_trisurf(x, y, z, cmap=cmap)

    # 添加标签和标题
    ax.set_xlabel('Ti-B coordination number')
    ax.set_ylabel('Ti-Al coordination number')
    ax.set_zlabel('Energy (kJ/mol)')
    ax.set_title('3-dimension contour and surface plot')

    # 定义网格
    xi = np.linspace(min(x), max(x), 500)
    yi = np.linspace(min(y), max(y), 500)
    X, Y = np.meshgrid(xi, yi)
    # 设置纵坐标的刻度范围，调整曲面及投影图在坐标系中的相对位置
    ax.set_zlim(-7, 2)

    # 插值数据到网格上
    Z = griddata((x, y), z, (X, Y), method='linear')

    # 绘制投影图
    contour = ax.contourf(X, Y, Z, cmap=cmap, levels=levels, offset=offset)
    # fig.colorbar(contour)

    # 添加colorbar
    # fig.add_axes() 方法用于在图形中添加新的坐标轴对象，参数指定了新坐标轴的位置和大小。这个方法接受一个参数列表 [left, bottom, width, height]，这里的 left 表示新坐标轴的左边缘位置， bottom 表示下边缘位置， width 表示坐标轴的宽度， height 表示坐标轴的高度。
    cbar_ax = fig.add_axes([0.88, 0.10, 0.02, 0.7])
    fig.colorbar(contour, cax=cbar_ax)

    # 设置图片大小
    # fig.set_size_inches(10, 6)

    # 显示图形
    plt.show()



if __name__ == '__main__':
    
    print('''
  本脚本的功能如下:
      01: txt文件特定列加上常数，忽略 空行 和 # 开头行，打印总行数（忽略空行和 # 字开头的）
      02: 将两个txt文件合并，忽略 空行 和 # 开头行，打印总行数（忽略空行和 # 字开头的）
      03: 输出txt文件某列 大于 等于某个数的行号
      04: 输出txt文件某列 小于 等于某个数的行号
      05: 生成10000行自定义曲面函数的data.txt文件
      06: 绘制3列（x,y,z）数据组成的曲面图及其二维填色图
      
      -1: 测试
           
          ''')    
    
    print("请选择功能，输入Enter默认为-1测试")     # 提示选择功能
    defChoose = input()
    
    if  defChoose == "01":
        # Example usage
        filename = inputFunction()
        column_index = int(input("Enter the index of the column to modify (starting from 0): "))
        constant = float(input("Enter the constant to add to the selected column: "))
        row_count = add_constant_to_column(filename, column_index, constant)
        print(f"Total number of rows: {row_count}")

    elif defChoose == "02":
        print("请输入第一个txt文件，先输入的位于合并文件的上方")
        filename1 = inputFunction()
        print("请输入第二个txt文件，后输入的位于合并文件的下方")
        filename2 = inputFunction()
        merge_files(filename1, filename2)

    elif defChoose == "03":
        file_path = inputFunction()
        column_index = int(input('Enter the column index to filter (starting from 0): '))
        constant = float(input('Enter the constant to use as the filter: '))
        
        filtered_indices = get_filtered_indices(file_path, column_index, constant)
        print(f"Indices of filtered lines: {filtered_indices}")
        print("满足要求的原子序号",[i-1 for i in filtered_indices])

    elif defChoose == "04":
        file_path = inputFunction()
        column_index = int(input('Enter the column index to filter (starting from 0): '))
        constant = float(input('Enter the constant to use as the filter: '))
        filtered_indices = get_filtered_indices_less(file_path, column_index, constant)
        print(f"Indices of filtered lines: {filtered_indices}")
        print("满足要求的原子序号",[i-1 for i in filtered_indices])

    elif defChoose == "05":

        def my_surface(x, y):
            return np.sin(np.sqrt(x**2 + y**2))
        
        # Generate data for a 3D surface and save it to a file
        generate_surface_data('surface_data.txt', my_surface, (-5, 5), (-5, 5), 10000)
        
        # Load the data from the file
        #data = np.loadtxt('surface_data.txt')
        
        # Plot the surface
        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        # ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=data[:, 2], cmap='coolwarm')
        # plt.show()

    elif defChoose == "06":
        filename = inputFunction()
        plot_fes(filename, cmap='viridis', levels=40, offset=-7, figsize=(10,6))
        # levels : This parameter specifies the number of contour levels and/or the values of the contour levels to be drawn. By default, levels is set to 10, meaning that the contour plot will have 10 equally spaced levels between the minimum and maximum values of the interpolated data Z. Alternatively, a list of specific contour levels can be passed to the levels parameter to create a custom set of contours.
        # offset : This parameter specifies a constant offset to apply to the Z data, which is useful for creating stacked contour plots. By default, offset is set to None, meaning that the contour plot is drawn at the same Z-level as the interpolated data.

    else:
        print("序号不存在，请重新选择！")






