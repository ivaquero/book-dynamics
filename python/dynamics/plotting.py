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
            from ..ode.integrators import euler_fixed as _default_integrator

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
