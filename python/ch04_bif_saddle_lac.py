import matplotlib.pyplot as plt
import numpy as np

from .dynamics.bifurcations import arrows_with_r, lac, stablity

x_range = [0.001, 10]
X = np.linspace(x_range[0], x_range[1], 2000)
a = 0.006
r = (1 / X) * (a + X**2) / (1 + X**2)

stable_x = []
stable_y = []
unstable_x = []
unstable_y = []

for ri, x in zip(r, X, strict=True):
    if stablity(x, lac, a, ri):
        stable_x.append(ri)
        stable_y.append(x)
    else:
        unstable_x.append(ri)
        unstable_y.append(x)

_, ax = plt.subplots()

ax.scatter(stable_x, stable_y, color="g")
ax.scatter(unstable_x, unstable_y, color="r")
ax.plot(r, X)
ax.set(xlim=(0, 1), xlabel="r", ylabel="X")


arrows_with_r(ax, 0.2, [2, 6], lac, a)
arrows_with_r(ax, 0.4, [1, 6], lac, a)
arrows_with_r(ax, 0.6, [1, 6], lac, a)

plt.show()
