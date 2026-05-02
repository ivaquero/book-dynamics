import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import logistic_eq

x_inits = [1, 50, 200]
t_span = [0, 200]
t = np.linspace(t_span[0], t_span[1], 1000)

_, ax = plt.subplots()

for x_init in x_inits:
    sol = solve_ivp(logistic_eq, t_span, [x_init], dense_output=True)
    X = sol.sol(t).T
    ax.plot(t, X, label=f"X = {x_init}")

ax.legend()
ax.set(xlabel="Time", ylabel="X", title="The Logistics Equation")
