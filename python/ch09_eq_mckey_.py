import matplotlib.pyplot as plt
import numpy as np

n_list = np.arange(0, 0.5, 0.01)
τ_list = np.arange(0, 0.5, 0.01)
ts = np.arange(0, 10, 0.01)
L, Vmax = 6, 16


def mckey_glass(X, X_τ, n):
    return L - (Vmax * X_τ**n) / (1 + X_τ**n) * X


def oscillation(X_init, n, τ, period=len(ts), step_size=0.01):
    X = X_init
    x = []
    count = 0
    currency_sign = -1

    for i in range(period):
        x.append(X)
        X_τ = 0.5 if ts[i] <= τ else x[i - int(τ / step_size)]
        if np.sign(mckey_glass(x[-1], X_τ, n)) != currency_sign:
            count += 1
            currency_sign = -currency_sign
        X += step_size * mckey_glass(x[-1], X_τ, n)
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
