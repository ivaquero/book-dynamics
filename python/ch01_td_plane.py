"""Trace-determinant 平面上的临界点分类图。

对应 01 章「系统的分类」一节：横轴 T = tr(A)，纵轴 D = det(A)，
抛物线 T^2 = 4D 与纵轴把平面分成若干区域，每区对应一类临界点。

输出：images/ch01/td-plane.svg（矢量）
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "images" / "ch01" / "td-plane.svg"

T = np.linspace(-4.0, 4.0, 600)
D = np.linspace(-3.0, 5.0, 600)
TT, DD = np.meshgrid(T, D)

PARABOLA = TT**2 / 4

code = np.zeros_like(TT, dtype=int)
upper = DD > 0
code[upper & (TT < 0) & (DD > PARABOLA)] = 1  # 稳定结点
code[upper & (TT < 0) & (DD < PARABOLA)] = 2  # 稳定焦点
code[upper & (TT > 0) & (DD > PARABOLA)] = 3  # 不稳定结点
code[upper & (TT > 0) & (DD < PARABOLA)] = 4  # 不稳定焦点

COLORS = {
    0: "#f5ecd4",  # 鞍点
    1: "#cfe0ef",  # 稳定结点
    2: "#9dc2de",  # 稳定焦点
    3: "#f4d2c6",  # 不稳定结点
    4: "#e3a48f",  # 不稳定焦点
}

fig, ax = plt.subplots(figsize=(5.4, 4.6))

for key, color in COLORS.items():
    ax.contourf(TT, DD, (code == key).astype(float), levels=[0.5, 1.5], colors=[color])

ax.plot(T, T**2 / 4, color="#222222", lw=1.4, zorder=5)
ax.axhline(0, color="#222222", lw=1.4, zorder=5)
ax.axvline(0, color="#222222", lw=0.9, ls=(0, (3, 3)), zorder=4)

# 区域标签：位置手工调过，避开曲线与坐标轴
ax.text(-2.45, 3.30, "stable node", ha="center", fontsize=8.5, color="#14304a")
ax.text(-2.05, 0.30, "stable focus", ha="center", fontsize=8.5, color="#14304a")
ax.text(2.45, 3.30, "unstable node", ha="center", fontsize=8.5, color="#5c2416")
ax.text(2.05, 0.30, "unstable focus", ha="center", fontsize=8.5, color="#5c2416")
ax.text(0.0, -1.7, "saddle", ha="center", fontsize=8.5, color="#4a3c10")

# 中心：纵轴上 D>0 的一段，用圆点标出并加引线说明
ax.plot(0, 1.6, marker="o", ms=4, color="#222222", zorder=6)
ax.annotate(
    "center",
    xy=(0, 1.6),
    xytext=(0.55, 2.15),
    fontsize=8.5,
    color="#1a1a1a",
    arrowprops={"arrowstyle": "-", "lw": 0.7, "color": "#444444"},
)

ax.set_xlim(-4, 4)
ax.set_ylim(-3, 5)
ax.set_xlabel(r"$T = \operatorname{tr}\mathbf{A}$", fontsize=10)
ax.set_ylabel(r"$D = \det\mathbf{A}$", fontsize=10)
ax.set_xticks([-4, -2, 0, 2, 4])
ax.set_yticks([-2, 0, 2, 4])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(labelsize=9)

fig.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, format="svg")
print(f"saved {OUT}")
