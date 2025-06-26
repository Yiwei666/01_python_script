import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 列出当前目录下所有文件
print("当前目录下文件：")
for fname in os.listdir('.'):
    print(fname)

# 提示用户输入要读取的数据文件名
filename = input("请输入要绘图的数据文件名（例如 lcurve.out）：")

# 读取并解析曲线数据
with open(filename) as f:
    headers = f.readline().split()[1:]
lcurve = pd.DataFrame(np.loadtxt(filename), columns=headers)

# 指定要绘制的曲线
legends = ["rmse_e_val", "rmse_e_trn", "rmse_f_val", "rmse_f_trn"]

# 横轴线性，纵轴对数
for legend in legends:
    plt.semilogy(lcurve["step"], lcurve[legend], label=legend)

plt.legend()
plt.xlabel("Training steps")
plt.ylabel("Loss (log scale)")
plt.title(f"Learning Curve: {filename}")
plt.show()
