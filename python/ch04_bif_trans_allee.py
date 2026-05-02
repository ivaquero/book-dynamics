import matplotlib.pyplot as plt
import numpy as np

from .dynamics.bifurcations import allee, arrows_param, stablity

x_range = [1, 2000]
interval = 1

a_array = np.arange(x_range[0], x_range[1], interval)

stable_x, stable_y = [], []
unstable_x, unstable_y = [], []
zero_x_stable, zero_y_stable = [], []
zero_x_unstable, zero_y_unstable = [], []

for a in a_array:
    if stablity(a, allee, a):
        stable_x.append(a)
        stable_y.append(a)
    else:
        unstable_x.append(a)
        unstable_y.append(a)

    if stablity(1000, allee, a):
        stable_x.append(a)
        stable_y.append(1000)
    else:
        unstable_x.append(a)
        unstable_y.append(1000)

    if stablity(0, allee, a):
        zero_x_stable.append(a)
        zero_y_stable.append(0)
    else:
        zero_x_unstable.append(a)
        zero_y_unstable.append(0)

_, ax = plt.subplots()

ax.plot(stable_x, stable_y, color="g", label="stable")
ax.plot(unstable_x, unstable_y, color="r", label="unstable")
ax.plot(zero_x_stable, zero_y_stable, linestyle="-.", color="g", label="zero stable")
ax.plot(
    zero_x_unstable, zero_y_unstable, linestyle="-.", color="r", label="zero unstable"
)


def arrows(a, X, head_width=50, head_length=75):
    ax.vlines(a, 0, 2000, color="black")
    for x in X:
        points_at = allee(x, a)
        ax.arrow(
            a,
            x,
            0,
            points_at,
            head_width=head_width,
            head_length=head_length,
            color="black",
        )


arrows_param(ax, 300, [-50, 100, 500, 1200], allee)
arrows_param(ax, 500, [-50, 100, 500, 1200], allee)
arrows_param(ax, 1200, [-50, 250, 1110, 1500], allee)
ax.set(xlabel="a", ylabel="X")
ax.legend(loc="right")
plt.show()
