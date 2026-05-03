import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import fhn_nullclines

V = np.arange(-2, 2.05, 0.01)
W, w_ = fhn_nullclines(V, theta=0.1, gamma_slope=2.0)

_, ax = plt.subplots()

ax.plot(V, W)
ax.plot(V, w_)
ax.set(xlim=(-2, 2.05))

plt.show()
