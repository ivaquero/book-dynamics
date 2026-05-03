import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .attractors import logistic_map


def plot_phase(ax, func, t_span, z):
    sol = solve_ivp(func, t_span, z, dense_output=True)
    t = np.linspace(t_span[0], t_span[1], int((t_span[1] - t_span[0]) * 10))
    X1 = sol.sol(t).T

    ax.plot(X1[:, 0], X1[:, 1], "r-", lw=0.2)
    ax.set(title="Phase portrait")


def plot_poincare(ax, func, t_span, z, n_period):
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
    X, Y = np.meshgrid(
        np.linspace(xy_range[0], xy_range[1], n_points),
        np.linspace(xy_range[2], xy_range[3], n_points),
    )
    return X, Y


def vector_field(ax, X, Y, U, V):
    M = np.hypot(U, V)  # Norm of the growth rate
    M[M == 0] = 1  # Avoid zero division errors
    U /= M  # Normalize each vector_field
    V /= M
    ax.quiver(X, Y, U, V, M, pivot="mid", cmap=plt.cm.jet)


def derivatives(t, z, a, b, c, d):
    x, y = z
    u = a * x + b * y
    v = c * x + d * y
    return [u, v]


def plot_vector_field(
    ax,
    x_start,
    x_end,
    y_start,
    y_end,
    vector_function=None,
    n_points=5000,
    title=None,
    arrow_length=1,
    arrow_scale=1,
):
    """
    Visualize a 2D vector field using quiver plot.

    Parameters:
    - x_start, x_end: Start and end points for the x-axis
    - y_start, y_end: Start and end points for the y-axis
    - n_points: Number of points for grid resolution
    - title: Title of the plot (optional)
    - arrow_length: Length of the arrows (relative scaling factor)
    - arrow_scale: Scale for adjusting the density of arrows
    """

    # Create grid points
    x = np.arange(x_start, x_end, n_points)
    y = np.arange(y_start, y_end, n_points)
    X, Y = np.meshgrid(x, y)

    try:
        U, V = vector_function(X, Y)
    except NameError:
        raise ValueError(
            "Please provide a vector field function similar to the examples above."
        ) from None

    # Scale arrows appropriately to prevent overlap
    scale = arrow_length / ((X.max() - X.min()) / 2.0) / arrow_scale

    ax.quiver(X, Y, U, V, units="x", scale=scale, cmap=plt.cm.jet)
    ax.set(
        title=title if title else "Vector Field Visualization", xlabel="X", ylabel="Y"
    )
    ax.grid(True)


def make_param_anim(ax, compute_xy_for_param, xlim=None, ylim=None):
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
        if xlim is not None:
            ax.set(xlim=xlim)
        if ylim is not None:
            ax.set(ylim=ylim)

        return (line,)

    return init, animate


def make_multi_traj_anim(ax, compute_trajs_for_param, xlim=None, ylim=None):
    """Create an animate callable that clears the axes and plots multiple trajectories for a parameter."""

    def animate(param):
        ax.clear()
        if xlim is not None:
            ax.set(xlim=xlim)
        if ylim is not None:
            ax.set(ylim=ylim)

        trajs = compute_trajs_for_param(param)
        for X in trajs:
            ax.plot(X[:, 0], X[:, 1])

    return animate

    def time_series_from_pulsed_factory(
        start, stop, I_ext_value, ts, z0, integrator=None, factory_func=None
    ):
        """Integrate a pulsed factory over time grid `ts` using `integrator`.

        - `integrator` defaults to `ode.integrators.euler_fixed` and must accept
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

    return None


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


def draw_cobweb(ax, steps, x_init, r, color="b"):
    """Draw a cobweb diagram on the given axis.

    - `ax` is a matplotlib Axes instance.
    - `steps` number of cobweb iterations to draw.
    - `x_init` initial x value.
    - `r` logistic map parameter.
    """
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


def plot_rossler_attractor(ax, traj, **plot_kwargs):
    """Plot Rossler attractor on given axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        3D axes instance for plotting.
    traj : numpy.ndarray
        Trajectory array of shape (n_points, 3) containing [x, y, z] coordinates.
    **plot_kwargs : dict
        Additional keyword arguments passed to ax.plot().

    Returns
    -------
    matplotlib.lines.Line2D
        The plotted line object.
    """
    xs = traj[:, 0]
    ys = traj[:, 1]
    zs = traj[:, 2]

    line = ax.plot(xs, ys, zs, lw=0.5, **plot_kwargs)
    ax.set(xlabel="x", ylabel="y", zlabel="z", title="Rossler Attractor")
    return line


def plot_lorenz_3d(ax, x, y, z, **plot_kwargs):
    """Plot Lorenz attractor in 3D on given axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        3D axes instance for plotting.
    x, y, z : array-like
        Arrays of x, y, z coordinates.
    **plot_kwargs : dict
        Additional keyword arguments passed to ax.plot().

    Returns
    -------
    matplotlib.lines.Line2D
        The plotted line object.
    """
    return ax.plot(x, y, z, "b-", lw=0.5, **plot_kwargs)


def setup_lorenz_3d_plot(ax, title="Lorenz Attractor"):
    """Setup Lorenz 3D plot properties.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        3D axes instance.
    title : str, optional
        Plot title. Defaults to "Lorenz Attractor".
    """
    ax.set(xlabel="x", ylabel="y", zlabel="z", title=title)


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
