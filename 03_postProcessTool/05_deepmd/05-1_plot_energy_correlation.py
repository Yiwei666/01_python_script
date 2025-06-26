import matplotlib

matplotlib.use('Agg')

import dpdata
import matplotlib.pyplot as plt
import numpy as np


training_systems = dpdata.LabeledSystem(
    "../00.data/training_data",
    fmt="deepmd/npy"
)
predict = training_systems.predict(
    "../01.train/graph.pb"
)


plt.scatter(training_systems["energies"], predict["energies"])
x_range = np.linspace(plt.xlim()[0], plt.xlim()[1])
plt.plot(x_range, x_range, "r--", linewidth=0.25)
plt.xlabel("Energy of DFT")
plt.ylabel("Energy predicted by deep potential")


plt.tight_layout()
plt.savefig("energy_scatter.png", dpi=300)
