import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from sympy import symbols

from .dynamics.bifurcations import opinion, stablity


def pitchwork(a_vals, x_vals):
    final_xs, final_ys = [], []
    final_x, final_y = [], []

    for a in a_vals:
        values = opinion(x_vals, a)
        x_list = [
            x_vals[i + 1]
            for i in range(len(values) - 1)
            if (values[i] <= 0 and values[i + 1] >= 0)
            or (values[i] >= 0 and values[i + 1] <= 0)
        ]

        # find null_points:
        null_points = np.zeros(len(x_list))
        for i, x in enumerate(x_list):
            null_points[i] = brentq(opinion, x - 0.02, x + 0.02, args=(a,))
            # 0.01 is the spacing between 2 points with different sign -> 0.02 certainly
        for null_point in null_points:
            if stablity(null_point, opinion, a):
                final_xs.append(a)
                final_ys.append(null_point)
            else:
                final_x.append(a)
                final_y.append(null_point)
    return final_xs, final_ys, final_x, final_y


a = 1.3
x = np.arange(-1, 1, 0.01)

a_vals = np.arange(-1, 2, 0.01)
x_vals = np.arange(-1, 1, 0.01)

X = symbols("X")
final_xs, final_ys, final_x, final_y = pitchwork(a_vals, x_vals)

_, ax = plt.subplots()

ax.scatter(final_xs, final_ys, color="g")
ax.scatter(final_x, final_y, color="r")
plt.show()
