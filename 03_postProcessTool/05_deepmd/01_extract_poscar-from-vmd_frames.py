#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 VMD 导出的多帧 POSCAR 文件中提取指定帧，并各自保存为独立文件。

功能：
1. 列出当前目录内所有文件名，提示用户输入待处理的 POSCAR 文件。
2. 通过统计 'Direct' 或 'Cartesian' 关键字出现次数识别帧数，并校验各帧行数一致。
3. 支持两种帧索引输入方式：
   (a) 逗号分隔的具体索引，可用 "-" 指定连续区间，如 0,5,9-12
   (b) 类似 range(a,b,c) 的等步长抽取：输入 a,b,c（三个整数，用逗号分隔）
4. 提取前列出待写入的索引列表及数量，要求用户键入 'y' 确认。
5. 将每帧写入 `index_<索引>_POSCAR`，并把该帧 **第一行** 复制到第 6 行，
   使第 6 行成为元素符号行，满足常规 POSCAR 格式。

作者：ChatGPT（OpenAI o3）
"""

import os
import re
import sys
from typing import List, Tuple


def list_files() -> None:
    """打印当前目录下的所有文件（不含子目录）。"""
    print("当前目录文件：")
    for f in sorted(p for p in os.listdir() if os.path.isfile(p)):
        print("  ", f)
    print()


def ask_filename() -> str:
    """提示用户输入需要处理的 POSCAR 文件名。"""
    while True:
        name = input("请输入需要处理的 VMD 导出的 POSCAR 文件名： ").strip()
        if os.path.isfile(name):
            return name
        print(f"未找到文件 '{name}'，请重新输入。")


def read_frames(lines: List[str]) -> Tuple[int, int]:
    """
    返回 (frame_count, lines_per_frame)。
    若各帧行数不一致则抛出 ValueError。
    """
    key_pat = re.compile(r"^\s*(Direct|Cartesian)\b", re.I)
    key_lines = [i for i, line in enumerate(lines) if key_pat.match(line)]
    if not key_lines:
        raise ValueError("文件中未找到 'Direct' 或 'Cartesian' 关键字！")

    # 帧数即关键字出现次数
    frame_count = len(key_lines)

    # 计算行数间隔是否一致
    intervals = [j - i for i, j in zip(key_lines, key_lines[1:])]
    if intervals and any(x != intervals[0] for x in intervals):
        raise ValueError("检测到相邻两帧行数不一致，无法继续处理！")

    # 文件总行数必须能被帧数整除
    if len(lines) % frame_count != 0:
        raise ValueError("文件总行数无法整除帧数，可能存在异常行。")

    lines_per_frame = len(lines) // frame_count
    return frame_count, lines_per_frame


def parse_index_list(text: str, max_idx: int) -> List[int]:
    """解析形如 0,3,5-9 的索引串。"""
    idx_set = set()
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = map(int, part.split("-", 1))
            if a > b:
                a, b = b, a
            idx_set.update(range(a, b + 1))
        else:
            idx_set.add(int(part))
    if any(i < 0 or i >= max_idx for i in idx_set):
        raise ValueError("部分索引超出范围！")
    return sorted(idx_set)


def parse_range_input(text: str, max_idx: int) -> List[int]:
    """解析 a,b,c 三个整数，返回 list(range(a,b,c))。"""
    try:
        a, b, c = map(int, text.split(","))
    except Exception:
        raise ValueError("范围输入格式应为 a,b,c（整数，用逗号分隔）")
    if c == 0:
        raise ValueError("步长 c 不能为 0")
    idx_list = list(range(a, b, c))
    if not idx_list:
        raise ValueError("生成的索引列表为空，请检查 a,b,c")
    if any(i < 0 or i >= max_idx for i in idx_list):
        raise ValueError("部分索引超出范围！")
    return idx_list


def ask_indices(frame_count: int) -> List[int]:
    """与用户交互，获取待提取的帧索引列表。"""
    print(f"\n检测到文件共有 {frame_count} 帧。")
    while True:
        mode = input("选择索引输入方式：\n"
                     "  1) 逗号/区间混合 (如 0,3,10-15)\n"
                     "  2) range(a,b,c) 风格 (输入 a,b,c)\n"
                     "请输入 1 或 2： ").strip()
        try:
            if mode == "1":
                s = input("请输入索引列表： ").strip()
                indices = parse_index_list(s, frame_count)
            elif mode == "2":
                s = input("请输入 a,b,c： ").strip()
                indices = parse_range_input(s, frame_count)
            else:
                print("无效选项，请重新选择。")
                continue
        except ValueError as e:
            print(f"输入错误：{e}")
            continue

        print("\n将提取的帧索引：", indices)
        print("总计帧数：", len(indices))
        if input("确认请键入 y，然后回车： ").strip().lower() == "y":
            return indices
        print("已取消，重新输入。\n")


def insert_element_line(frame_lines: List[str]) -> List[str]:
    """复制第一行到第 6 行（索引 5）并返回新列表。"""
    new_lines = frame_lines[:]
    new_lines.insert(5, frame_lines[0])
    return new_lines


def write_frames(lines: List[str], lines_per_frame: int, indices: List[int]) -> None:
    """按索引写出各帧为独立 POSCAR 文件。"""
    for idx in indices:
        start = idx * lines_per_frame
        end = start + lines_per_frame
        frame = lines[start:end]
        frame_fixed = insert_element_line(frame)
        out_name = f"index_{idx}_POSCAR"
        with open(out_name, "w", encoding="utf-8") as fout:
            fout.writelines(frame_fixed)
        print(f"已写入 {out_name}")


def main() -> None:
    list_files()
    fname = ask_filename()

    with open(fname, encoding="utf-8") as f:
        lines = f.readlines()

    try:
        n_frames, lines_per_frame = read_frames(lines)
    except ValueError as e:
        print(f"错误：{e}")
        sys.exit(1)

    idx_list = ask_indices(n_frames)
    write_frames(lines, lines_per_frame, idx_list)

    print("\n全部完成！")


if __name__ == "__main__":
    main()
