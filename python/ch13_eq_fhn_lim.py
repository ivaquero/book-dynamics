import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import fhn_lim_derivatives

θ, ω, γ, ϵ = 0.14, 0.112, 2.54, 0.01


x0 = [0.5, 0.09]
t_span = [0, 100]
sol = solve_ivp(fhn_lim_derivatives, t_span, x0, dense_output=True)
t = np.linspace(t_span[0], t_span[1], 1000)
X = sol.sol(t).T

_, ax = plt.subplots()

ax.plot(X[:, 0], X[:, 1], "r-")
ax.set(xlabel="u", ylabel="v")

ax.set(xlim=(-0.5, 1.5), ylim=(0, 0.3))
x = np.arange(-0.5, 1.5, 0.01)
ax.plot(x, x / γ, "b--", x, -x * (x - θ) * (x - 1) + ω, "b--")

plt.show()
