import matplotlib.cm as cm
import matplotlib.pyplot as plt

# $$fc(z) = z2 + C$$
# Choose a complex C as the 'seed'.
from .dynamics.attractors import julia_set

julia = julia_set(complex(0.9, 0.5))

# Plot the array using matplotlib's imshow
_, ax = plt.subplots()

ax.imshow(julia, interpolation="nearest", cmap=cm.gnuplot2)
ax.axis("off")
plt.show()
