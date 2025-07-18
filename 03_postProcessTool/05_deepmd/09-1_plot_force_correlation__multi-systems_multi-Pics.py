#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Batch force-correlation plotting for all training systems under ../00.data/training_data/.

This script will:
1. Discover each first-level subdirectory under ../00.data/training_data/
2. For each system, load the DeepMD npy data and run a prediction with the trained graph.pb
3. Generate x/y/z force-correlation scatter plots and save them as PNGs named
   force_<component>_scatter_<system>.png
"""

import os
import dpdata
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- User-configurable paths ---
base_dir   = "../00.data/training_data"
model_path = "../01.train/graph.pb"

# List all first-level system directories
systems = sorted([
    d for d in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, d))
])

# Force components
components = ["x", "y", "z"]

for system in systems:
    system_path = os.path.join(base_dir, system)
    print(f"Processing system: {system_path}")

    # Load reference data and run prediction
    training_system = dpdata.LabeledSystem(system_path, fmt="deepmd/npy")
    predict        = training_system.predict(model_path)

    # Extract force tensors: shape (n_frames, n_atoms, 3)
    ref_forces  = training_system["forces"]
    pred_forces = predict["forces"]

    # For each Cartesian component, plot correlation
    for i, comp in enumerate(components):
        # Flatten to 1D arrays
        ref  = ref_forces[:, :, i].ravel()
        pred = pred_forces[:, :, i].ravel()

        plt.figure()
        plt.scatter(ref, pred, s=1, alpha=0.5)

        # y = x reference line
        lo = min(ref.min(), pred.min())
        hi = max(ref.max(), pred.max())
        plt.plot([lo, hi], [lo, hi], "r--", linewidth=0.25)

        # Labels and title
        plt.xlabel(f"DFT Force ({comp}) (eV/Å)")
        plt.ylabel(f"Predicted Force ({comp}) (eV/Å)")
        plt.title(f"Force correlation: {comp}-component ({system})")

        plt.tight_layout()
        out_fname = f"force_{comp}_scatter_{system}.png"
        plt.savefig(out_fname, dpi=300)
        plt.close()

    print(f"  → Saved plots for {system}\n")
