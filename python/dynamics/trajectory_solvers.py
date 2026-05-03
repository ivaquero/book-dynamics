"""Trajectory solvers for dynamical systems.

This module contains functions for solving trajectories of various dynamical systems.
"""

import numpy as np
from scipy.integrate import solve_ivp


def solve_lorenz_trajectory(xyz_init, t_span, params=(10, 2.667, 28), n_points=10000):
    """Solve Lorenz trajectory for given initial condition and parameters.

    Parameters
    ----------
    xyz_init : tuple
        Initial [x, y, z] conditions.
    t_span : list
        Time span [t_start, t_end].
    params : tuple, optional
        Lorenz parameters (sigma, beta, rho). Defaults to (10, 2.667, 28).
    n_points : int, optional
        Number of time points. Defaults to 10000.

    Returns
    -------
    tuple
        (x, y, z, t) arrays of trajectory coordinates and time points.
    """
    from .systems import lorenz

    σ, β, ρ = params
    sol = solve_ivp(lorenz, t_span, xyz_init, args=(σ, β, ρ), dense_output=True)
    t = np.linspace(t_span[0], t_span[1], n_points)
    x, y, z = sol.sol(t)
    return x, y, z, t


def solve_rossler_trajectory(initial_conditions=None, dt=0.01, step_count=50000):
    """Solve Rossler attractor trajectory using Euler integration.

    Parameters
    ----------
    initial_conditions : list, optional
        Initial [x, y, z] conditions. Defaults to [1.0, 1.0, 1.0].
    dt : float, optional
        Time step size. Defaults to 0.01.
    step_count : int, optional
        Number of integration steps. Defaults to 50000.

    Returns
    -------
    tuple
        (trajectory, times) where trajectory is array of shape (step_count, 3)
        and times is array of integration time points.
    """
    if initial_conditions is None:
        initial_conditions = [1.0, 1.0, 1.0]

    from .integrators import euler_fixed
    from .systems import rossler

    traj, times = euler_fixed(rossler, initial_conditions, dt, step_count)
    return traj, times


def solve_hpg_trajectory(initial_conditions, step_size=0.1, period=1000):
    """Solve HPG system trajectory.

    Parameters
    ----------
    initial_conditions : list
        Initial [P, H, G] conditions.
    step_size : float, optional
        Time step size. Defaults to 0.1.
    period : int, optional
        Number of integration steps. Defaults to 1000.

    Returns
    -------
    tuple
        (trajectory, times) where trajectory is array of shape (period, 3).
    """
    from .integrators import euler_fixed
    from .systems import HPG

    traj, times = euler_fixed(HPG, initial_conditions, step_size, period)
    return traj, times


def compute_hpg_derivatives(traj):
    """Compute HPG derivatives for vector field visualization.

    Parameters
    ----------
    traj : numpy.ndarray
        Trajectory array of shape (n_points, 3) containing [P, H, G] coordinates.

    Returns
    -------
    tuple
        (dP, dH, dG) arrays of derivatives.
    """
    from .systems import HPG

    derivs = np.array([HPG(t=0, init=row) for row in traj])
    return derivs[:, 0], derivs[:, 1], derivs[:, 2]


def prepare_hpg_initial_conditions():
    """Prepare initial conditions for HPG system.

    Returns
    -------
    list
        Default initial conditions [P, H, G] = [1, 0.2, 2].
    """
    return [1, 0.2, 2]


def prepare_hpg2_initial_conditions(n_angles=5, outer_radius=1.5, inner_radius=0.05):
    """Prepare initial conditions for HPG2 system.

    Parameters
    ----------
    n_angles : int, optional
        Number of angular positions. Defaults to 5.
    outer_radius : float, optional
        Outer radius for initial conditions. Defaults to 1.5.
    inner_radius : float, optional
        Inner radius for initial conditions. Defaults to 0.05.

    Returns
    -------
    list
        List of [H, G] coordinate pairs for multiple initial conditions.
    """
    θs = np.linspace(0, 2 * np.pi, n_angles)
    coordinates = []

    for θ in θs:
        coordinates.extend(
            [
                [outer_radius * np.cos(θ), outer_radius * np.sin(θ)],
                [inner_radius * np.cos(θ), inner_radius * np.sin(θ)],
            ]
        )

    return coordinates


def solve_hpg2_trajectories(coordinates, t_span, t):
    """Solve HPG2 trajectories for multiple initial conditions.

    Parameters
    ----------
    coordinates : list
        List of [H, G] initial condition pairs.
    t_span : list
        Time span [t_start, t_end].
    t : numpy.ndarray
        Array of time points for evaluation.

    Returns
    -------
    list
        List of (H_traj, G_traj) trajectory tuples.
    """
    from .systems import HPG2

    trajectories = []
    for coordinate in coordinates:
        h_i, g_i = coordinate
        sol = solve_ivp(HPG2, t_span, [h_i, g_i], dense_output=True)
        X = sol.sol(t).T
        trajectories.append((X[:, 0], X[:, 1]))
    return trajectories


def solve_poincare_trajectory(initial_conditions, t_span, n_points=10000):
    """Solve Poincare trajectory.

    Parameters
    ----------
    initial_conditions : list
        Initial [x, y] conditions.
    t_span : list
        Time span [t_start, t_end].
    n_points : int, optional
        Number of time points. Defaults to 10000.

    Returns
    -------
    numpy.ndarray
        Trajectory array of shape (n_points, 2).
    """
    from .systems import poincare_derivatives

    sol = solve_ivp(poincare_derivatives, t_span, initial_conditions, dense_output=True)
    t = np.linspace(t_span[0], t_span[1], n_points)
    return sol.sol(t).T
