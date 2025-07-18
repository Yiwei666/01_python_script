#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Energy and force correlation plotting for all training systems in one figure.

This script will:
1. Discover all first‐level subdirectories under "../00.data/training_data/".
2. For each system, load the deepmd/npy data and predict energies using the trained graph.
3. Plot DFT vs. predicted energies for all systems in a single scatter plot.
4. Draw the y = x reference line.
5. Save the figure as "energy_scatter_all_systems.png".
"""

import os
import dpdata
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Base directory containing subdirectories for each training system
base_dir = "../00.data/training_data"
# Path to the trained deep potential graph
model_path = "../01.train/graph.pb"

# Find all first‐level subdirectories under base_dir
systems = [
    name for name in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, name))
]

# Plot each system’s energy correlation
for sys_name in systems:
    sys_path = os.path.join(base_dir, sys_name)
    # Load system
    ts = dpdata.LabeledSystem(sys_path, fmt="deepmd/npy")
    # Predict energies
    pred = ts.predict(model_path)
    # Scatter plot: true vs. predicted
    plt.scatter(
        ts["energies"],
        pred["energies"],
        label=sys_name,
        s=10,
        alpha=0.7
    )

# Reference line y = x
x_min, x_max = plt.xlim()
x_range = np.linspace(x_min, x_max, 100)
plt.plot(x_range, x_range, "r--", linewidth=0.25)

# Labels and legend
plt.xlabel("Energy of DFT")
plt.ylabel("Energy predicted by deep potential")
plt.legend(title="System", fontsize="small", loc="best")

plt.tight_layout()
plt.savefig("energy_scatter_all_systems.png", dpi=300)
