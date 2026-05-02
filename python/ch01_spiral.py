import matplotlib.pyplot as plt

from .dynamics.attractors import clarinet
from .ode.integrators import euler_fixed

_, ax = plt.subplots()

xy_inits = [[0, 0.1], [1.2, 1.2]]
step_sizes = [0.1, 0.1]
periods = [150, 80]


# wrapper to accept (t, z) signature
def f(t, z):
    return clarinet(t, z, a=1)


for xy_init, step_size, period in zip(xy_inits, step_sizes, periods, strict=True):
    traj, t = euler_fixed(f, xy_init, step_size, period)
    x = traj[:, 0]
    y = traj[:, 1]

    ax.plot(x, y)
    ax.set(xlim=(-2, 2))
