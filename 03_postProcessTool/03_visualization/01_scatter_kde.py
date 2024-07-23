import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 生成示例数据
np.random.seed(0)
BL = np.random.uniform(1.5, 4.0, 300)
MBO = 2.0 * np.exp(-BL) + np.random.normal(0, 0.1, 300)

# 创建一个DataFrame
data = pd.DataFrame({'BL': BL, 'MBO': MBO})

# 绘制散点图和密度图
plt.figure(figsize=(10, 6))

# 散点图
sns.scatterplot(data=data, x='BL', y='MBO', s=50, color='blue', edgecolor='w', alpha=0.5)

# 密度图
sns.kdeplot(data=data, x='BL', y='MBO', cmap="Reds", shade=True, alpha=0.6)

# 设置标题和标签
plt.title('Scatter Plot with Density Overlay', fontsize=16)
plt.xlabel('BL (Å)', fontsize=14)
plt.ylabel('MBO', fontsize=14)

# 显示图例
plt.legend(labels=['Scatter Plot', 'Density Plot'])

# 显示图形
plt.show()
