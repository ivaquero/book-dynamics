"""Visualization utilities for dynamical systems.

This module contains functions for visualizing vector fields, nullclines,
phase portraits, Poincaré sections, and other properties of dynamical systems.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def arrows(ax, x, y, a=1, step=50, head_width=0.05, scale=30, color="black"):
    """Draw arrows for vector field visualization.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to draw arrows on
    x : array-like
        x-coordinates of arrow positions
    y : array-like
        y-coordinates of arrow positions
    a : float, optional
        System parameter for clarinet system, by default 1
    step : int, optional
        Step size for arrow placement, by default 50
    head_width : float, optional
        Arrow head width, by default 0.05
    scale : int, optional
        Arrow scaling factor, by default 30
    color : str, optional
        Arrow color, by default "black"
    """
    from .systems import clarinet

    dx, dy = [], []
    for x_, y_ in zip(x, y, strict=True):
        ver = clarinet(t=0, z=[x_, y_], a=a)
        dx.append(ver[0])
        dy.append(ver[1])
    m = np.hypot(dx, dy)
    for i in range(1, len(x), step):
        ax.arrow(
            x[i],
            y[i],
            dx[i] / m[i] / scale,
            dy[i] / m[i] / scale,
            head_width=head_width,
            color=color,
        )


def fhn_nullclines(V, theta=0.1, gamma_slope=2.0):
    """Compute FHN nullclines for a given range or array of V values.

    - `V` may be a numpy array.
    - Returns tuple `(W_nullcline, w_prime)` for plotting.

    Parameters
    ----------
    V : array-like
        Voltage values for nullcline calculation
    theta : float, optional
        Threshold parameter, by default 0.1
    gamma_slope : float, optional
        Slope parameter for w-nullcline, by default 2.0

    Returns
    -------
    tuple
        (W_nullcline, w_prime) arrays for plotting
    """
    V = np.asarray(V)
    W = V * (1 - V) * (V - theta)
    w_prime = gamma_slope * V
    return W, w_prime


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
