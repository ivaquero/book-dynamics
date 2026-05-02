import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import iterate_map as ppen

T = np.arange(0, 500, 1)
X = np.zeros(500)
X_ = np.arange(0, 1, 0.001)
f = 4 * X_ * (1 - X_)


X = ppen(0.4, 4, len(T))

_, ax = plt.subplots()

ax.scatter(X[:-1], X[1:])
ax.plot(X_, f)
plt.show()
