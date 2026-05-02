import matplotlib.pyplot as plt
import numpy as np

from .ode.integrators import euler_delay

n_list = np.arange(0, 0.5, 0.01)
τ_list = np.arange(0, 0.5, 0.01)
ts = np.arange(0, 10, 0.01)
L, Vmax = 6, 16


def mckey_glass(X, X_τ, n):
    return L - (Vmax * X_τ**n) / (1 + X_τ**n) * X


def oscillation(X_init, n, τ, period=len(ts), step_size=0.01):
    # integrate using shared delay integrator
    x_arr = euler_delay(
        lambda X, X_tau, n: mckey_glass(X, X_tau, n),
        X_init,
        step_size,
        period,
        τ,
        history_value=0.5,
        n=n,
    )

    count = 0
    currency_sign = -1
    delay_steps = int(round(τ / step_size))

    for i in range(period):
        if i * step_size <= τ or i - delay_steps < 0:
            X_tau = 0.5
        else:
            X_tau = x_arr[i - delay_steps]

        val = mckey_glass(x_arr[i], X_tau, n)
        if np.sign(val) != currency_sign:
            count += 1
            currency_sign = -currency_sign

    return 1 if count > 3 else 0


matrix = np.zeros((len(n_list), len(τ_list)))

for i, n in enumerate(n_list):
    for j, τ in enumerate(τ_list):
        matrix[i][j] = oscillation(2, n, τ)

extent = [0, 0.5, 0, 0.5]
# extent = [x_min , x_max, y_min , y_max]

_, ax = plt.subplots()

image = ax.imshow(
    matrix, interpolation="nearest", origin="lower", extent=extent, aspect="auto"
)

plt.show()
