# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:25:36 2021

@author: sun78
"""


import math
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


pi = math.pi
e = math.e
a = 52.92 # 单位埃
#print (pi,e)


x = np.arange(0,5000, 1)
y = 4500*np.power(0.9998192975, x) 

#y =1/(pi*a**3) * np.power(e, -2*x/a)
#y = np.sin(x)*np.cos(x)

plt.xlim(0, 6000)  # x轴范围
plt.ylim(0,5000) # y轴范围

plt.xlabel('Step')
plt.ylabel('Temperature')
plt.title("指数函数")
plt.plot(x, y)
plt.grid()  #添加网格线
plt.show()


