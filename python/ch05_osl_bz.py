import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import bz_reaction

q, f, ϵ, δ = 3.1746e-5, 1, 0.0099, 2.4802e-5
xyz_init = [0, 0, 0.1]
t_span = [0, 50]

sol = solve_ivp(bz_reaction, t_span, xyz_init, args=((q, f, ϵ, δ)), dense_output=True)

t = np.linspace(t_span[0], t_span[1], 10000)
sols = sol.sol(t)

_, axes = plt.subplots(1, 3, constrained_layout=1)

labels = ["$HBrO_2$", "$Br^-$", "$Ce^{4+}$"]
linestyles = ["b-", "r-", "m-"]

for ax, sol, label, linestyle in zip(
    axes.flatten(), sols, labels, linestyles, strict=True
):
    ax.set(ylabel=f"relative concentration of {label}")
    ax.plot(t, sol, linestyle)

plt.show()
