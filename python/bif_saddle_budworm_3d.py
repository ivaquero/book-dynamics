import matplotlib.pyplot as plt
import numpy as np

from .dynamics.bifurcations import track_in_3D

n_points = 20
r_range = [0, 0.6]
k_range = [0, 40]
rs = np.linspace(r_range[0], r_range[1], n_points)
ks = np.linspace(k_range[0], k_range[1], n_points)
stable_points, unstable_points = track_in_3D(rs, ks)

fig, ax = plt.subplots()

ax = fig.axes(projection="3d")

ax.scatter(stable_points[0], stable_points[1], stable_points[2], color="g")
ax.scatter(unstable_points[0], unstable_points[1], unstable_points[2], color="r")

plt.show()
