import os

def list_files_in_directory():
    """列出当前目录下的所有文件"""
    files = [f for f in os.listdir() if os.path.isfile(f)]
    for file in files:
        print(file)
    return files

def read_and_process_data(filename, col1, col2):
    """
    读取文件，忽略前三行，并处理数据。
    用户指定需要提取的列（从1开始计数，或使用负值代表倒数列）。
    第一个指定的列转换为int，第二个指定的列转换为float，并根据第一个列进行排序。
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[3:]  # 跳过前三行

        # 将用户输入的列索引转换成 Python 的索引（从0开始，负数不变）
        # 例如用户输入 1 代表 Python 索引 0，输入 -1 代表 Python 索引 -1
        col1_index = col1 - 1 if col1 > 0 else col1
        col2_index = col2 - 1 if col2 > 0 else col2

        data = []
        for line in lines:
            columns = line.strip().split()
            # 确保列索引不超过当前行拆分后的长度
            if len(columns) > max(abs(col1_index), abs(col2_index)) - 1:
                # 转换类型：col1 -> int, col2 -> float
                first_value = int(columns[col1_index])
                second_value = float(columns[col2_index])
                data.append((first_value, second_value))

        # 按照用户指定的第一个列值（已转换为整数）的大小排序
        data_sorted = sorted(data, key=lambda x: x[0])
        return data_sorted

    except Exception as e:
        print(f"读取或处理文件时出错: {e}")
        return []

def main():
    """主函数，执行脚本的主要逻辑"""
    print("当前目录下的文件列表:")
    files = list_files_in_directory()

    # 用户输入要处理的文件名
    filename = input("请输入你想处理的文件名: ")
    if filename not in files:
        print("文件不存在，请重新运行脚本。")
        return

    # 用户输入要提取的两列，使用英文逗号分隔
    columns_input = input("请输入需要提取的2个列号(用英文逗号分隔)，正数从1开始计数，负数代表倒数列，如-1代表倒数第一列: ")
    try:
        col1_str, col2_str = columns_input.split(',')
        col1, col2 = int(col1_str.strip()), int(col2_str.strip())
    except ValueError:
        print("输入格式有误，请重新运行脚本并按要求输入。")
        return

    # 调用处理函数
    result = read_and_process_data(filename, col1, col2)

    # 输出结果
    for item in result:
        print(f"{item[0]} {item[1]}")

if __name__ == "__main__":
    main()
