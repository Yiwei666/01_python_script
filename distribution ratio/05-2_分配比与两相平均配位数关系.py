# L_X vs CN_average^{X-O} curve and data export
# Assumption: impurity X is B → M_X = 10.81; change if needed.

import numpy as np
import matplotlib.pyplot as plt

# ---------- Parameters ----------

#######################
# 需要修改的参数
y = 4                 # stable valence of impurity in slag
CN_silicate_XO = 4.71 # average CN in silicate
M_X    = 47.87       # atomic mass of impurity X (B)
CN_avg = np.arange(0.0, 10.05 + 0.05, 0.05)  # 0..10 step 0.05


################################################################
N_X = 8               # initial impurity atoms (B) in Si phase
N_Si = 42             # initial Si atoms in Si phase
N_SiO2 = 40           # moles of SiO2
N_CaO = 43            # moles of CaO

M_SiO2 = 60.0843      # molar mass of SiO2
M_CaO  = 56.0774      # molar mass of CaO
M_Si   = 28.0855      # atomic mass of Si


# ---------- CN range ----------


# ---------- Compute E_X and L_X ----------
E_X = (CN_avg / CN_silicate_XO) * N_X

numer_mass = (N_Si + (y/4.0)*E_X) * M_Si + (N_X - E_X) * M_X
denom_mass = N_SiO2*M_SiO2 + N_CaO*M_CaO - (y/4.0)*E_X*M_Si + E_X*M_X

with np.errstate(divide='ignore', invalid='ignore'):
    L_X = (E_X / (N_X - E_X)) * (numer_mass / denom_mass)

# valid physical/defined points (avoid E_X >= N_X and nonpositive denominator)
valid = (E_X >= 0) & (E_X < N_X) & (denom_mass > 0) & np.isfinite(L_X)

# ---------- Save data ----------
data = np.column_stack([CN_avg[valid], L_X[valid]])
np.savetxt(
    "Lx_CN-ave.dat",
    data,
    header="CN_average_X-O    L_X",
    comments="",
    fmt="%.8f"
)

# ---------- Plot ----------
plt.figure(figsize=(7, 5))
plt.plot(CN_avg[valid], L_X[valid])
plt.xlabel(r"$CN_{\mathrm{average}}^{X-O}$")
plt.ylabel(r"$L_X$")
plt.title(r"$L_X$ vs $CN_{\mathrm{average}}^{X-O}$")
plt.grid(True)
plt.tight_layout()
plt.show()
