#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动对每个训练体系绘制 DFT 能量 vs. Deep Potential 预测能量的散点图
并保存到当前目录，文件名格式：energy_scatter_<体系名>.png
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import dpdata

# 基础目录和模型路径
BASE_DIR   = "../00.data/training_data"
MODEL_PATH = "../01.train/graph.pb"

# 遍历所有一级子文件夹
for name in sorted(os.listdir(BASE_DIR)):
    sys_path = os.path.join(BASE_DIR, name)
    if not os.path.isdir(sys_path):
        continue

    print(f"Processing system: {name}")

    # 读取体系并预测
    ds = dpdata.LabeledSystem(sys_path, fmt="deepmd/npy")
    pred = ds.predict(MODEL_PATH)

    # 绘图
    fig, ax = plt.subplots()
    ax.scatter(ds["energies"], pred["energies"], s=5)
    x_min, x_max = ax.get_xlim()
    x_line = np.linspace(x_min, x_max, 100)
    ax.plot(x_line, x_line, "r--", linewidth=0.25)

    ax.set_xlabel("Energy of DFT")
    ax.set_ylabel("Energy predicted by deep potential")
    ax.set_title(f"Energy Correlation: {name}")

    plt.tight_layout()
    outfig = f"energy_scatter_{name}.png"
    plt.savefig(outfig, dpi=300)
    plt.close(fig)

print("All systems processed.")
