import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import collins
from .ode.field_2d import gen_mesh, vector_field

xy_range = [0, 5, 0, 5]
n_points = 10
A, B = gen_mesh(xy_range, n_points)
u, v = collins(t=0, z=[A, B])

_, ax = plt.subplots()

vector_field(ax, A, B, u, v)

row, col = np.arange(0, 5, 0.1), np.arange(0, 5, 0.1)
null_row, null_col = 5 / (1 + col**4), 5 / (1 + row**4)

ax.plot(row, null_col)
ax.plot(null_row, col)
