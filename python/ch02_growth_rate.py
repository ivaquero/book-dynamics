import matplotlib.pyplot as plt
import numpy as np
from .ode.field_2d import gen_mesh, vector_field


def lotka_volterra(t, z, coefs=None):
    if coefs is None:
        coefs = [0.5, 0.01, 0.2, 0.005]
    x, y = z
    a, b, c, d = coefs
    return [a * x - b * x * y, -c * y + d * x * y]


# Use shared `gen_mesh` and `vector_field` from `ode.field_2d`


def euler2(xy_init, step_size, period):
    X, Y = xy_init
    x, y = [], []
    time = []
    for i in range(period):
        x.append(X)
        y.append(Y)
        # 每次 + 步长 * 导数（上一对 x,y）
        z = [x[-1], y[-1]]
        X += step_size * lotka_volterra(t=0, z=z)[0]
        Y += step_size * lotka_volterra(t=0, z=z)[1]
        time.append(step_size * i)
    return x, y, time


xy_range = [0, 100, 0, 100]
n_points = 15

# create a grid
X, Y = gen_mesh(xy_range, n_points)
# compute growth rate on the grid
U, V = lotka_volterra(t=0, z=[X, Y])

_, axes = plt.subplots(1, 2)

step_sizes = [0.01, 0.1]
xy_init = [80, 60]
period = 10000

for ind, step in enumerate(step_sizes):
    x, y, time = euler2(xy_init, step, period)
    axes[ind].scatter(x, y)
    vector_field(axes[ind], X, Y, U, V)
    axes[ind].set(title=f"δt = {step}")
