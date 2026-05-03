"""Plotting utilities for dynamical systems.

This module contains functions for creating various types of plots
for dynamical systems analysis, including phase portraits,
Poincaré sections, and vector fields.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def plot_phase(ax, func, t_span, z):
    """Plot phase portrait of a dynamical system.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to plot on
    func : callable
        System function f(t, z)
    t_span : list
        Time span [t_start, t_end]
    z : array-like
        Initial condition
    """
    sol = solve_ivp(func, t_span, z, dense_output=True)
    t = np.linspace(t_span[0], t_span[1], int((t_span[1] - t_span[0]) * 10))
    X1 = sol.sol(t).T

    ax.plot(X1[:, 0], X1[:, 1], "r-", lw=0.2)
    ax.set(title="Phase portrait")


def plot_poincare(ax, func, t_span, z, n_period):
    """Plot Poincaré section of a dynamical system.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to plot on
    func : callable
        System function f(t, z)
    t_span : list
        Time span [t_start, t_end]
    z : array-like
        Initial condition
    n_period : int
        Number of periods to sample
    """
    sol = solve_ivp(func, t_span, z, dense_output=True)
    t = np.linspace(
        t_span[0], t_span[1] * n_period, int((t_span[1] - t_span[0]) * n_period)
    )
    X2 = sol.sol(t).T

    x = [X2[int(t_span[1] * i), 0] for i in range(int(t_span[1]))]
    y = [X2[int(t_span[1] * i), 1] for i in range(int(t_span[1]))]

    ax.plot(x, y, "b.", ms=2)
    ax.set(title="Poincaré section")


def gen_mesh(xy_range, n_points):
    """Generate mesh grid for vector field plotting.

    Parameters
    ----------
    xy_range : list
        Range [xmin, xmax, ymin, ymax]
    n_points : int
        Number of points in each dimension

    Returns
    -------
    tuple
        X, Y meshgrid arrays
    """
    X, Y = np.meshgrid(
        np.linspace(xy_range[0], xy_range[1], n_points),
        np.linspace(xy_range[2], xy_range[3], n_points),
    )
    return X, Y


def vector_field(ax, X, Y, U, V):
    """Plot vector field on given axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to plot on
    X : array-like
        x-coordinates of grid points
    Y : array-like
        y-coordinates of grid points
    U : array-like
        x-components of vectors
    V : array-like
        y-components of vectors
    """
    M = np.hypot(U, V)  # Norm of the growth rate
    M[M == 0] = 1  # Avoid zero division errors
    U /= M  # Normalize each vector_field
    V /= M
    ax.quiver(X, Y, U, V, M, pivot="mid", cmap=plt.cm.jet)


def derivatives(t, z, a, b, c, d):
    """Linear system derivatives for testing.

    Parameters
    ----------
    t : float
        Time (not used in autonomous system)
    z : array-like
        State vector [x, y]
    a, b, c, d : float
        Matrix coefficients

    Returns
    -------
    list
        Derivatives [dx/dt, dy/dt]
    """
    x, y = z
    u = a * x + b * y
    v = c * x + d * y
    return [u, v]
