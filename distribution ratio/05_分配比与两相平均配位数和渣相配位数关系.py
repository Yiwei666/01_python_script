# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:24:43 2023

@author: sun78
"""


import math
import numpy as np
import matplotlib.pyplot as plt


# variable_x = CN_two_ave / CN_slag_ave
def logL_CN(variable_x, M_X, y):       # 杂质原子 X 相对原子质量, 

    # y = 4        # 杂质原子在渣中稳定价态
    N_X = 8      # 硅相初始杂质原子B数
    N_Si = 42     # 初始硅相Si原子数
    N_SiO2 = 40    # SiO2摩尔数
    N_MeOi = [43]       # 各碱性氧化物摩尔数，示例值，根据具体情况进行修改 [8.0, 6.0, 4.0]
    # N_XinSi = 8-5.684654   # 反应平衡后硅相中剩余的杂质原子数
    # M_X = 47.867                  # 杂质原子 Ti 相对原子质量
    
    # CN_two_ave =  E_X / N_X * CN_slag_ave
    
    # variable_x = CN_two_ave / CN_slag_ave
    
    E_X =  variable_x * N_X
    
    # E_X = N_X - N_XinSi     # 从硅相进入到渣相的X杂质原子数
    
    M_SiO2 = 60.0843   # SiO2相对分子质量
    M_MeOi = [56.0774]  # 各碱性氧化物相对分子质量，示例值，根据具体情况进行修改 [1.2, 0.9, 0.7]
    
    j = len(N_MeOi)     
    M_Si = 28.0855                # Si相对原子质量
    
    
    # 分子的第一项
    numerator_part1 = (N_Si + (y / 4) * E_X) * M_Si
    
    # 分子的第二项
    numerator_part2 = (N_X - E_X) * M_X
    
    # 分母的第一项
    denominator_part1 = N_SiO2 * M_SiO2
    
    # 分母的第二项
    denominator_part2 = sum(N_MeOi[i] * M_MeOi[i] for i in range(0, j))
    
    # 分母的第三项
    denominator_part3 = (y / 4) * E_X * M_Si
    
    # 分母的第四项
    denominator_part4 = E_X * M_X
    
    # 计算最终结果
    L_X = (E_X / (N_X - E_X)) * (numerator_part1 + numerator_part2) / (denominator_part1 + denominator_part2 - denominator_part3 + denominator_part4)

    return math.log(L_X, 10)

"""
print("分配比 L_X:",L_X)
print("分配比取对数 log(L_X, 10):",math.log(L_X, 10))

string = "N_X:"+str(N_X)+"  N_Si:"+str(N_Si)+"  N_SiO2:"+str(N_SiO2)+"  N_MeOi:"+str(N_MeOi)
print(string)
print("N_XinSi:", N_XinSi, "  N_XinSlag:", E_X)
"""



def plot_lists(x, y):
    # 检查输入列表的长度是否相同
    if len(x) != len(y):
        print("Error: The lengths of the input lists are not equal.")
        return

    # 创建图形
    plt.plot(x, y)

    # 添加标题和坐标轴标签
    plt.title("Plot of x and y")
    plt.xlabel("x")
    plt.ylabel("y")

    # 显示图形
    plt.show()

# import matplotlib.pyplot as plt

def plot_graph(x, y1, y2, y3):
    plt.plot(x, y1, label='Y1')
    plt.plot(x, y2, label='Y2')
    plt.plot(x, y3, label='Y3')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot')
    
    plt.legend()
    plt.show()


def save_to_file(x, y1, y2, y3):
    with open('distribution.dat', 'w') as file:
        for i in range(len(x)):
            line = f"{x[i]} {y1[i]} {y2[i]} {y3[i]}\n"
            file.write(line)


# my_list = np.arange(0, 1.02, 0.02)
# variable_x_list = [i * 0.0002 for i in range(1,50)]

variable_x_list = np.arange(0.001, 1, 0.001)

# M_Ti = 47.867
# M_P = 30.973762
# M_Mg = 24.305

logL_CN_list_P = [logL_CN(i, 30.973762, 5) for i in variable_x_list]
logL_CN_list_Mg = [logL_CN(i, 24.305, 2) for i in variable_x_list]
logL_CN_list_Ti = [logL_CN(i, 47.867, 4) for i in variable_x_list]
# print(logL_CN_list)

# 绘制单个图表
# plot_lists(variable_x_list,logL_CN_list)

# 3个图表绘于一张图中
plot_graph(variable_x_list, logL_CN_list_P, logL_CN_list_Mg, logL_CN_list_Ti)

save_to_file(variable_x_list, logL_CN_list_P, logL_CN_list_Mg, logL_CN_list_Ti)



