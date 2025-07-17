#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Multi‐trajectory DeepMD‑kit data preparation:
– 分别读取多个 CP2K AIMD 输出（tem.out）轨迹
– 随机抽取指定帧数作为验证集
– 按指定间隔抽取训练集
– 合并各轨迹的训练/验证子系统
– 保存为 DeepMD‑kit 支持的 npy 格式
"""

import os
import numpy as np
from dpdata import LabeledSystem, MultiSystems

# ----- 用户可配置参数 -----
trajectory_dirs = [
    r"C:\Users\sun78\Desktop\cp2k_model\80-1_B-slag_dpmd",
    r"C:\Users\sun78\Desktop\cp2k_model\80_B-slag\deepmd_aimd\non-equilib-initial-config\5000-steps"
]
cp2k_output_name = "tem.out"         # 每条轨迹的 CP2K 输出文件名
fmt = "cp2kdata/md"                  # dpdata 格式
validation_counts = [25, 35]         # 对应每条轨迹的验证集帧数
training_intervals = [6, 8]          # 对应每条轨迹的训练集抽帧间隔
random_seed = 42                     # 随机种子，保证可复现

training_out_dir = "./00.data/training_data"
validation_out_dir = "./00.data/validation_data"

# 检查参数长度一致性
assert len(trajectory_dirs) == len(validation_counts) == len(training_intervals), \
    "trajectory_dirs、validation_counts、training_intervals 三个列表长度必须相同"

# 创建输出目录
os.makedirs(training_out_dir, exist_ok=True)
os.makedirs(validation_out_dir, exist_ok=True)

# 初始化 MultiSystems 容器
ms_train = MultiSystems()
ms_validation = MultiSystems()

# 计数器，用于最终汇总
total_train_frames = 0
total_validation_frames = 0

# 固定随机种子
np.random.seed(random_seed)

for traj_dir, val_count, interval in zip(trajectory_dirs, validation_counts, training_intervals):
    # 1. 读取单条轨迹
    ls = LabeledSystem(traj_dir, cp2k_output_name=cp2k_output_name, fmt=fmt)
    total_frames = len(ls)
    print(f"# 轨迹目录: {traj_dir}")
    print(f"# 总帧数: {total_frames}")

    # 2. 随机抽取验证集索引
    val_idx = np.random.choice(total_frames, size=val_count, replace=False)
    val_idx_sorted = sorted(val_idx)
    print(f"# 验证集索引（共 {len(val_idx_sorted)} 帧）：{val_idx_sorted}")

    # 3. 剩余帧中按间隔抽取训练集索引
    remaining = sorted(set(range(total_frames)) - set(val_idx))
    train_idx = remaining[::interval]
    print(f"# 训练集索引（每隔 {interval} 帧，共 {len(train_idx)} 帧）：{train_idx}\n")

    # 累加计数
    total_validation_frames += len(val_idx)
    total_train_frames += len(train_idx)

    # 4. 拆分并添加到 MultiSystems
    ms_validation.append(ls.sub_system(val_idx))
    ms_train.append(ls.sub_system(train_idx))

# 5. 保存为 DeepMD‑kit npy 格式
ms_train.to_deepmd_npy(training_out_dir)
ms_validation.to_deepmd_npy(validation_out_dir)

# 6. 打印最终汇总
print(f"# 训练数据包含 {total_train_frames} 帧，已保存到 \"{training_out_dir}\"")
print(f"# 验证数据包含 {total_validation_frames} 帧，已保存到 \"{validation_out_dir}\"")
