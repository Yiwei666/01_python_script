#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Force correlation plotting for all training systems under ../00.data/training_data/.

This script will:
1. Discover all first‑level subdirectories in ../00.data/training_data/
2. For each system:
   - Load the reference forces from the DeepMD‑kit npy data
   - Predict forces using the trained graph.pb model
3. For each force component (x, y, z):
   - Scatter‑plot reference vs. predicted forces for *all* systems on a single figure
   - Draw the y = x guide line
   - Add a legend to distinguish the different systems
   - Save the figure as force_<comp>_scatter_all.png
"""

import os
import dpdata
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# --- User‑configurable parameters ---
DATA_ROOT   = "../00.data/training_data"
MODEL_PATH  = "../01.train/graph.pb"
COMPONENTS  = ["x", "y", "z"]
OUT_PATTERN = "force_{comp}_scatter_all.png"
# --------------------------------------

# 1. Find all first‑level subdirectories (each corresponds to one system)
systems = [
    d for d in os.listdir(DATA_ROOT)
    if os.path.isdir(os.path.join(DATA_ROOT, d))
]
if not systems:
    raise RuntimeError(f"No subdirectories found under {DATA_ROOT}")

# 2. Collect reference and predicted forces for each system
#    Structure: data[comp][system] = (ref_array, pred_array)
data = {comp: {} for comp in COMPONENTS}

for sys_name in systems:
    sys_path = os.path.join(DATA_ROOT, sys_name)
    print(f"Processing system: {sys_name}")
    # Load reference dataset
    ds_ref = dpdata.LabeledSystem(sys_path, fmt="deepmd/npy")
    # Run prediction
    ds_pred = ds_ref.predict(MODEL_PATH)

    # Extract force arrays (shape: n_frames × n_atoms × 3)
    ref_forces  = ds_ref["forces"]
    pred_forces = ds_pred["forces"]

    # Flatten each component and store
    for idx, comp in enumerate(COMPONENTS):
        ref_flat  = ref_forces[:, :, idx].ravel()
        pred_flat = pred_forces[:, :, idx].ravel()
        data[comp][sys_name] = (ref_flat, pred_flat)

# 3. Plot combined scatter for each component
for comp in COMPONENTS:
    plt.figure(figsize=(6,6))
    for sys_name, (ref_vals, pred_vals) in data[comp].items():
        plt.scatter(
            ref_vals, pred_vals,
            s=1, alpha=0.5,
            label=sys_name
        )

    # Determine global min and max for the y=x line
    all_mins = [min(r.min(), p.min()) for r, p in data[comp].values()]
    all_maxs = [max(r.max(), p.max()) for r, p in data[comp].values()]
    lo = min(all_mins)
    hi = max(all_maxs)
    plt.plot([lo, hi], [lo, hi], "r--", linewidth=0.25)

    # Labels and title
    plt.xlabel(f"DFT Force ({comp}) (eV/Å)")
    plt.ylabel(f"Predicted Force ({comp}) (eV/Å)")
    plt.title(f"Force Correlation: {comp}-component")

    # Legend
    plt.legend(
        title="System",
        markerscale=5,
        fontsize="small",
        title_fontsize="small",
        loc="best"
    )

    plt.tight_layout()
    out_file = OUT_PATTERN.format(comp=comp)
    plt.savefig(out_file, dpi=300)
    plt.close()
    print(f"Saved plot: {out_file}")
