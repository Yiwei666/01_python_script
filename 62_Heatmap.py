# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:17:36 2023

@author: sun78
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 从data.txt文件中读取数据，假设第一列是索引列
data = pd.read_csv('data.txt', sep='\t', index_col=0)

print(data)

# 使用corr方法计算相关性矩阵，排除第一列
correlation_matrix = data.iloc[:, :].corr()

print(correlation_matrix)

# 获取变量名列表
variable_names = correlation_matrix.columns.tolist()

# 将相关性矩阵转换为二维数组
correlation_array = correlation_matrix.values

# 使用Seaborn设置绘图样式，并增大字号
sns.set(font_scale=1.2)

# 使用sns.heatmap()绘制热力图
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_array, annot=True, cmap='coolwarm', linewidths=0.5, square=True, xticklabels=variable_names, yticklabels=variable_names, vmin=-1, vmax=1)

# 调整横轴标签位置和旋转角度，并设置标签加粗
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, fontsize=15, fontweight='bold')
heatmap.set_yticklabels(heatmap.get_yticklabels(), fontsize=15, fontweight='bold')

# 获取colorbar对象
cbar = heatmap.collections[0].colorbar

# 设置colorbar上刻度数值的字体加粗
cbar.ax.tick_params(labelsize=16, width=2, labelcolor='black')

# 添加标题
# plt.title('Correlation Heatmap')

# 显示热力图
plt.show()










