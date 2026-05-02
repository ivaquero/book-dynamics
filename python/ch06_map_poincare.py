import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import poincare_derivatives

t_span = [0, 16 * np.pi]
z = [1, 0]
sol = solve_ivp(poincare_derivatives, t_span, z, dense_output=True)

t = np.linspace(t_span[0], t_span[1], 10000)
X = sol.sol(t).T

_, ax = plt.subplots()

ax.plot(X[:, 0], X[:, 1], "r-")
ax.set(xlabel="x", ylabel="y", xlim=(-0.5, 1.5), ylim=(-0.5, 0.5))

plt.show()
