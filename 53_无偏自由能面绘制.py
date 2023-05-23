# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:07:04 2023

@author: sun78
"""

import numpy as np
import matplotlib.pyplot as plt

bohr_2_angstrom = 0.529177
kb = 8.6173303e-5 # eV * K^-1
conversion_factor = 96.4853 # KJ/mol per 1 eV

temperature = 1823                          #Change temperature according to your MD simulations!
colvar_path = "./SiTiB-COLVAR.metadynLog"

# Load the colvar file
colvar_raw = np.loadtxt(colvar_path)

# Extract the two CVs
# d1 = colvar_raw[:, 1] * bohr_2_angstrom
# d2 = colvar_raw[:, 2] * bohr_2_angstrom

# Extract the two CVs
d1 = colvar_raw[:, 1] 
d2 = colvar_raw[:, 2]

# Create a 2d histogram corresponding to the CV occurances
cv_hist = np.histogram2d(d1, d2, bins=10)

print("Bin edges for d1:", cv_hist[1])
print("Bin edges for d2:", cv_hist[2])
print("Histogram of frequencies:")
print(cv_hist[0])


# probability from the histogram
prob = cv_hist[0]/len(d1)

# Free energy surface
fes = -kb * temperature * np.log(prob)

# Convert the energy unit to kJ/mol
fes_kjmol = fes * conversion_factor

# Save the image
extent = (np.min(cv_hist[1]), np.max(cv_hist[1]), np.min(cv_hist[2]), np.max(cv_hist[2]))
# extent = (0, 8, 0, 8)
plt.figure(figsize=(8, 8))
plt.imshow(fes_kjmol.T, extent=extent, aspect='auto', origin='lower', cmap='hsv')
cbar = plt.colorbar()
cbar.set_label("Free energy [kJ/mol]")
plt.xlabel("d1 [ang] Ti-Si")
plt.ylabel("d2 [ang] Ti-B ")

# plt.savefig("./fes.png", dpi=200)
# plt.close()
plt.show()