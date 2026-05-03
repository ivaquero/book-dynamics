"""Bifurcation analysis functions.

This module contains functions for analyzing bifurcations and stability
in dynamical systems, including logistic, budworm, and other models.
"""

import numpy as np
from sympy import symbols
from sympy.solvers import solve


def logistic(X, h, a):
    """Logistic growth with harvesting.

    Parameters
    ----------
    X : float
        Population size
    h : float
        Harvesting rate
    a : float
        Half-saturation constant

    Returns
    -------
    float
        Growth rate
    """
    return X * (1 - X) - h * X / (a + X)


def budworm(X, k, r):
    """Budworm population model.

    Parameters
    ----------
    X : float
        Population size
    k : float
        Carrying capacity
    r : float
        Growth rate

    Returns
    -------
    float
        Growth rate
    """
    return r * X * (1 - X / k) - (X**2) / (1 + X**2)


def number_track(H, A):
    """Count number of real roots of logistic-like equation over grids H x A.

    Parameters
    ----------
    H : array-like
        Harvesting rate values
    A : array-like
        Half-saturation constant values

    Returns
    -------
    list
        Matrix-like structure with number of roots for each (H, A) pair
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

    Parameters
    ----------
    rs : array-like
        Growth rate values
    ks : array-like
        Carrying capacity values

    Returns
    -------
    tuple
        (stable_points, unstable_points) where each is a list of three lists
        [ks, rs, x_values]
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
    """Hopf bifurcation normal form.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : array-like
        State vector [x, y]
    mu : float, optional
        Bifurcation parameter, by default 1

    Returns
    -------
    list
        Derivatives [dx/dt, dy/dt]
    """
    x, y = z
    return [y + mu * x - x * y**2, mu * y - x - y**3]


def snic(t, z, mu=1):
    """Saddle-node on invariant circle bifurcation normal form.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : array-like
        State vector [x, y]
    mu : float, optional
        Bifurcation parameter, by default 1

    Returns
    -------
    list
        Derivatives [dx/dt, dy/dt]
    """
    x, y = z
    return [
        x * (1 - x**2 - y**2) - y * (1 + mu + x),
        y * (1 - x**2 - y**2) + x * (1 + mu + x),
    ]


def opinion(X, a):
    """Opinion dynamics model.

    Parameters
    ----------
    X : float
        Opinion value
    a : float
        Influence parameter

    Returns
    -------
    float
        Opinion change rate
    """
    return (1 - X) * np.exp(a * X) - (1 + X) * np.exp(-a * X)


def lac(X, a, r):
    """Lac operon model.

    Parameters
    ----------
    X : float
        Lactose concentration
    a : float
        Parameter
    r : float
        Parameter

    Returns
    -------
    float
        Change rate
    """
    return (a + X**2) / (1 + X**2) - r * X


def allee(X, a):
    """Allee effect model.

    Parameters
    ----------
    X : float
        Population size
    a : float
        Allee threshold

    Returns
    -------
    float
        Growth rate
    """
    return 0.1 * X * (1 - X / 1000) * (X / a - 1)


def stablity(
    X_init, func, *func_args, perturbation=0.01, time_interval=0.01, iterations=100
):
    """Test stability of equilibrium point.

    Parameters
    ----------
    X_init : float
        Equilibrium point to test
    func : callable
        Function to test
    *func_args
        Arguments passed to func
    perturbation : float, optional
        Initial perturbation size, by default 0.01
    time_interval : float, optional
        Time step, by default 0.01
    iterations : int, optional
        Number of iterations, by default 100

    Returns
    -------
    bool
        True if stable, False if unstable
    """
    X = X_init + perturbation
    for _ in range(iterations):
        X += time_interval * func(X, *func_args)
    return abs(X - X_init) <= perturbation


def pillar(X, Y, vec):
    """Extract points at regular intervals for plotting.

    Parameters
    ----------
    X : array-like
        x-coordinates
    Y : array-like
        y-coordinates
    vec : int
        Sampling interval

    Returns
    -------
    tuple
        (x_sampled, y_sampled, t_sampled) coordinates
    """
    x, y = [], []
    t = []
    for i in range(100):
        x.append(X[i * vec])
        y.append(Y[i * vec])
        t.append(i * vec)
    return x, y, t
