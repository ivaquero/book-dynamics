import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import SEIR

ρs = [1, 0.6, 0.4]
seir_inits = [[999999, 0, 1, 0], [999999, 0, 1, 0], [999999, 0, 1, 0]]
t_span = [0, 800]
t = np.linspace(t_span[0], t_span[1], 5000)

_, ax = plt.subplots()

for seir_init, ρ in zip(seir_inits, ρs, strict=True):
    sol = solve_ivp(SEIR, t_span, seir_init, args=(ρ,), dense_output=True)
    X = sol.sol(t).T
    S, i, E, R = X[:, 0], X[:, 1], X[:, 2], X[:, 3]

    ax.plot(t, i, label=f"ϱ = {ρ}")

ax.legend()
ax.set(
    xlabel="Time (days)",
    ylabel="Number",
    title="Number of Infection by Function of Time",
)

plt.show()
