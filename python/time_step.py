import matplotlib.pyplot as plt
import numpy as np

from .dynamics.symbolic import build_piecewise_time_lambdas

tmax = 10
tmax_default = 10
functions, tmax = build_piecewise_time_lambdas(tmax_default)

t = np.linspace(-1, 10, 1000)
conditions = [t <= 0] + [t > i for i in range(tmax)]

_, ax = plt.subplots()

ax.plot(t, np.piecewise(t, conditions, functions))

ax.set(xlabel="t", ylabel="x(t)")
plt.show()
