#!/usr/bin/env python3
"""
多帧 XYZ 文件抽取脚本

功能：
1. 列出当前目录下全部文件并提示用户选择 XYZ 文件。
2. 确认第 i 帧行号范围公式：[(i-1)*(a+2)+1, i*(a+2)]（1 基），其中 a 为原子数。
3. 每 n 帧提取一帧（回车默认 n = 10），并报告提取数量 b。
4. 将结果写入 0-b_every_{n}th_frame.xyz 文件。
"""

import os

def main():
    # 1⃣  列出当前目录普通文件
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print("当前目录文件：")
    for i, f in enumerate(files, 1):
        print(f"{i:2d}. {f}")

    # 读取目标文件名
    while True:
        xyz_name = input("\n请输入待处理的 XYZ 文件名：").strip()
        if xyz_name and os.path.isfile(xyz_name):
            break
        print("❌ 文件不存在，请重新输入。")

    # 读取文件内容
    with open(xyz_name, "r") as fp:
        lines = fp.readlines()

    # 原子数 a 与每帧行数 frame_size = a + 2
    try:
        a = int(lines[0].strip())
    except ValueError:
        raise RuntimeError("文件第一行不是整数，无法解析原子数。")

    frame_size = a + 2
    total_frames = len(lines) // frame_size
    if len(lines) % frame_size:
        print("⚠️  警告：文件行数并非帧长度整数倍，可能存在残缺帧。")

    # 2⃣  验证行号范围公式（示例前 3 帧）
    print("\n✅ 行号范围验证（示例前 3 帧）：")
    for i in range(1, min(3, total_frames) + 1):
        start = (i - 1) * frame_size + 1  # 1-based
        end   = i * frame_size
        print(f"  第 {i:2d} 帧：[{start}, {end}]")

    # 3⃣  读取 n（默认 10）
    n_raw = input("\n每隔 n 帧取 1 帧，输入 n (Enter 默认 10)：").strip()
    n = int(n_raw) if n_raw else 10
    print(f"参数 n = {n}")

    frames_idx = list(range(n, total_frames + 1, n))
    b = len(frames_idx)
    print(f"将提取 {b} 帧：{frames_idx}")

    # 4⃣  写出新文件
    out_name = f"0-{b}_every_{n}th_frame.xyz"
    with open(out_name, "w") as out:
        for i in frames_idx:
            s = (i - 1) * frame_size
            e = s + frame_size
            out.writelines(lines[s:e])

    print(f"\n✅ 完成！已写入 {out_name}")

if __name__ == "__main__":
    main()

