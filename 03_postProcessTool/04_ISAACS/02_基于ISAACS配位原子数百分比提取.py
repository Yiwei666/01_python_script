import os

def list_files_in_directory():
    """列出当前目录下的所有文件"""
    files = [f for f in os.listdir() if os.path.isfile(f)]
    for file in files:
        print(file)
    return files

def read_and_process_data(filename):
    """读取文件，忽略前三行，并处理数据"""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[3:]  # 跳过前三行
        data = []
        for line in lines:
            columns = line.strip().split()
            if len(columns) >= 2:  # 确保有足够的列
                first_column = int(columns[0])  # 将第一列转换为整数
                second_last_column = float(columns[-2])  # 将倒数第二列转换为浮点数
                data.append((first_column, second_last_column))
        # 按第一列递增排序，数值排序
        data_sorted = sorted(data, key=lambda x: x[0])
        return data_sorted
    except Exception as e:
        print(f"读取或处理文件时出错: {e}")
        return []

def main():
    """主函数，执行脚本的主要逻辑"""
    print("当前目录下的文件列表:")
    files = list_files_in_directory()
    filename = input("请输入你想处理的文件名: ")
    if filename in files:
        result = read_and_process_data(filename)
        for item in result:
            print(f"{item[0]} {item[1]}")
    else:
        print("文件不存在，请重新运行脚本。")

if __name__ == "__main__":
    main()
