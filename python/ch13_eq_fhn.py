import matplotlib.pyplot as plt
import numpy as np

_, axes = plt.subplots(1, 2, constrained_layout=1)
ts = np.arange(0, 4, 0.01)


def FHN(V, w, II, a=0.1, γ=1, ϵ=0.01):
    V_ = (1 / ϵ) * (-w + V * (1 - V) * (V - a) + II)
    w_ = V - γ * w
    return [V_, w_]


from .ode.integrators import euler_fixed


def run_fhn(start_puls, stop_puls, recover_puls):
    def f(t, z):
        V, w = z
        i_ext = recover_puls if start_puls <= t <= stop_puls else 0
        return FHN(V, w, i_ext)

    step = ts[1] - ts[0]
    traj, times = euler_fixed(f, [0, 0], step, len(ts))
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
