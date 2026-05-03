import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

from .dynamics.bifurcations import number_track

n_points = 20
r_range = [0, 0.6]
k_range = [0, 40]
rs = np.linspace(r_range[0], r_range[1], n_points)
ks = np.linspace(k_range[0], k_range[1], n_points)

matrix = []

cmap = colors.ListedColormap(["red", "orange"])
bounds = [1, 2, 3]
extent = [0, 40, 0, 0.6]
norm = colors.BoundaryNorm(bounds, cmap.N)

matrix = number_track(rs, ks, n_points)

_, ax = plt.subplots()

image = ax.imshow(
    matrix,
    interpolation="nearest",
    origin="lower",
    cmap=cmap,
    norm=norm,
    extent=extent,
    aspect="auto",
)

plt.colorbar(image, boundaries=bounds, ticks=[1, 2, 3])
plt.show()
