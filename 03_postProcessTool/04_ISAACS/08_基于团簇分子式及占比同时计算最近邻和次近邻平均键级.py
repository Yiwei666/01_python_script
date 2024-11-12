import os
import re
import pandas as pd

# 设置常数
i = 1.16
j = 1.14
k = 0.657
l = 0.186

# 获取当前目录下的所有txt文件
txt_files = [f for f in os.listdir() if f.endswith('.txt')]

# 定义输出数据
results = []

# 处理每个txt文件
for txt_file in txt_files:
    data = []
    file_path = os.path.join(os.getcwd(), txt_file)
    
    # 读取文件内容并过滤出含有“%”的行
    with open(file_path, 'r') as file:
        for line in file:
            if '%' in line:
                line_data = line.strip().split()
                data.append(line_data)
    
    # 检查列数是否一致
    col_counts = set(len(row) for row in data)
    if len(col_counts) > 1:
        print(f"文件 {txt_file} 中的data列数不一致，程序终止。")
        exit()

    # 构建字典
    data_dict = {}
    for row in data:
        key = row[-1]
        if key in data_dict:
            print(f"文件 {txt_file} 中存在重复的键 {key}，程序终止。")
            exit()
        try:
            a = int(re.search(r'B(\d+)', key).group(1)) if 'B' in key else 0
            b = int(re.search(r'Si(\d+)', key).group(1)) if 'Si' in key else 0
            c = int(re.search(r'Al(\d+)', key).group(1)) if 'Al' in key else 0
            d = int(re.search(r'O(\d+)', key).group(1)) if 'O' in key else 0
        except AttributeError:
            print(f"文件 {txt_file} 中的键 {key} 不符合格式，程序终止。")
            exit()
        
        # 计算x和v值
        x = d - a - b - c
        list_values = [float(row[-7]), float(row[-2]), float(row[-4])]
        v = 0.01 * list_values[2] * (a * i + b * j + c * k + x * l)
        
        data_dict[key] = list_values + [v]

    # 计算s值
    s = sum(entry[-1] for entry in data_dict.values())
    results.append({'文件名': txt_file, 's值': s})
    print(f"{txt_file} 的 s 值: {s}")

# 将结果写入到xlsx文件
df = pd.DataFrame(results)
output_file = "MBO_sum.xlsx"
df.to_excel(output_file, index=False)

print(f"所有文件的s值已保存至 {output_file}")
