"""Pyragas 时滞反馈控制 Lorenz 系统的演示。

在 $t = t_\\text{sw}$ 时刻接入反馈 $\\bm{u} = K[\\bm{x}(t - \\tau) - \\bm{x}(t)]$，
目标为 Lorenz 系统的不稳定平衡点 $C_+$。反馈项在该点上恒为零，因此平衡点在
接入控制后位置不变，只改变其稳定性；但增益过大反而会把轨道推出稳定域。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

SIGMA, RHO, BETA = 10.0, 28.0, 8.0 / 3.0
TARGET = np.array([np.sqrt(BETA * (RHO - 1))] * 2 + [RHO - 1])
DT = 0.005
TAU = 0.5
T_SWITCH = 40.0
T_TOTAL = 80.0
X0 = np.array([1.0, 1.0, 1.0])
OUT = Path(__file__).resolve().parent.parent / "images" / "ch14" / "pyragas-lorenz.svg"


def lorenz(s):
    return np.array(
        [SIGMA * (s[1] - s[0]), s[0] * (RHO - s[2]) - s[1], s[0] * s[1] - BETA * s[2]]
    )


def rk4(s, u, dt):
    k1 = lorenz(s) + u
    k2 = lorenz(s + 0.5 * dt * k1) + u
    k3 = lorenz(s + 0.5 * dt * k2) + u
    k4 = lorenz(s + dt * k3) + u
    return s + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)


def integrate(t_total, dt, tau, gain, t_switch, x0):
    """固定时滞的显式积分：时滞项取 t - tau 处的历史值。"""
    n_steps = int(round(t_total / dt))
    n_tau = int(round(tau / dt))
    traj = np.empty((n_steps, 3))
    traj[0] = x0

    for i in range(1, n_steps):
        u = np.zeros(3)
        if i * dt >= t_switch:
            u = gain * (traj[max(i - n_tau, 0)] - traj[i - 1])
        traj[i] = rk4(traj[i - 1], u, dt)

    return np.arange(n_steps) * dt, traj


def main():
    t, traj_small = integrate(T_TOTAL, DT, TAU, 2.0, T_SWITCH, X0)
    _, traj_large = integrate(T_TOTAL, DT, TAU, 12.0, T_SWITCH, X0)

    _, (ax_t, ax_e) = plt.subplots(2, 1, figsize=(7, 4.4), sharex=True)

    ax_t.plot(t, traj_small[:, 0], "k-", lw=0.8)
    ax_t.axhline(TARGET[0], color="tab:red", ls="--", lw=1, label="$x^*_{C_+}$")
    ax_t.axvline(T_SWITCH, color="tab:blue", ls=":", lw=1.2)
    ax_t.set(ylabel="$x(t)$", ylim=(-12, 22))
    ax_t.legend(loc="upper right", frameon=False, ncol=2)
    ax_t.annotate(
        "control on, $K = 2$",
        xy=(T_SWITCH, 0.92),
        xycoords=("data", "axes fraction"),
        xytext=(T_SWITCH + 2, 0.92),
        textcoords=("data", "axes fraction"),
        color="tab:blue",
        fontsize=8,
    )

    for traj, style, name in (
        (traj_small, "tab:blue", "$K = 2$"),
        (traj_large, "tab:orange", "$K = 12$"),
    ):
        err = np.linalg.norm(traj - TARGET, axis=1)
        ax_e.semilogy(t, np.maximum(err, 1e-6), style, lw=1, label=name)

    ax_e.axvline(T_SWITCH, color="k", ls=":", lw=1)
    ax_e.set(xlabel="$t$", ylabel="$\\| \\mathbf{x} - \\mathbf{x}^* \\|$")
    ax_e.legend(loc="lower left", frameon=False)

    plt.tight_layout()
    plt.savefig(OUT, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
