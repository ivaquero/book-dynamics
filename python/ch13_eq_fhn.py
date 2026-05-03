import matplotlib.pyplot as plt
import numpy as np

from .dynamics.plotting import time_series_from_pulsed_factory
from .ode.integrators import euler_fixed

_, axes = plt.subplots(1, 2, constrained_layout=1)
ts = np.arange(0, 4, 0.01)


def run_fhn(start_puls, stop_puls, recover_puls):
    traj, times = time_series_from_pulsed_factory(
        start_puls, stop_puls, recover_puls, ts, [0, 0], integrator=euler_fixed
    )
    v = traj[:, 0]
    w = traj[:, 1]
    i_ext = [recover_puls if start_puls <= tt <= stop_puls else 0 for tt in times]
    return v, w, i_ext


v, w, i_ext = run_fhn(1, 1.20, 0.01)

axes[0].set(xlim=(0, 4), ylim=(-0.35, 1), title="$I_{ext} = 0.01$ from 1 to 1.20s")
axes[0].plot(ts, v, label="neuron")
axes[0].plot(ts, i_ext, label="power surge", color="r")
axes[0].legend()

v_, w_, i_ext_ = run_fhn(1, 1.20, 0.03)

axes[1].plot(ts, v_, label="neuron")
axes[1].plot(ts, i_ext_, label="power surge", color="r")
axes[1].set(xlim=(0, 4), ylim=(-0.35, 1), title="$I_{ext} = 0.03$ from 1 to 1.20s")

axes[1].legend()

plt.show()
