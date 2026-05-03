"""Visualization utilities for dynamical systems.

This module contains functions for visualizing vector fields, nullclines,
and other properties of dynamical systems.
"""

import numpy as np


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
