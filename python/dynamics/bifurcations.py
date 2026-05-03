import numpy as np
from sympy import symbols
from sympy.solvers import solve


def logistic(X, h, a):
    return X * (1 - X) - h * X / (a + X)


def budworm(X, k, r):
    return r * X * (1 - X / k) - (X**2) / (1 + X**2)


def number_track(H, A):
    """Count number of real roots of logistic-like equation over grids H x A.

    Returns list-of-arrays (matrix-like) compatible with existing examples.
    """
    matrix = []
    X = symbols("X", real=True)
    for h in H:
        item = np.zeros(len(A))
        for ind, a in enumerate(A):
            sols = solve(X * (1 - X) - h * X / (a + X), X)
            item[ind] = len(sols)
        matrix.append(item)
    return matrix


def track_in_3D(rs, ks):
    """Return stable/unstable equilibria for budworm model over rs x ks grids.

    Returns (stable_points, unstable_points) where each is a list of three lists
    [ks, rs, x_values].
    """
    X = symbols("X", real=True)
    stable_points = [[], [], []]
    unstable_points = [[], [], []]
    for r in rs:
        for k in ks:
            equilibria = solve(r * (1 - X / k) - X / (1 + X**2), X)
            equilibria_vals = [float(e) for e in equilibria] if equilibria else [0.0]
            for x in equilibria_vals:
                if stablity(x, budworm, k, r):
                    stable_points[0].append(k)
                    stable_points[1].append(r)
                    stable_points[2].append(x)
                else:
                    unstable_points[0].append(k)
                    unstable_points[1].append(r)
                    unstable_points[2].append(x)

    return stable_points, unstable_points


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


def pillar(X, Y, vec):
    x, y = [], []
    t = []
    for i in range(100):
        x.append(X[i * vec])
        y.append(Y[i * vec])
        t.append(i * vec)
    return x, y, t
