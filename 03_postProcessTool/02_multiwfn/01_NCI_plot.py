import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# 设定块大小
chunksize = 100000

# 创建空的DataFrame用于存储最后两列数据
filtered_data = pd.DataFrame()

# 逐块读取数据并提取符合条件的最后两列
for chunk in pd.read_csv('output.txt', delim_whitespace=True, header=None, chunksize=chunksize):
    # 提取最后两列
    last_two_cols = chunk.iloc[:, -2:]
    # 筛选符合条件的数据
    condition = (last_two_cols.iloc[:, 0] >= -0.05) & (last_two_cols.iloc[:, 0] <= 0.05) & \
                (last_two_cols.iloc[:, 1] >= 0) & (last_two_cols.iloc[:, 1] <= 2)
    filtered_chunk = last_two_cols[condition]
    filtered_data = pd.concat([filtered_data, filtered_chunk], ignore_index=True)

# 随机采样10万行数据用于绘图（如果满足条件的数据少于10万行，则全部使用）
sampled_data = filtered_data.sample(n=min(100000, len(filtered_data)), random_state=1)

# 提取x和y轴数据
x = sampled_data.iloc[:, 0]
y = sampled_data.iloc[:, 1]

# 生成颜色数据，颜色渐变从蓝色到绿色再到红色，基于x值
norm = plt.Normalize(vmin=-0.05, vmax=0.05)

# 使用 rainbow 颜色映射
cmap = plt.get_cmap('rainbow')

# 绘制散点图
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=x, cmap=cmap, norm=norm, alpha=0.6, s=1)
plt.xlabel('sign(λ2)ρ (a.u.)')
plt.ylabel('RDG')
colorbar = plt.colorbar(scatter)
colorbar.set_ticks(np.linspace(-0.05, 0.05, num=11))  # 设置色彩刻度条的范围
plt.grid(False)
plt.show()
