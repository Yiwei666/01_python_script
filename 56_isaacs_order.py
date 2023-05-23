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

# 打印同级目录下的所有文件
files = os.listdir('.')
print("同级目录下的文件:")
for file in files:
    print(file)

# 提示用户输入待处理的数据文本名
filename = input("请输入待处理的数据文本名: ")

# 读取数据文本，忽略空行和以 '#' 开头的行
data = []
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith('#'):
            data.append(line)

# 打印所有列的数据
print("所有列的数据:")
for line in data:
    columns = line.split()
    print(columns)

# 按照递增的顺序打印第一列及其对应的倒数第二列数据
print("第一列及其对应的倒数第二列数据:")
sorted_data = sorted(data, key=lambda x: int(x.split()[0]))
for line in sorted_data:
    columns = line.split()
    print(columns[0], columns[-2])
