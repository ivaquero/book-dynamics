import matplotlib.pyplot as plt

from .ode.field_2d import gen_mesh, vector_field
from .ode.integrators import euler_fixed


def lotka_volterra(t, z, coefs=None):
    if coefs is None:
        coefs = [0.5, 0.01, 0.2, 0.005]
    x, y = z
    a, b, c, d = coefs
    return [a * x - b * x * y, -c * y + d * x * y]


# Use shared `gen_mesh` and `vector_field` from `ode.field_2d`


# Use shared explicit Euler integrator from ode.integrators


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
    # wrapper keeps signature f(t, z)
    f = lambda t, z: lotka_volterra(t, z)
    traj, times = euler_fixed(f, xy_init, step, period)
    x = traj[:, 0]
    y = traj[:, 1]
    axes[ind].scatter(x, y)
    vector_field(axes[ind], X, Y, U, V)
    axes[ind].set(title=f"δt = {step}")
