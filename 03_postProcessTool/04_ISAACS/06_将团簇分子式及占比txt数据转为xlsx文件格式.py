import os
import pandas as pd

# 获取当前脚本所在目录
current_directory = os.getcwd()

# 打印当前目录下的所有文件名
files = os.listdir(current_directory)
print("当前目录下的所有文件:")
for idx, file in enumerate(files):
    print(f"{idx + 1}: {file}")

# 提示用户选择文件
file_index = int(input("请输入文件序号: ")) - 1
selected_file = files[file_index]

# 检查用户选择的是否为文件
if not os.path.isfile(selected_file):
    print("选择的不是一个文件!")
    exit()

# 存储含有 "%" 的行
rows_with_percentage = []

# 逐行读取文件并判断是否包含 "%"
with open(selected_file, 'r', encoding='utf-8') as file:
    for line in file:
        if '%' in line:
            # 去掉多余的空格并使用空格分隔
            cleaned_line = ' '.join(line.split())
            rows_with_percentage.append(cleaned_line.split(' '))  # 将每一行分割为多个列

# 将结果写入到新的 Excel 文件中
output_file = selected_file.split('.')[0] + ".xlsx"
df = pd.DataFrame(rows_with_percentage)
df.to_excel(output_file, index=False, header=False)

print(f"处理完成，包含 % 的行已写入文件: {output_file}")
