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
