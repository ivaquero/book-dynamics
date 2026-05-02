import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import HPG, HPG2
from .ode.integrators import euler_fixed

fig = plt.figure()
ax = fig.add_subplot(121, projection="3d")

xyz_init = [1, 0.2, 2]
step_size, period = 0.1, 1000

# integrate using shared euler_fixed
traj, times = euler_fixed(lambda t, z: HPG(t, z), xyz_init, step_size, period)

x = traj[:, 0]
y = traj[:, 1]
z = traj[:, 2]

# compute derivatives for arrows
derivs = np.array([HPG(t=0, init=row) for row in traj])
dx = derivs[:, 0]
dy = derivs[:, 1]
dz = derivs[:, 2]

for i in range(100, 1000, 400):
    ax.quiver(x[i], y[i], z[i], dx[i], dy[i], dz[i], color="red")

ax.plot(x, y, z, label="Limit Cycle of HPG", color="r")
ax.legend()


ax2 = fig.add_subplot(122)

t_span = [0, 100]
t = np.linspace(t_span[0], t_span[1], 1000)

# Number of starting points:
θs = np.linspace(0, 2 * np.pi, 5)
coordinates = []

for θ in θs:
    coordinates.extend(
        ([1.5 * np.cos(θ), 1.5 * np.sin(θ)], [0.05 * np.cos(θ), 0.05 * np.sin(θ)])
    )

for coordinate in coordinates:
    x_i = coordinate[0]
    y_i = coordinate[1]
    sol = solve_ivp(HPG2, t_span, [x_i, y_i], dense_output=True)
    X = sol.sol(t).T
    x, y = X[:, 0], X[:, 1]
    ax2.plot(x, y)

# ax2.set(xlim=(-2, 2)
# ax2.set(ylim=(-2, 4)
plt.show()
