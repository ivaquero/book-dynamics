import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from .dynamics.attractors import mckey_glass
from .ode.integrators import euler_delay

ts = np.arange(0, 10, 0.01)
τ = 0.2
n_list = np.arange(1, 10, 1)
L, Vmax = 6, 16


# thin wrapper removed; use `euler_delay` directly in `animate`


fig, ax = plt.subplots()


def animate(i):
    ax.clear()
    ax.set(xlim=(0, 10), ylim=(0, 4), xlabel="time", title=f"n={n_list[i]}")

    def func(X, X_tau):
        return mckey_glass(X, X_tau, n_list[i])

    X = euler_delay(func, 2, 0.01, len(ts), τ, history_value=0.5)
    ax.plot(ts, X)


anim = FuncAnimation(fig, animate, frames=len(n_list), interval=200)
plt.show()
