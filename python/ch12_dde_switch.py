"""延迟微分方程 $\\dot{x} = -x(t - \\tau)$ 的稳定性切换。

特征方程为 $\\lambda = -e^{-\\lambda \\tau}$，在 $\\tau = \\pi / 2$ 处一对共轭特征根
穿越虚轴（$\\lambda = \\pm i$），平衡点由渐近稳定转为不稳定。
上图给出主支特征根实部随 $\\tau$ 的变化，下图给出两种 $\\tau$ 下的解。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import lambertw

TAU_STABLE = 1.0
TAU_UNSTABLE = 2.0
DT = 0.002
T_END = 30.0
OUT = Path(__file__).resolve().parent.parent / "images" / "ch12" / "dde-switch.svg"


def solve_steps(tau, t_end, dt):
    """用时间步法（分段 Euler）求解 x' = -x(t - tau)，历史函数取 x = 1。"""
    n = int(round(t_end / dt))
    n_tau = int(round(tau / dt))
    x = np.ones(n + 1)
    for i in range(1, n + 1):
        past = x[max(i - n_tau, 0)]
        x[i] = x[i - 1] - dt * past
    return np.arange(n + 1) * dt, x


def main():
    tau = np.linspace(0.05, 4.0, 800)
    root = lambertw(-tau) / tau

    _, (ax_r, ax_x) = plt.subplots(2, 1, figsize=(7, 4.6))

    ax_r.plot(tau, root.real, "k-", lw=1.2, label=r"$\mathrm{Re}\,\lambda$")
    ax_r.plot(
        tau, root.imag, "tab:purple", ls="--", lw=1, label=r"$\mathrm{Im}\,\lambda$"
    )
    ax_r.axhline(0, color="gray", lw=0.8)
    ax_r.axvline(np.pi / 2, color="tab:red", ls=":", lw=1.2)
    ax_r.annotate(
        r"$\tau = \pi/2$",
        xy=(np.pi / 2, 0.6),
        xytext=(np.pi / 2 + 0.12, 0.6),
        color="tab:red",
        fontsize=9,
    )
    ax_r.set(xlabel=r"$\tau$", ylabel="eigenvalue", ylim=(-1.6, 1.6))
    ax_r.legend(loc="lower right", frameon=False)

    for tau_i, style, name in (
        (TAU_STABLE, "tab:blue", r"$\tau = 1 < \pi/2$"),
        (TAU_UNSTABLE, "tab:orange", r"$\tau = 2 > \pi/2$"),
    ):
        t, x = solve_steps(tau_i, T_END, DT)
        ax_x.plot(t, x, style, lw=1.1, label=name)

    ax_x.axhline(0, color="gray", lw=0.8)
    ax_x.set(xlabel="$t$", ylabel="$x(t)$")
    ax_x.legend(loc="upper left", frameon=False)

    plt.tight_layout()
    plt.savefig(OUT, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
