v_1, w_1, v_2, w_2, i_ext = euler([1, 1.20, 0.025])
import matplotlib.pyplot as plt
import numpy as np

from .ode.integrators import euler_fixed

ts = np.arange(0, 4, 0.01)


def FHN_coupled(Z, I_ext, R=45, a=0.1, γ=0.5, ϵ=0.008):
    V_1, w_1, V_2, w_2 = Z
    I_c21 = (V_2 - V_1) / R
    I_c12 = (V_1 - V_2) / R

    V_1_ = (1 / ϵ) * (-w_1 + V_1 * (1 - V_1) * (V_1 - a) + I_c21 + I_ext)
    w_1_ = V_1 - γ * w_1
    V_2_ = (1 / ϵ) * (-w_2 + V_2 * (1 - V_2) * (V_2 - a) + I_c12)
    w_2_ = V_2 - γ * w_2

    return [V_1_, w_1_, V_2_, w_2_]


def run_coupled(start_puls, stop_puls, recover_puls):
    def f(t, z):
        i_ext = recover_puls if start_puls <= t <= stop_puls else 0
        return FHN_coupled(z, i_ext)

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
