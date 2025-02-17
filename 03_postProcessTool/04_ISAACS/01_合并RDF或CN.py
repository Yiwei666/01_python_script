import os
import glob

# 获取当前目录下所有没有扩展名的文件，排除 Python 脚本
file_list = [file for file in glob.glob('*') if os.path.isfile(file) and not file.endswith('.py')]

# 创建一个字典，存储每个文件的列数据及其对应的文件名
data_dict = {}
column_names = []

# 读取每个文件并存储数据
for file in file_list:
    try:
        # 尝试使用 UTF-8 编码读取文件
        with open(file, 'r', encoding='utf-8') as f:
            data = [line.strip().split() for line in f if line.strip()]  # 去掉空行
    except UnicodeDecodeError:
        print(f"文件 {file} 使用 UTF-8 编码读取失败，尝试使用 gbk 编码重新读取。")
        # 如果 UTF-8 失败，尝试使用 gbk 编码读取
        with open(file, 'r', encoding='gbk') as f:
            data = [line.strip().split() for line in f if line.strip()]  # 去掉空行

    if not data:  # 如果文件是空的，跳过
        print(f"文件 {file} 是空的或没有有效数据，跳过。")
        continue

    # 检查每行是否有两列数据
    valid_data = [row for row in data if len(row) == 2]
    if not valid_data:
        print(f"文件 {file} 中没有有效的两列数据，跳过。")
        continue

    # 将数据按列添加到字典中
    col1 = [row[0] for row in valid_data]
    col2 = [row[1] for row in valid_data]
    data_dict[file] = (col1, col2)
    column_names.append(file)  # 保存文件名，对应后面打印列名

if not data_dict:
    print("没有有效的数据文件，退出。")
    exit()

# 写入到 total_data.txt 文件中
with open('total_data.txt', 'w', encoding='utf-8') as outfile:
    # 获取最大行数（因为每个文件可能行数不一样）
    max_rows = max(len(data_dict[file][0]) for file in data_dict)
    
    # 逐行写入数据，每一列的值来自不同文件
    for i in range(max_rows):
        row_data = []
        for file in data_dict:
            # 如果该文件行数不够，则补充空白数据
            if i < len(data_dict[file][0]):
                row_data.append(data_dict[file][0][i])
                row_data.append(data_dict[file][1][i])
            else:
                row_data.append('')
                row_data.append('')
        # 用空格分隔列并写入一行
        outfile.write(' '.join(row_data) + '\n')

# 打印并将每列对应的文件名写入到 log.txt 文件中
with open('log.txt', 'w', encoding='utf-8') as log_file:
    print("从左到右不同列对应的原始文件名:")
    log_file.write("从左到右不同列对应的原始文件名:\n")
    for file in data_dict:
        log_msg = f"{file}: 2 列\n"
        print(log_msg.strip())
        log_file.write(log_msg)
