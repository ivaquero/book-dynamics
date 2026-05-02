import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate, linalg

from .ode.field_2d import derivatives, gen_mesh, vector_field
from .ode.stability import pillar

xy_range = [0, 100, 0, 100]
n_points = 15
A, B = gen_mesh(xy_range, n_points)
coefs = (9 / 7, -4 / 7, 8 / 7, -9 / 7)
u, v = derivatives(0, [A, B], *coefs)

_, axes = plt.subplots(1, 2, constrained_layout=1)

xy_inits = [[2, 1], [20, 80]]
vecs = [1, 10]
colors = ["b", "r"]

M = np.array([coefs[0:2], coefs[2:4]])
eigen_values, eigen_vectors = linalg.eig(M)
X, Y = eigen_vectors
origin = [0, 0]

t_spans = [[0, 10], [0, 100]]
ts = [
    np.linspace(t_spans[0][0], t_spans[0][1], 5000),
    np.linspace(t_spans[1][0], t_spans[1][1], 5000),
]

for i, (t_span, xy_init, vec, _color) in enumerate(
    zip(t_spans, xy_inits, vecs, colors, strict=True)
):
    sol = integrate.solve_ivp(
        derivatives, t_span, xy_init, args=coefs, dense_output=True
    )
    Z = sol.sol(ts[i]).T
    x, y = Z[:, 0], Z[:, 1]

    x_arrows, y_arrows, time = pillar(x, y, vec)
    direction_x = np.array(x_arrows[1:]) - np.array(x_arrows[:-1])
    direction_y = np.array(y_arrows[1:]) - np.array(y_arrows[:-1])
    axes[i].quiver(
        x_arrows[:-1],
        y_arrows[:-1],
        direction_x,
        direction_y,
        scale=1000,
        lw=time[:-1],
        color=_color,
    )

    vector_field(axes[i], A, B, u, v)
    axes[i].quiver(
        origin,
        origin,
        X,
        Y,
        scale=0.01,
        scale_units="xy",
        angles="xy",
        color=["b", "g"],
    )

    axes[i].plot(x, y, color=_color)
    axes[i].set(xlim=(0, 100), ylim=(0, 100))
