from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import mckey_glass
from .dynamics.integrators import euler_delay

n_list = np.arange(0, 0.5, 0.01)
τ_list = np.arange(0, 0.5, 0.01)
ts = np.arange(0, 10, 0.01)
L, Vmax = 6, 16


matrix = np.zeros((len(n_list), len(τ_list)))

step_size = ts[1] - ts[0]
period = len(ts)

for i, n in enumerate(n_list):
    for j, τ in enumerate(τ_list):
        func = partial(mckey_glass, n=n)
        x_arr = euler_delay(func, 2, step_size, period, τ, history_value=0.5)

        count = 0
        currency_sign = -1
        delay_steps = round(τ / step_size)

        for ii in range(period):
            if ii * step_size <= τ or ii - delay_steps < 0:
                X_tau = 0.5
            else:
                X_tau = x_arr[ii - delay_steps]

            val = mckey_glass(x_arr[ii], X_tau, n)
            if np.sign(val) != currency_sign:
                count += 1
                currency_sign = -currency_sign

        matrix[i][j] = 1 if count > 3 else 0

extent = [0, 0.5, 0, 0.5]
# extent = [x_min , x_max, y_min , y_max]

_, ax = plt.subplots()

image = ax.imshow(
    matrix, interpolation="nearest", origin="lower", extent=extent, aspect="auto"
)

plt.show()
