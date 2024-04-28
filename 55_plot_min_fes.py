import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, NullFormatter
import math

def find_and_plot_min_z_in_grids(file_name):
    # 初始化数据和界限
    data = []
    x_min, x_max, y_min, y_max = float('inf'), -float('inf'), float('inf'), -float('inf')

    # 读取数据并确定界限
    with open(file_name, 'r') as f:
        for line in f:
            x, y, z = map(float, line.split())
            data.append((x, y, z))
            if x < x_min:
                x_min = x
            if x > x_max:
                x_max = x
            if y < y_min:
                y_min = y
            if y > y_max:
                y_max = y

    # 初始化网格字典以存储每个网格内的最小z值
    grid_min_z = {}
    for x in range(int(x_min), int(x_max) + 1):
        for y in range(int(y_min), int(y_max) + 1):
            grid_min_z[(x, y)] = {'z': float('inf'), 'x': None, 'y': None}

    # 更新每个网格内的最小z值
    for x, y, z in data:
        grid_x = int(x)
        grid_y = int(y)
        if z < grid_min_z[(grid_x, grid_y)]['z']:
            grid_min_z[(grid_x, grid_y)] = {'z': z, 'x': x, 'y': y}

    # 准备绘图数据
    num_x = int(x_max) - int(x_min) + 1
    num_y = int(y_max) - int(y_min) + 1
    z_values = np.full((num_y, num_x), np.nan)
    labels = np.full((num_y, num_x), "", dtype=object)

    # 填充绘图数组
    for key, value in grid_min_z.items():
        if value['z'] != float('inf'):
            ix = key[0] - int(x_min)
            iy = key[1] - int(y_min)
            scaled_z = value['z'] * 4.3597 * 6.022 * 100
            z_values[iy, ix] = scaled_z
            labels[iy, ix] = f"{value['x']:.2f}\n{value['y']:.2f}\n{scaled_z:.1f}"

    # 绘图
    fig, ax = plt.subplots(dpi=800)
    cax = ax.matshow(z_values, cmap='viridis', origin='lower')
    # 只显示次刻度对应的网格线
    ax.grid(which='minor', linestyle='-', linewidth=0.5, color='gray', alpha=0.5)
    
    for (i, j), label in np.ndenumerate(labels):
        if label:
            ax.text(j, i, label, va='center', ha='center', color='white', fontsize=3.8)

    # 设置次刻度标签为整数
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.xaxis.set_minor_formatter(plt.FuncFormatter(lambda x, _: f"{int(x_min + x)}"))
    
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_major_formatter(NullFormatter())
    # y轴刻度整体加1
    ax.yaxis.set_minor_formatter(plt.FuncFormatter(lambda y, _: f"{math.ceil(y_min + y)}"))

    fig.colorbar(cax)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.xaxis.tick_bottom()
    plt.title('Scaled minimum z values in each grid')
    plt.show()

# 调用函数
find_and_plot_min_z_in_grids('fes.dat')
