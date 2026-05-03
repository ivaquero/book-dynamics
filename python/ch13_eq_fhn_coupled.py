import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import pulsed_FHN_coupled_factory
from .ode.integrators import euler_fixed

ts = np.arange(0, 4, 0.01)


def run_coupled(start_puls, stop_puls, recover_puls):
    f = pulsed_FHN_coupled_factory(start_puls, stop_puls, recover_puls)

    step = ts[1] - ts[0]
    traj, times = euler_fixed(f, [0, 0, 0, 0], step, len(ts))
    v_1 = traj[:, 0]
    v_2 = traj[:, 2]
    i_ext = [recover_puls if start_puls <= tt <= stop_puls else 0 for tt in times]
    return v_1, v_2, i_ext


v_1, v_2, i_ext = run_coupled(1, 1.20, 0.025)

_, ax = plt.subplots()

ax.set(xlim=(0, 4), ylim=(-0.35, 1))
ax.plot(ts, v_1, label="neuron 1")
ax.plot(ts, v_2, label="neuron 2")
ax.plot(ts, i_ext, label="power surge", title="2 connected neurons")
ax.legend()
plt.show()
