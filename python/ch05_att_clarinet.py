import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

from .dynamics.attractors import clarinet
from .dynamics.plotting import make_multi_traj_anim

θs = np.linspace(0, 2 * np.pi, 5)
coordinates = []

for θ in θs:
    coordinates.extend(
        ([1.5 * np.cos(θ), 1.5 * np.sin(θ)], [0.05 * np.cos(θ), 0.05 * np.sin(θ)])
    )

a_list = np.arange(0.1, 2, 0.1)[::-1]
fig, ax = plt.subplots()
t_span = [0, 10]
t = np.linspace(t_span[0], t_span[1], 100)


def compute_trajs_for_param(a):
    trajs = []
    for coordinate in coordinates:
        x_i = coordinate[0]
        y_i = coordinate[1]
        sol = solve_ivp(clarinet, t_span, [x_i, y_i], args=(a,), dense_output=True)
        X = sol.sol(t).T
        trajs.append(X)
    return trajs


animate = make_multi_traj_anim(
    ax, compute_trajs_for_param, xlim=(-2, 2), ylim=(-1, 1), xlabel="x", ylabel="y"
)

anim = FuncAnimation(fig, animate, frames=a_list, interval=100)

plt.show()
