import glob
import pandas as pd
import matplotlib.pyplot as plt

# 查找包含 'origin_g(r)' 字符串的文件
file_list = glob.glob("*origin_g(r)*")

# 遍历所有找到的文件
for file in file_list:
    # 读取文件中的两列数据，假设文件中数据使用空格分隔
    data = pd.read_csv(file, delim_whitespace=True, header=None, names=['x', 'y'])

    # 筛选x在0到6范围内的数据
    filtered_data = data[(data['x'] >= 0) & (data['x'] <= 6)]

    # 绘制x和y的曲线图
    plt.plot(filtered_data['x'], filtered_data['y'], label=file)

# 添加图例和标签
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve for origin_g(r) files')
plt.legend()
plt.show()
