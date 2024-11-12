import os
import re
import pandas as pd

# 定义常数
i, j, k, l = 1.16, 1.14, 0.657, 0.186

# 定义输出的Excel文件名
output_file = "最近邻和次近邻_MBO_sum.xlsx"
results = []

# 获取当前目录中所有的txt文件
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

# 正则表达式用于解析key字符串
element_pattern = re.compile(r"(B|Si|Al|O)(\d*)")

for txt_file in txt_files:
    data = []
    with open(txt_file, 'r') as file:
        # 读取只包含 '%' 的行
        for line in file:
            if '%' in line:
                data.append(line.strip().split())
    
    # 检查列数是否一致
    col_counts = {len(row) for row in data}
    if len(col_counts) != 1:
        print(f"{txt_file} 中数据列数不一致，程序终止。")
        exit(1)

    # 构建字典
    data_dict = {}
    for row in data:
        key = row[-1]  # 最后一列作为键
        # 获取倒数第7列、倒数第2列和倒数第4列的值
        list_vals = [float(row[-7]), float(row[-2]), float(row[-4])]
        
        # 检查键是否唯一
        if key in data_dict:
            print(f"{txt_file} 中的键 {key} 重复，程序终止。")
            exit(1)

        data_dict[key] = list_vals

    # 计算sv和sw
    sv, sw = 0, 0
    for key, list_vals in data_dict.items():
        # 使用正则表达式解析a, b, c, d
        elements = {'B': 0, 'Si': 0, 'Al': 0, 'O': 0}  # 初始化元素数量
        for match in element_pattern.finditer(key):
            elem = match.group(1)
            count = int(match.group(2)) if match.group(2) else 1
            elements[elem] = count

        a, b, c, d = elements['B'], elements['Si'], elements['Al'], elements['O']

        # 计算x、v、w
        x = d - a - b - c
        v = 0.01 * list_vals[2] * (a * i + b * j + c * k + x * l)
        w = 0.01 * list_vals[2] * (1.16 * d)

        # 累加v和w
        sv += v
        sw += w

    print(f"{txt_file} 的 sv: {sv}, sw: {sw}")
    results.append({"文件名": txt_file, "sv": sv, "sw": sw})

# 将结果写入Excel文件
df = pd.DataFrame(results)
df.to_excel(output_file, index=False)
print(f"结果已写入 {output_file}")
