"""
这段代码的功能是：
    获取当前目录下的所有文件并打印文件名。
    提示用户输入待处理的数据文本名。
    读取数据文本中的有效数据，并打印所有列的数据。
    按照第一列的数值进行递增排序，并打印第一列及其对应的倒数第二列数据。
    计算每一行中第一列和倒数第二列乘积的求和，并打印结果。
这段代码主要实现了文件操作、数据处理和统计计算的功能。

"""

import os

# 获取当前目录
current_directory = os.getcwd()

# 打印同级目录下的所有文件
print("同级目录下的文件：")
for file_name in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, file_name)):
        print(file_name)

# 提示用户输入待处理的数据文本名
data_file = input("请输入待处理的数据文本名：")

# 读取数据文本，忽略空行和#开头的行
data = []
with open(data_file, 'r') as file:
    for line in file:
        if line.startswith("#"):
            print("所有的#开头行：")
            print(line.strip())
        line = line.strip()
        if line != "" and not line.startswith("#"):
            data.append(line.split())

# 打印所有列的数据
print("所有列的数据：")
for row in data:
    print(row)

# 按照递增顺序打印第一列及其对应的倒数第二列数据
sorted_data = sorted(data, key=lambda x: float(x[0]))
print("按递增顺序打印第一列及其对应的倒数第二列数据：")
for row in sorted_data:
    print(row[0], row[-2])

# 计算每一行中的第一列和倒数第二列乘积的求和
sum_product = 0.0
for row in data:
    sum_product += float(row[0]) * float(row[-2])

# 打印求和结果
print("每一行中的第一列和倒数第二列乘积的求和（平均配位数）：", sum_product*0.01)   # 由于计算时使用的是百分数，这里要乘以0.01

