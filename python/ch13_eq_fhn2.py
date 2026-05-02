import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import FHN
from .ode.integrators import euler, euler_fixed

v, w, i_ext = euler(cond=[0, 4, 0.01])
fig, axes = plt.subplots(1, 2, constrained_layout=1)
ts = np.arange(0, 4, 0.01)


def run_fhn(start_puls, stop_puls, recover_puls):
    def f(t, z):
        i_ext = recover_puls if start_puls <= t <= stop_puls else 0
        return FHN(t, z, I_ext=i_ext)

    step = ts[1] - ts[0]
    traj, times = euler_fixed(f, [0, 0], step, len(ts))
    v = traj[:, 0]
    w = traj[:, 1]
    i_ext = [recover_puls if start_puls <= tt <= stop_puls else 0 for tt in times]
    return v, w, i_ext


v, w, i_ext = run_fhn(0, 4, 0.01)
axes[0].set(xlim=(0, 4), ylim=(-0.35, 1), title="constant $I_{ext} = 0.01$")
axes[0].plot(ts, v, label="neuron")
axes[0].plot(ts, i_ext, label="flow", color="r")
axes[0].legend()

v_, w_, i_ext_ = run_fhn(0, 4, 0.2)
axes[1].set(xlim=(0, 4), ylim=(-0.35, 1), title="constant $I_{ext} = 0.2$")
axes[1].plot(ts, v_, label="neuron")
axes[1].plot(ts, i_ext_, label="flow", color="r")
axes[1].legend()

plt.show()
