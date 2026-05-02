from itertools import product

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate, linalg

from .plot.field_2d import derivatives, gen_mesh

a, b, c, d = 2, 1, 1, 2
m = np.array([[a, b], [c, d]])
eigen = linalg.eig(m)[0]


xlabel, ylabel = ["x", "u"], ["y", "v"]
ic = np.linspace(-1, 1, 5)

t_span1 = [0, 4]
t_span2 = [-4, 0]
t1 = np.linspace(t_span1[0], t_span1[1], 1000)
t2 = np.linspace(t_span2[0], t_span2[1], 1000)

xy_range = [-1, 1, -1, 1]
n_points = 10

_, ax = plt.subplots(1, 2, constrained_layout=1)

for i in range(2):
    if i == 1:
        a, b, c, d = eigen[1], 0, 0, eigen[0]

    for init in product(ic, ic):
        sol1 = integrate.solve_ivp(derivatives, t_span1, init, dense_output=True)
        X1 = sol1.sol(t1).T
        x1, y1 = X1[:, 0], X1[:, 1]
        ax[i].plot(x1, y1, "r-")
        sol2 = integrate.solve_ivp(derivatives, t_span2, init, dense_output=True)
        X2 = sol1.sol(t1).T
        x2, y2 = X1[:, 0], X1[:, 1]
        ax[i].plot(x2, y2, "r-")

    ax[i].set(xlim=(-1, 1), ylim=(-1, 1), xlabel=xlabel[i], ylabel=ylabel[i])

    major_locator = plt.MultipleLocator(0.5)
    ax[i].xaxis.set_major_locator(major_locator)
    ax[i].yaxis.set_major_locator(major_locator)

    # 箭头位置
    X, Y = gen_mesh(xy_range, n_points)
    # X, Y = np.mgrid[-1:1:10j, -1:1:10j]
    # 箭头方向，通常为二维度组
    u, v = derivatives(t=0, z=[X, Y])
    ax[i].quiver(X, Y, u, v, color="b")
