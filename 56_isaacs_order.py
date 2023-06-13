"""
上述代码实现了以下功能：
    首先，代码列出了同级目录下的所有文件，并将它们打印出来，以便用户知道可以选择哪个数据文本文件进行处理。
    然后，代码提示用户输入待处理的数据文本名，并读取该文本文件的内容。
    在读取文本文件时，代码会忽略空行和以 '#' 开头的行，以确保只处理有效的数据行。
    接下来，代码打印了所有列的数据。它将每一行分割成不同的列，并将每列的数据打印出来。
    最后，代码按照第一列数据的递增顺序对数据进行排序，并打印出第一列及其对应的倒数第二列的数据。它首先将数据解析成列，然后根据第一列的值进行排序，并将排序后的结果打印出来。
通过这些步骤，代码可以处理指定数据文本文件中的数据，并提供了打印所有列数据以及按照第一列排序的功能。

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
print("每一行中的第一列和倒数第二列乘积的求和（平均配位数）：", sum_product)

