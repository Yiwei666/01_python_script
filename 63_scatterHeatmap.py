import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def plot_scatter_heatmap():
    """
    从extract.xyz文件中读取数据，并绘制散点图和热力图。
    """
    input_extract_file = "extract.xyz"

    # 从文件读取数据
    with open(input_extract_file, 'r') as infile:
        lines = infile.readlines()

    # 提取x和y数据列
    x_column, y_column = map(int, input("Enter the column numbers for x and y (comma-separated): ").split(','))

    x_data = [float(line.split()[x_column - 1]) for line in lines]
    y_data = [float(line.split()[y_column - 1]) for line in lines]

    # 设置方格的数量
    gridsize = 15

    # 计算每个方格中点的数量
    heatmap, xedges, yedges = np.histogram2d(x_data, y_data, bins=gridsize)

    # 定义自定义颜色映射
    cmap_colors = [(1, 1, 1), (1, 0.6, 0), (0, 0.6, 0), (0, 0, 1)]  # White to orange to green to blue
    custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', cmap_colors, N=256)

    # 绘制散点图
    plt.scatter(x_data, y_data, c='navy', s=10, alpha=0.5)
    

    # 使用自定义颜色映射绘制热力图
    plt.imshow(heatmap.T, extent=(xedges.min(), xedges.max(), yedges.min(), yedges.max()),
               cmap=custom_cmap, interpolation='gaussian', origin='lower', aspect='auto', alpha=0.8, vmin=0, vmax=np.max(heatmap))

    plt.colorbar(label='Density')
    plt.xlabel(f'Column {x_column}')
    plt.ylabel(f'Column {y_column}')
    plt.title('Scatter Plot with Heatmap')
    
    
    plt.xticks(fontname='Times New Roman', fontsize=15)
    plt.yticks(fontname='Times New Roman', fontsize=15)


    # 将标签移到图外边
    plt.legend(['Scatter Plot'], loc='upper center', bbox_to_anchor=(2, 2))
    
    plt.show()

# 示例用法:
plot_scatter_heatmap()
