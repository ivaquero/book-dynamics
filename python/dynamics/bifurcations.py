import numpy as np


def hopf(t, z, mu=1):
    x, y = z
    return [y + mu * x - x * y**2, mu * y - x - y**3]


def snic(t, z, mu=1):
    x, y = z
    return [
        x * (1 - x**2 - y**2) - y * (1 + mu + x),
        y * (1 - x**2 - y**2) + x * (1 + mu + x),
    ]


def opinion(X, a):
    return (1 - X) * np.exp(a * X) - (1 + X) * np.exp(-a * X)


def lac(X, a, r):
    return (a + X**2) / (1 + X**2) - r * X


def allee(X, a):
    return 0.1 * X * (1 - X / 1000) * (X / a - 1)


def stablity(
    X_init, func, *func_args, perturbation=0.01, time_interval=0.01, iterations=100
):
    X = X_init + perturbation
    for _ in range(iterations):
        X += time_interval * func(X, *func_args)
    return abs(X - X_init) <= perturbation


def arrows_param(
    ax, param, X_list, func, head_width=0.02, head_length=0.5, color="black"
):
    ax.vlines(param, min(X_list) - 1, max(X_list) + 1, color=color)
    for x in X_list:
        points_at = func(x, param)
        ax.arrow(
            param,
            x,
            0,
            points_at,
            head_width=head_width,
            head_length=head_length,
            color=color,
        )


def arrows_with_r(
    ax, r_val, X_list, func, *func_args, head_width=0.02, head_length=0.5, color="black"
):
    ax.vlines(r_val, min(X_list) - 1, max(X_list) + 1, color=color)
    for x in X_list:
        points_at = func(x, *func_args, r_val)
        ax.arrow(
            r_val,
            x,
            0,
            points_at,
            head_width=head_width,
            head_length=head_length,
            color=color,
        )
