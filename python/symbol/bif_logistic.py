import matplotlib.pyplot as plt
import numpy as np

from ..dynamics.bifurcations import number_track

# colormap
# cmap = colors.ListedColormap(['red', 'orange'])
# bounds=[1,2,3]
extent = [0, 1, 0, 1]
# norm = colors.BoundaryNorm(bounds, cmap.N)
h_vals = np.linspace(0, 1, 20)
a_vals = np.linspace(0, 1, 20)
matrix = number_track(h_vals, a_vals)

_, ax = plt.subplots()

image = ax.imshow(matrix, extent=extent, aspect="auto")

plt.show()
