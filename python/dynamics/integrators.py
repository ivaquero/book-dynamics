"""Numerical integration utilities.

This module contains various numerical integrators for solving
differential equations, including Euler methods and Runge-Kutta.
"""

import numpy as np


def euler(t, tmax, y, func_dx, step=1.0):
    """Simple Euler integration (legacy function).

    Parameters
    ----------
    t : float
        Initial time
    tmax : float
        Maximum time
    y : float
        Initial value
    func_dx : callable
        Derivative function
    step : float, optional
        Time step, by default 1.0

    Returns
    -------
    list
        Solution values
    """
    ys = []
    while t < tmax:
        y = y + step * dx(t, y)
        ys.append(y)
        t += step
    return ys


def dx(t, y):
    """Test derivative function (legacy)."""
    return y


def euler_fixed(func, z0, step_size, n_steps, t0=0.0):
    """Simple fixed-step explicit Euler integrator.

    Parameters
    ----------
    func : callable
        Function to integrate. May have signature f(t, z) or f(z).
    z0 : array-like
        Initial state (scalar or vector)
    step_size : float
        Time step size
    n_steps : int
        Number of steps
    t0 : float, optional
        Initial time, by default 0.0

    Returns
    -------
    tuple
        (traj, times) where traj is array shape (n_steps, dim)
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
    """Convenience wrapper for scalar state.

    Parameters
    ----------
    func : callable
        Derivative function
    x0 : float
        Initial value
    step_size : float
        Time step size
    n_steps : int
        Number of steps
    t0 : float, optional
        Initial time, by default 0.0

    Returns
    -------
    tuple
        (traj, times) for scalar state
    """
    traj, times = euler_fixed(func, [x0], step_size, n_steps, t0=t0)
    return traj.ravel(), times


def euler_delay(func, x0, step_size, n_steps, tau, history_value=0.5, *args, **kwargs):
    """Simple explicit Euler integrator with a fixed delay.

    Parameters
    ----------
    func : callable
        Function with signature f(x, x_tau, *args, **kwargs)
    x0 : float
        Initial state
    step_size : float
        Time step size
    n_steps : int
        Number of steps
    tau : float
        Delay time
    history_value : float, optional
        Value for delayed state when t <= tau, by default 0.5
    *args, **kwargs
        Additional arguments passed to func

    Returns
    -------
    numpy.ndarray
        Array of states of length n_steps
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
    """Compute 4th order Runge-Kutta for dy/dx.

    Parameters
    ----------
    y : float
        Current y value
    x : float
        Current x value
    dx : float
        Step size
    f : callable
        Derivative function dy/dx = f(y, x)

    Returns
    -------
    float
        Next y value
    """
    k1 = dx * f(y, x)
    k2 = dx * f(y + 0.5 * k1, x + 0.5 * dx)
    k3 = dx * f(y + 0.5 * k2, x + 0.5 * dx)
    k4 = dx * f(y + k3, x + dx)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
