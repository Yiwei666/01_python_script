# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 17:13:55 2021

@author: sun78
"""

import numpy as np
import os                     # 导入时间模块

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
        
print("-------------")

print("请输出需要处理的文件命名,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

x = np.loadtxt(na)

print(x.shape)

print(x)

print(x[:,1])