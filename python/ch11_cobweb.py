import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import logistic_map
from .dynamics.maps import cobweb_points, draw_cobweb

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=1)

r = 4
X_init = 0.01
step = 50


ax1.set(xlim=(0, 1), ylim=(0, 1.1))
draw_cobweb(ax1, step, X_init, r)

T = np.arange(0, 1, 0.001)
X = logistic_map(T, 4)

ax1.plot(T, X, color="black")
ax1.plot(T, T, color="grey")

ax2.set(xlim=(0, step), ylim=(0, 1.1))
T = np.arange(0, step, 1)
X = np.zeros(step)


X = cobweb_points(X_init, r, len(T))
ax2.plot(T, X, color="b")
ax2.scatter(T, X, color="black")
plt.show()
