import matplotlib.pyplot as plt

from .dynamics.attractors import henon
from .dynamics.maps import iterate_map_2d

a = 1.2  # Set a= 1 to get Figure 14.23(a)
b = 0.4
num_iterations = 10000


X0 = [(1 - b) / 2, (1 - b) / 2]

# warmup iterates (discarded)
_, _ = iterate_map_2d(henon, X0, 100, a, b)

X, Y = iterate_map_2d(henon, X0, num_iterations, a, b)

_, ax = plt.subplots()

ax.plot(X, Y, "b.", ms=1)
ax.set(xlabel="x", ylabel="y")
plt.show()
