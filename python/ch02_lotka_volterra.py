import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def lotka_volterra(t, z, coefs):
    x, y = z
    a, b, c, d = coefs
    return [a * x - b * x * y, -c * y + d * x * y]


def generate_mesh_2d(xy_range, n_points):
    X, Y = np.meshgrid(
        np.linspace(xy_range[0], xy_range[1], n_points),
        np.linspace(xy_range[2], xy_range[3], n_points),
    )
    return X, Y


def vector_field(X, Y, U, V, ax):
    M = np.hypot(U, V)  # Norm of the growth rate
    M[M == 0] = 1  # Avoid zero division errors
    U /= M  # Normalize each vector_field
    V /= M
    ax.quiver(X, Y, U, V, M, pivot="mid", cmap=plt.cm.jet)


_, (ax, ax2) = plt.subplots(1, 2, figsize=(10, 5), constrained_layout=1)

xy_range = [0, 5, 0, 10]
n_points = 20
coefs = [1, 0.7, 0.35, 1]
a, b, c, d = coefs

# create a grid
X, Y = generate_mesh_2d(xy_range, n_points)
# compute growth rate on the grid
U, V = lotka_volterra(t=0, z=[X, Y], coefs=coefs)
vector_field(X, Y, U, V, ax)

X_R = [c / d, a / b]
t_span = [0, 100]

vals = np.linspace(1, 5, 5)
v_colors = plt.cm.autumn_r(vals)
t = np.linspace(t_span[0], t_span[1], 1000)

for v, col in zip(vals, v_colors, strict=True):
    z = v * np.array(X_R)
    sol = solve_ivp(lotka_volterra, t_span, z, args=([coefs]), dense_output=True)
    X = sol.sol(t).T
    preys, predators = X[:, 0], X[:, 1]
    ax.plot(preys, predators, color=col, label=f"X0=({z[0]:.0f}, {z[1]:.0f})")

ax.set(
    xlabel="Number of Preys",
    ylabel="Number of Predators",
    xlim=(xy_range[0], xy_range[1]),
    ylim=(xy_range[2], xy_range[3]),
)
ax.grid()
ax.legend()

# curves
X0 = [10, 5]
sol2 = solve_ivp(lotka_volterra, t_span, X0, args=([coefs]), dense_output=True)

z = sol2.sol(t).T

ax2.plot(t, z)
ax2.set(xlabel="Time", ylabel="Population", xlim=(t_span[0], t_span[1]))
ax2.grid()
ax2.legend(["Preys", "Predators"])
