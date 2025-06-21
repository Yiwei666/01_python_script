#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def is_convertible_line(line):
    """
    判断一行是否符合需要转换的格式：
    - 列数为4
    - 第一列无法转换为数值（视为字符串）
    - 后三列能够转换为浮点数
    """
    parts = line.split()
    if len(parts) != 4:
        return False
    # 检查第一列不是数值
    try:
        float(parts[0])
        return False
    except ValueError:
        pass

    # 检查后三列都能转换为浮点数
    try:
        float(parts[1])
        float(parts[2])
        float(parts[3])
        return True
    except ValueError:
        return False

def main():
    # 系数：将 amu·Å/fs² 转换为 Hartree/Bohr
    COEF = 2.015529557777

    # 列出当前目录下所有文件（不包含子目录中的文件）
    all_files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print("当前目录下的文件：")
    for fname in all_files:
        print(f"  {fname}")

    # 提示用户输入需要读取的文件名
    filename = input("\n请输入需要读取的文件名（例如 *.frc.xyz）：").strip()
    if not os.path.isfile(filename):
        print(f"错误：未找到文件 '{filename}'。请确保文件名正确。")
        sys.exit(1)

    # 读取所有行
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 进行一致性检验前的统计
    count_time = 0     # a：文档中“time”出现的总次数
    count_nonempty = 0 # b：非空行总数
    count_convert = 0  # c：需要进行数值转换的行数

    for line in lines:
        # 统计“time”出现的次数
        count_time += line.count("time")
        # 统计非空行
        if line.strip():
            count_nonempty += 1
        # 判断是否需要转换
        if is_convertible_line(line):
            count_convert += 1

    # 一致性检验：2*a + c == b
    a = count_time
    b = count_nonempty
    c = count_convert
    if 2 * a + c != b:
        print("一致性检验未通过：")
        print(f"  count_time (a) = {a}")
        print(f"  count_nonempty (b) = {b}")
        print(f"  count_convert (c) = {c}")
        print("请检查文件内容，程序已退出。")
        sys.exit(1)

    # 如果通过检验，则开始数值转换
    output_lines = []
    for line in lines:
        if is_convertible_line(line):
            parts = line.split()
            atom_label = parts[0]
            # 将后三列转换为浮点数并乘以系数
            x = float(parts[1]) * COEF
            y = float(parts[2]) * COEF
            z = float(parts[3]) * COEF
            # 格式化为小数点后10位
            new_line = f"{atom_label} {x:.10f} {y:.10f} {z:.10f}\n"
            output_lines.append(new_line)
        else:
            # 保留原行（包括换行符）
            output_lines.append(line)

    # 保存到新文件
    new_filename = "Hartree-Bohr_" + filename
    with open(new_filename, 'w', encoding='utf-8') as fout:
        fout.writelines(output_lines)

    print(f"转换完成，已保存为 '{new_filename}'。")

if __name__ == "__main__":
    main()
