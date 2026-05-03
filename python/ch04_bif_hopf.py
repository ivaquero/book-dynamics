import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

from .dynamics.bifurcations import hopf
from .dynamics.plotting import make_multi_traj_anim

x0 = [1, 0]
t_span = [0, 200]
t = np.arange(t_span[0], t_span[1], 0.01)

fig, ax = plt.subplots()


def compute_trajs_for_param(mu):
    sol = solve_ivp(hopf, t_span, x0, args=(mu,), dense_output=True)
    X = sol.sol(t).T
    return [X]


animate = make_multi_traj_anim(ax, compute_trajs_for_param)

anim = FuncAnimation(fig, animate, frames=np.arange(-1, 1, 0.1), interval=100)

plt.show()
