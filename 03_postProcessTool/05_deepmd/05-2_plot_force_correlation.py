import matplotlib
matplotlib.use('Agg')

import dpdata
import matplotlib.pyplot as plt
import numpy as np

# 1. 读取数据
training_systems = dpdata.LabeledSystem(
    "../00.data/training_data",
    fmt="deepmd/npy"
)
predict = training_systems.predict(
    "../01.train/graph.pb"
)

# 2. 拿到参考和预测的力张量，形状 (n_frames, n_atoms, 3)
ref_forces = training_systems["forces"]
pred_forces = predict["forces"]

# 3. 对每个分量循环：0->x, 1->y, 2->z
components = ["x", "y", "z"]
for i, comp in enumerate(components):
    # 展平成一维数组
    ref = ref_forces[:, :, i].ravel()
    pred = pred_forces[:, :, i].ravel()

    # 新开一个 figure
    plt.figure()
    plt.scatter(ref, pred, s=1, alpha=0.5)
    
    # 画 y=x 参考线
    lo = min(ref.min(), pred.min())
    hi = max(ref.max(), pred.max())
    plt.plot([lo, hi], [lo, hi], "r--", linewidth=0.25)

    # 标签与单位
    plt.xlabel(f"DFT Force ({comp}) (eV/Å)")
    plt.ylabel(f"Predicted Force ({comp}) (eV/Å)")
    plt.title(f"Force correlation: {comp}-component")

    # 紧凑布局、保存
    plt.tight_layout()
    plt.savefig(f"force_{comp}_scatter.png", dpi=300)
    plt.close()
  
