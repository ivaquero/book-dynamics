import numpy as np
from scipy.integrate import solve_ivp


def plot_phase(func, t_span, z, ax):
    sol = solve_ivp(func, t_span, z, dense_output=True)
    t = np.linspace(t_span[0], t_span[1], int((t_span[1] - t_span[0]) * 10))
    X1 = sol.sol(t).T

    ax.plot(X1[:, 0], X1[:, 1], "r-", lw=0.2)
    ax.set(xlabel="x", ylabel="y", title="Phase portrait")


def plot_poincare(func, t_span, z, n_period, ax):
    sol = solve_ivp(func, t_span, z, dense_output=True)
    t = np.linspace(
        t_span[0], t_span[1] * n_period, int((t_span[1] - t_span[0]) * n_period)
    )
    X2 = sol.sol(t).T

    x = [X2[int(t_span[1] * i), 0] for i in range(int(t_span[1]))]
    y = [X2[int(t_span[1] * i), 1] for i in range(int(t_span[1]))]

    ax.plot(x, y, "b.", ms=2)
    ax.set(xlabel="x", ylabel="y", title="Poincaré section")


def make_param_anim(
    ax, compute_xy_for_param, xlim=None, ylim=None, xlabel="x", ylabel="y"
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
        if xlim is not None:
            ax.set(xlim=xlim)
        if ylim is not None:
            ax.set(ylim=ylim)
        ax.set(xlabel=xlabel, ylabel=ylabel)
        return (line,)

    return init, animate


def make_multi_traj_anim(
    ax, compute_trajs_for_param, xlim=None, ylim=None, xlabel="x", ylabel="y"
):
    """Create an animate callable that clears the axes and plots multiple trajectories for a parameter."""

    def animate(param):
        ax.clear()
        if xlim is not None:
            ax.set(xlim=xlim)
        if ylim is not None:
            ax.set(ylim=ylim)
        ax.set(xlabel=xlabel, ylabel=ylabel)

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
