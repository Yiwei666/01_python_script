# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:44:55 2022

@author: sun78
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

x=np.linspace(-10,10,200)
# y=[(1+1/i)**i for i in x]
y=[(1-(i/3)**6)/(1-(i/3)**12) for i in x]
plt.plot(x,y)
# pyplot.gcf().set_facecolor(np.ones(3)* 240 / 255)   # 生成画布的大小

x_major_locator=MultipleLocator(1)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(0.5)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
plt.xlim(-5,10)
#把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
plt.ylim(-4,4)
#把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白

plt.grid()  # 生成网格
plt.show()
for i,j in enumerate(y):
    print(i,j,x[i])

     