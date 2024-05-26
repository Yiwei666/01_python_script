import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

def process_data_file(filename, r_min):
    # 读取数据文件
    data = pd.read_csv(filename, delimiter=r'\s+', comment='@', header=None)

    # 获取第一列数据r
    r = data.iloc[:, 0]

    # 获取第二列数据g(r)
    g_r = data.iloc[:, 1]

    # 计算新的第二列数据y
    y = []
    for i in range(len(g_r)):
        if pd.notna(g_r[i]) and pd.notna(r[i]) and g_r[i] != 0:
            y.append(-np.log(g_r[i]) - 2 * np.log(r[i] / r_min))
        else:
            y.append(np.nan)

    # 构建新文件名
    new_filename = "pmf_" + filename + ".txt"

    # 将第一列数据和新得到的第二列数据保存到新文件中
    np.savetxt(new_filename, np.column_stack((r, y)), fmt='%.6f', delimiter=' ')

    # 绘制图表
    plt.figure()
    plt.plot(r, y)
    plt.grid(True)
    plt.xlabel('r')
    plt.ylabel('y')
    plt.title('Plot')
    plt.show()

if __name__ == '__main__':
    # 获取当前文件夹下的所有文件名
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    # 打印文件名（不包括子文件夹）
    for file in files:
        print(file)

    # 测试示例
    filename = input("请输入数据文件名: ")
    r_min = float(input("请输入截断半径r_min: "))
    process_data_file(filename, r_min)
