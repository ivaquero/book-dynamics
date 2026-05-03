import numpy as np


def euler(t, tmax, y, func_dx, step=1.0):
    ys = []
    while t < tmax:
        y = y + step * dx(t, y)
        ys.append(y)
        t += step
    return ys


def dx(t, y):
    return y


def euler_fixed(func, z0, step_size, n_steps, t0=0.0):
    """Simple fixed-step explicit Euler integrator.

    - `func` may have signature `f(t, z)` or `f(z)`.
    - `z0` is an iterable initial state (scalar or vector).
    - Returns `(traj, times)` where `traj` is an array shape (n_steps, dim).
    """
    z = np.asarray(z0, dtype=float)
    dim = z.size if z.ndim > 0 else 1
    traj = np.empty((n_steps, dim))
    times = np.empty(n_steps)

    t = float(t0)
    for i in range(n_steps):
        traj[i] = z
        times[i] = t
        try:
            dz = func(t, z)
        except TypeError:
            dz = func(z)
        dz = np.asarray(dz, dtype=float)
        z = z + step_size * dz
        t += step_size

    return traj, times


def euler_1d(func, x0, step_size, n_steps, t0=0.0):
    """Convenience wrapper for scalar state."""
    traj, times = euler_fixed(func, [x0], step_size, n_steps, t0=t0)
    return traj.ravel(), times


def euler_delay(func, x0, step_size, n_steps, tau, history_value=0.5, *args, **kwargs):
    """Simple explicit Euler integrator with a fixed delay `tau` for scalar state.

    - `func(x, x_tau, *args, **kwargs)` should return dx/dt given current x and delayed x_tau.
    - `x0` initial scalar state at t=0.
    - `history_value` is used for t <= tau as the delayed state.
    Returns array of states length `n_steps` and implicit times can be inferred as `i*step_size`.
    """
    x_arr = np.empty(n_steps)
    x = float(x0)
    for i in range(n_steps):
        x_arr[i] = x
        t = i * step_size
        if t <= tau:
            x_tau = history_value
        else:
            idx = i - round(tau / step_size)
            x_tau = history_value if idx < 0 else x_arr[idx]

        dx = func(x, x_tau, *args, **kwargs)
        x = x + step_size * dx

    return x_arr


def runge_kutta4(y, x, dx, f):
    """computes 4th order Runge-Kutta for dy/dx."""
    k1 = dx * f(y, x)
    k2 = dx * f(y + 0.5 * k1, x + 0.5 * dx)
    k3 = dx * f(y + 0.5 * k2, x + 0.5 * dx)
    k4 = dx * f(y + k3, x + dx)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
