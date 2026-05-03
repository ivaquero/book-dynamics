import matplotlib.pyplot as plt

from .dynamics.attractors import rossler
from .ode.integrators import euler_fixed

dt = 0.01
step_count = 50000

# initial conditions
xyz0 = [1.0, 1.0, 1.0]

# integrate using shared euler_fixed
traj, times = euler_fixed(rossler, xyz0, dt, step_count)

xs = traj[:, 0]
ys = traj[:, 1]
zs = traj[:, 2]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot(xs, ys, zs, lw=0.5)
ax.set(xlabel="x", ylabel="y", zlabel="z", title="Rossler Attractor")
plt.show()
