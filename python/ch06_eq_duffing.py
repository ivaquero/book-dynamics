import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import duffing
from .dynamics.plotting import plot_phase, plot_poincare

α, β, ω, γ = 1, -1, 1.25, 0.5
k = 0.3


z = [1, 0]
t_span = [0, 1000]
n_period = (2 * np.pi) / ω

_, axes = plt.subplots(1, 2, constrained_layout=1)

plot_phase(func=duffing, t_span=t_span, z=z, ax=axes[0])
plot_poincare(func=duffing, t_span=t_span, z=z, n_period=n_period, ax=axes[1])
plt.show()
