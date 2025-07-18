#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Multi‐trajectory DeepMD-kit data preparation:
– 支持多种 dpdata.LabeledSystem 读取方式
– 分别随机抽取指定帧数作为验证集
– 按指定间隔抽取训练集
– 合并各轨迹的训练/验证子系统
– 保存为 DeepMD-kit 支持的 npy 格式
"""

import os
import numpy as np
from dpdata import LabeledSystem, MultiSystems

# ----- 用户可配置参数 -----
trajectory_configs = [
    # 普通 CP2K 输出轨迹
    {
        "traj_dir": r"C:\Users\sun78\Desktop\cp2k_model\80-1_B-slag_dpmd",
        "cp2k_output_name": "tem.out",
        "fmt": "cp2kdata/md",
        "val_count": 100,
        "interval": 10,
    },
    {
        "traj_dir": r"C:\Users\sun78\Desktop\cp2k_model\80_B-slag\deepmd_aimd\non-equilib-initial-config\5000-steps",
        "cp2k_output_name": "tem.out",
        "fmt": "cp2kdata/md",
        "val_count": 100,
        "interval": 10,
    },
    # 需要指定 cell 矩阵和 ensemble_type
    {
        "traj_dir": r"C:\Users\sun78\Desktop\cp2k_model\63_SiB\dpdata-temp",
        "cp2k_output_name": None,
        "cells": np.array([[9.34477, 0, 0],
                           [0, 9.34477, 0],
                           [0, 0, 9.34477]]),
        "ensemble_type": "NVT",
        "fmt": "cp2kdata/md",
        "val_count": 100,
        "interval": 10,
    },
    {
        "traj_dir": r"C:\Users\sun78\Desktop\cp2k_model\64_B2O3\dpdata-temp",
        "cp2k_output_name": None,
        "cells": np.array([[9.402, 0, 0],
                           [0, 9.402, 0],
                           [0, 0, 9.402]]),
        "ensemble_type": "NVT",
        "fmt": "cp2kdata/md",
        "val_count": 100,
        "interval": 10,
    }
]

random_seed = 42
training_out_dir = "./00.data/training_data"
validation_out_dir = "./00.data/validation_data"

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

for config in trajectory_configs:
    traj_dir   = config["traj_dir"]
    val_count  = config["val_count"]
    interval   = config["interval"]

    # 动态构造 LabeledSystem 所需的可选参数
    ls_kwargs = {}
    for key in ("cp2k_output_name", "cells", "ensemble_type", "fmt"):
        if key in config:
            ls_kwargs[key] = config[key]

    # 1. 读取单条轨迹
    ls = LabeledSystem(traj_dir, **ls_kwargs)
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
    total_train_frames      += len(train_idx)

    # 4. 拆分并添加到 MultiSystems
    ms_validation.append(ls.sub_system(val_idx))
    ms_train.append(ls.sub_system(train_idx))

# 5. 保存为 DeepMD-kit npy 格式
ms_train.to_deepmd_npy(training_out_dir)
ms_validation.to_deepmd_npy(validation_out_dir)

# 6. 打印最终汇总
print(f"# 训练数据包含 {total_train_frames} 帧，已保存到 \"{training_out_dir}\"")
print(f"# 验证数据包含 {total_validation_frames} 帧，已保存到 \"{validation_out_dir}\"")
