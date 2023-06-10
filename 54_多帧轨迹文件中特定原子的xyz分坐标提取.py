import os

# 提示用户输入待处理数据文件名
filename = input("请输入待处理数据文件名（请输入每帧原子数都相同的标准xyz文件）：")

# 确定文件路径
filepath = os.path.join(os.getcwd(), filename)

# 如果文件存在，则继续处理
if os.path.isfile(filepath):
    # 读取文件内容
    with open(filepath, 'r') as file:
        data = file.readlines()

    # 提示用户输入系数q和列数n
    q = int(input("请输入等比系数q（一帧的总行数，即总原子数＋2，一般为3）："))
    n = int(input("请输入想要提取的列数n（列数从1开始计数）："))

    # 筛选出满足要求的行，并将第n列数据存入新文件中
    filtered_data = []
    count = 1
    for i in range(1, len(data)+1):
        if i % q == 0:
            row = data[i-1].strip().split()
            filtered_data.append([count, row[n-1]])
            count += 1

    # 提示用户输入新文件名
    new_filename = input("请输入新文件名（按Enter键默认为xyzDiag.txt）：")

    # 如果用户未输入新文件名，则使用默认文件名
    if new_filename == "":
        new_filename = "xyzDiag.txt"

    # 将数据保存到新文件中
    with open(new_filename, 'w') as file:
        for row in filtered_data:
            file.write(str(row[0]) + ' ' + str(row[1]) + '\n')
    print("保存格式为：第一列为帧数，第二列为 x or y or z 分坐标")
    print("已保存数据到文件：" + new_filename)                   # new_filename = "xyzDiag.txt"

else:
    print("文件不存在！")
