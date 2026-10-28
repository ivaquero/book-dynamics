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


def make_param_anim(
    ax, compute_xy_for_param, xlim=None, ylim=None, xlabel=None, ylabel=None
):
    """Create init and animate callables for a parameterized curve.

    - `compute_xy_for_param(param)` should return (x_array, y_array).
    - Returned `init()` clears the line; `animate(param)` sets data and returns the line tuple.
    """

    (line,) = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return (line,)

    def animate(param):
        x, y = compute_xy_for_param(param)
        line.set_data(x, y)
        ax.set(xlim=xlim, ylim=ylim, xlabel=xlabel, ylabel=ylabel)

        return (line,)

    return init, animate


def make_multi_traj_anim(
    ax, compute_trajs_for_param, xlim=None, ylim=None, xlabel=None, ylabel=None
):
    """Create an animate callable that clears the axes and plots multiple trajectories for a parameter."""

    def animate(param):
        ax.clear()
        ax.set(xlim=xlim, ylim=ylim, xlabel=xlabel, ylabel=ylabel)

        trajs = compute_trajs_for_param(param)
        for X in trajs:
            ax.plot(X[:, 0], X[:, 1])

    return animate


def time_series_from_pulsed_factory(
    start, stop, I_ext_value, ts, z0, integrator=None, factory_func=None
):
    """Integrate a pulsed factory over time grid `ts` using `integrator`.

    - `integrator` defaults to `dynamics.integrators.euler_fixed` and must accept
      signature `integrator(func, z0, step_size, n_steps)`.
    - Returns `(traj, times)` where `traj` is array n_steps x dim and `times` equals `ts`.
    """

    if integrator is None:
        from .integrators import euler_fixed as _default_integrator

        integrator = _default_integrator

    # delayed import to avoid circulars; pulsed factory is in attractors
    from .attractors import pulsed_FHN_factory

    if factory_func is None:
        factory_func = pulsed_FHN_factory

    func = factory_func(start, stop, I_ext_value)
    step = ts[1] - ts[0]
    traj, times = integrator(func, z0, step, len(ts))
    return traj, times


def arrows_with_r(
    ax, r_val, X_list, func, *func_args, head_width=0.02, head_length=0.5, color="black"
):
    """Draw vertical arrows along a vertical line at `r_val` for each point in `X_list`."""
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


def draw_cobweb(ax, steps, x_init, r, color="b"):
    """Draw a cobweb diagram on the given axis.

    - `ax` is a matplotlib Axes instance.
    - `steps` number of cobweb iterations to draw.
    - `x_init` initial x value.
    - `r` logistic map parameter.
    """
    from .attractors import logistic_map

    X, Y = [], []
    X.append(x_init)
    Y.append(0)
    for _ in range(steps):
        # compute next point and draw the two segments of the cobweb
        y_next = logistic_map(X[-1], r)
        X.append(X[-1])
        Y.append(y_next)
        ax.plot(X[-2:], Y[-2:], color=color)
        X.append(y_next)
        Y.append(y_next)
        ax.plot(X[-2:], Y[-2:], color=color)


def plot_hpg_3d_with_vectors(ax, x, y, z, dx, dy, dz, **plot_kwargs):
    """Plot HPG 3D trajectory with vector field.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        3D axes instance for plotting.
    x, y, z : array-like
        Arrays of trajectory coordinates.
    dx, dy, dz : array-like
        Arrays of derivative components for vector field.
    **plot_kwargs : dict
        Additional keyword arguments passed to ax.plot().

    Returns
    -------
    matplotlib.lines.Line2D
        The plotted line object.
    """
    # Add quiver arrows at intervals
    for i in range(100, len(x), 400):
        ax.quiver(x[i], y[i], z[i], dx[i], dy[i], dz[i], color="red")

    line = ax.plot(x, y, z, label="Limit Cycle of HPG", **plot_kwargs)
    ax.set(xlabel="x", ylabel="y", zlabel="z")
    return line


def plot_hpg2_phase_portraits(ax, trajectories, **plot_kwargs):
    """Plot HPG2 phase portraits for multiple trajectories.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        2D axes instance for plotting.
    trajectories : list
        List of (x_traj, y_traj) tuples.
    **plot_kwargs : dict
        Additional keyword arguments passed to ax.plot().
    """
    for x_traj, y_traj in trajectories:
        ax.plot(x_traj, y_traj, **plot_kwargs)


def plot_poincare_section(ax, X, **plot_kwargs):
    """Plot Poincare section on given axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        2D axes instance for plotting.
    X : numpy.ndarray
        Trajectory array of shape (n_points, 2) containing [x, y] coordinates.
    **plot_kwargs : dict
        Additional keyword arguments passed to ax.plot().

    Returns
    -------
    matplotlib.lines.Line2D
        The plotted line object.
    """
    line = ax.plot(X[:, 0], X[:, 1], "r-", **plot_kwargs)
    ax.set(xlabel="x", ylabel="y", xlim=(-0.5, 1.5), ylim=(-0.5, 0.5))
    return line
