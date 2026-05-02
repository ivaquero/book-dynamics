import matplotlib.pyplot as plt

from .dynamics.attractors import complex_set

num_iter = 50
n_points = 1000
X0 = [-2, 2, -2, 2]

X, Y, Q = complex_set(num_iter, n_points, X0, "Mandelbrot")

_, ax = plt.subplots()
ax.pcolormesh(X, Y, Q, cmap="Greys")
ax.axis("equal")
plt.show()
