import glob
import pandas as pd
import matplotlib.pyplot as plt

# 查找包含 'origin_g(r)' 字符串的文件
file_list = glob.glob("*origin_g(r)*")

# 如果没有找到符合条件的文件，提示用户并退出
if not file_list:
    print("未找到文件名中包含 'origin_g(r)' 的文件。")
    exit()

# 打印所有找到的文件及对应序号
print("找到以下文件：")
for idx, file in enumerate(file_list):
    print(f"{idx}: {file}")

# 提示用户输入需要绘制的文件序号（多个序号之间用英文逗号分隔）
selected_indices = input("请输入需要绘制文件的序号（多个序号之间使用英文逗号分隔）：")

# 将输入的序号转换为整数列表
try:
    indices = [int(x.strip()) for x in selected_indices.split(',')]
except ValueError:
    print("输入无效，请确保输入的是数字，多个数字之间使用英文逗号分隔。")
    exit()

# 根据用户输入的序号选择文件（并对越界的索引进行提示）
selected_files = []
for i in indices:
    if 0 <= i < len(file_list):
        selected_files.append(file_list[i])
    else:
        print(f"警告：序号 {i} 越界，已跳过。")

# 如果没有有效的文件被选中，则退出
if not selected_files:
    print("没有有效的文件被选中，程序退出。")
    exit()

# 遍历选中的文件，读取数据并绘图
for file in selected_files:
    # 读取文件中两列数据，假设数据使用空格分隔
    data = pd.read_csv(file, delim_whitespace=True, header=None, names=['x', 'y'])
    
    # 筛选 x 在 0 到 6 范围内的数据
    filtered_data = data[(data['x'] >= 0) & (data['x'] <= 6)]
    
    # 绘制曲线
    plt.plot(filtered_data['x'], filtered_data['y'], label=file)

# 添加图例和标签
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve for selected origin_g(r) files')
plt.legend()
plt.show()
