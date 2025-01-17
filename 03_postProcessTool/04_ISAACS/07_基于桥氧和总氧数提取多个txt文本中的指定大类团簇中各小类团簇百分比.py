import os
import pandas as pd
import re

def convert_key_format(key):
    """
    根据给定的规则转换键的格式。
    """
    # 提取键中元素及其数量
    pattern = r"([A-Za-z]+)(\d*)"
    elements = re.findall(pattern, key)

    # 初始化 a, b, c, d 为 0
    a, b, c, d = 0, 0, 0, 0

    for elem, count in elements:
        count = int(count) if count else 1  # 如果数量为空，则默认数量为1
        if elem == 'Si':
            a = count
        elif elem == 'Al':
            b = count
        elif elem == 'B':
            c = count
        elif elem == 'O':
            d = count

    # 计算 x = d - a - b - c
    x = d - a - b - c

    # 开始拼接结果字符串
    result = "B"

    # 如果 x 不为0和1，添加 "O\-(x)"
    if x > 1:
        result += f"O\\-({x})"
    elif x == 1:
        result += "O"

    # 如果 c 不为0和1，添加 "(BO\-(3))\-(c)"
    if c > 1:
        result += f"(BO\\-(3))\\-({c})"
    elif c == 1:
        result += "(BO\\-(3))"

    # 如果 b 不为0和1，添加 "(AlO\-(4))\-(b)"
    if b > 1:
        result += f"(AlO\\-(4))\\-({b})"
    elif b == 1:
        result += "(AlO\\-(4))"

    # 如果 a 不为0和1，添加 "(SiO\-(4))\-(a)"
    if a > 1:
        result += f"(SiO\\-(4))\\-({a})"
    elif a == 1:
        result += "(SiO\\-(4))"

    return result

def read_data_from_txt(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = []
        for line in f:
            if '%' in line:  # 只读取包含%符号的行
                columns = line.strip().split()
                if len(data) > 0 and len(columns) != len(data[0]):
                    print(f"列数不一致，文件：{file}")
                    return None
                data.append(columns)
        return data

def process_data(data):
    data_dict = {}
    for row in data:
        key = row[-1]  # 最后一列为键
        if key in data_dict:
            print(f"键值重复，键: {key}")
            return None
        data_dict[key] = [row[-7], row[-2], row[-4]]  # 获取倒数第7, 倒数第2, 倒数第4列
    return data_dict

def main():
    directory = '.'  # 当前目录
    files = [file for file in os.listdir(directory) if file.endswith('.txt')]
    
    # 存储每个文件的字典
    all_data_dicts = {}
    all_keys = set()

    for file in files:
        data = read_data_from_txt(file)
        if data is None:
            print(f"读取文件 {file} 失败，程序终止。")
            return

        data_dict = process_data(data)
        if data_dict is None:
            print(f"处理文件 {file} 失败，程序终止。")
            return

        all_data_dicts[file] = data_dict
        all_keys.update(data_dict.keys())

    # 提示用户输入两个整数 BO 和 TO
    try:
        TO = input("请输入整数 TO: ")
        BO = input("请输入整数 BO: ")
    except ValueError:
        print("输入无效，请输入整数。")
        return

    # 构建结果表格
    results = {key: [] for key in all_keys}
    for key in all_keys:
        for file in files:
            data_dict = all_data_dicts.get(file, {})
            if key in data_dict and data_dict[key][0] == TO and data_dict[key][1] == BO:
                results[key].append(data_dict[key][2])
            else:
                results[key].append(0)  # 没有满足条件的情况用0代替

    # 移除所有值均为0的键
    filtered_results = {key: val for key, val in results.items() if any(x != 0 for x in val)}

    if not filtered_results:
        print("没有满足条件的键值，结果为空。")
        return

    # 将结果保存为xlsx文件
    result_df = pd.DataFrame(filtered_results, index=files).transpose()
    result_df.columns = [f'文本{i+1}' for i in range(len(files))]  # 设置列名
    
    # 转置数据
    transposed_result_df = result_df.transpose()

    # 新增一行转换后的键
    converted_keys = {key: convert_key_format(key) for key in filtered_results.keys()}
    converted_keys_row = pd.DataFrame([converted_keys], index=["转换后的键"])
    transposed_result_df = pd.concat([transposed_result_df, converted_keys_row])

    # 保存结果到Excel文件中
    result_filename = f"{TO}-{BO}.xlsx"
    with pd.ExcelWriter(result_filename, engine='openpyxl') as writer:
        result_df.to_excel(writer, sheet_name='原始数据')  # 写入原始数据
        transposed_result_df.to_excel(writer, sheet_name='转置数据')  # 写入转置后的数据

    # 打印表格格式结果
    print(result_df)

if __name__ == '__main__':
    main()
