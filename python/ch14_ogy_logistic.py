"""OGY 参数微扰控制在 Logistic 映射上的演示。

以 x_{n+1} = r x_n (1 - x_n) 在 r = 3.8 处的不稳定不动点为控制目标。
控制律只在所需微扰落在允许区间 |dr| <= dr_max 时启用；否则令 dr = 0，
等轨道自行游走回目标邻域，即所谓「等待捕获」。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

R_NOMINAL = 3.8
X_FIXED = 1 - 1 / R_NOMINAL
LAMBDA_U = R_NOMINAL * (1 - 2 * X_FIXED)
B_LIN = X_FIXED * (1 - X_FIXED)
N_FREE = 150
N_CTRL = 500
DR_MAX = 0.05
OUT = Path(__file__).resolve().parent.parent / "images" / "ch14" / "ogy-logistic.svg"


def logistic(x, r):
    return r * x * (1 - x)


def run(x0, n_free, n_ctrl, dr_max):
    """返回轨迹、微扰序列与首次捕获的步号。"""
    n_total = n_free + n_ctrl
    x = np.empty(n_total)
    dr = np.zeros(n_total)
    captured = None
    x[0] = x0

    for n in range(1, n_total):
        if n > n_free:
            ideal = -LAMBDA_U * (x[n - 1] - X_FIXED) / B_LIN
            if abs(ideal) <= dr_max:
                dr[n] = ideal
                captured = n if captured is None else captured
        x[n] = logistic(x[n - 1], R_NOMINAL + dr[n])

    return x, dr, captured


def main():
    rng = np.random.default_rng(42)
    x, dr, captured = run(rng.uniform(0.3, 0.7), N_FREE, N_CTRL, DR_MAX)
    print(
        f"不动点 x_F = {X_FIXED:.4f}, lambda_u = {LAMBDA_U:.3f}, 第 {captured} 步捕获"
    )

    _, (ax_x, ax_p) = plt.subplots(2, 1, figsize=(7, 4), sharex=True)

    ax_x.plot(x, "k-", lw=0.9)
    ax_x.axhline(X_FIXED, color="tab:red", ls="--", lw=1, label="$x_F$")
    ax_x.axvline(N_FREE, color="tab:blue", ls=":", lw=1.2)
    ax_x.set(ylabel="$x_n$", ylim=(0, 1.05))
    ax_x.legend(loc="lower right", frameon=False)
    ax_x.annotate(
        "control on",
        xy=(N_FREE, 0.98),
        xytext=(N_FREE + 8, 0.98),
        color="tab:blue",
        fontsize=8,
        va="top",
    )

    ax_p.plot(dr, "tab:blue", lw=1)
    for bound in (DR_MAX, -DR_MAX):
        ax_p.axhline(bound, color="gray", ls="--", lw=0.8)
    ax_p.axvline(N_FREE, color="tab:blue", ls=":", lw=1.2)
    ax_p.set(xlabel="$n$", ylabel=r"$\delta r$", ylim=(-1.15 * DR_MAX, 1.15 * DR_MAX))

    plt.tight_layout()
    plt.savefig(OUT, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
