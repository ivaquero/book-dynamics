import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import SIR

t_span = [0, 50]
t = np.linspace(t_span[0], t_span[1], 5000)

_, axes = plt.subplots(1, 3, constrained_layout=1)

sir_inits = [[9999, 1, 0], [9900, 100, 0], [5000, 5000, 0]]

for i, sir_init in enumerate(sir_inits):
    sol = solve_ivp(SIR, t_span, sir_init, dense_output=True)
    X = sol.sol(t).T
    S, II, R = X[:, 0], X[:, 1], X[:, 2]
    axes[i].plot(t, S, label="S")
    axes[i].plot(t, II, label="I")
    axes[i].plot(t, R, label="R")
    axes[i].set(
        xlabel="Time (days)",
        title=f"{sir_init[0]} susceptible and {sir_init[1]} infected",
    )
    axes[i].legend(loc="right")

axes[0].set(ylabel="Number of People")
plt.show()
