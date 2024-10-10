import os

def process_file(file_name):
    # 创建新文件名
    new_file_name = "origin_" + file_name
    
    # 读取原文件，删除以@开头的行，并保存到新文件
    with open(file_name, 'r', encoding='utf-8') as file:
        with open(new_file_name, 'w', encoding='utf-8') as new_file:
            for line in file:
                if not line.startswith('@'):
                    new_file.write(line)
    
    print(f"已处理文件：{file_name}，新文件保存为: {new_file_name}")

def main():
    # 获取当前目录下的所有文件
    files = os.listdir('.')
    print("正在检查目录下的文件...")
    
    # 筛选没有文件后缀的文件
    files_to_process = [file for file in files if os.path.isfile(file) and '.' not in file]

    # 如果没有找到符合条件的文件
    if not files_to_process:
        print("没有找到没有文件后缀的文件。")
        return

    # 处理每一个符合条件的文件
    for file_name in files_to_process:
        process_file(file_name)

if __name__ == "__main__":
    main()
