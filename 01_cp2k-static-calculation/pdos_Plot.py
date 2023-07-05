# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:05:33 2023

@author: sun78
"""

import matplotlib.pyplot as plt
import os

# 获取当前文件夹下的所有文件名
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# 打印文件名（不包括子文件夹）
for file in files:
    print(file)

# 提示用户输入文件名
filename = input("请输入文件名（包括后缀名.txt）：")

# 提示用户输入 x 轴范围
# x_min = float(input("请输入 x 轴的最小值："))
# x_max = float(input("请输入 x 轴的最大值："))

x_min = -20
x_max = 60

# 读取数据文件
data = []
with open(filename, 'r') as file:
    for line in file:
        data.append(line.strip().split())

# 解析数据
labels = data[0][1:]  # 第一行的标签
x_data = [float(row[0]) for row in data[1:] if x_min <= float(row[0]) <= x_max]  # 指定范围内的 x 轴数据
y_data = [[] for _ in range(len(labels))]  # 初始化 y 轴数据

for row in data[1:]:
    if x_min <= float(row[0]) <= x_max:
        for i, value in enumerate(row[1:]):
            y_data[i].append(float(value))

# 绘制曲线
plt.figure()

for i in range(len(labels)):
    plt.plot(x_data, y_data[i], label=labels[i])

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


