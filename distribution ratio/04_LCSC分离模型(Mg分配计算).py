# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:38:33 2023

@author: sun78
"""

import math

y = 2        # 杂质原子在渣中稳定价态
N_X = 8     # 硅相初始杂质原子B数
N_Si = 42     # 初始硅相Si原子数
N_SiO2 = 40    # SiO2摩尔数
N_MeOi = [43]       # 各碱性氧化物摩尔数，示例值，根据具体情况进行修改 [8.0, 6.0, 4.0]
N_XinSi = 2.61735  # 反应平衡后硅相中剩余的杂质原子数
M_X = 24.305                  # 杂质原子 Mg 相对原子质量


E_X = N_X - N_XinSi     # 从硅相进入到渣相的X杂质原子数

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

print("分配比 L_X:",L_X)
print("分配比取对数 log(L_X, 10):",math.log(L_X, 10))

string = "N_X:"+str(N_X)+"  N_Si:"+str(N_Si)+"  N_SiO2:"+str(N_SiO2)+"  N_MeOi:"+str(N_MeOi)
print(string)
print("N_XinSi:", N_XinSi, "  N_XinSlag:", E_X)
