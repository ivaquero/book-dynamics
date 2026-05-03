"""Map iteration and analysis functions.

This module contains functions for iterating discrete maps and computing
dynamical properties like Lyapunov exponents.
"""

import numpy as np

from .attractors import logistic_map


def cobweb_points(x_init, r, steps):
    """Return the sequence of iterates for the cobweb (useful for plotting separately).

    Parameters
    ----------
    x_init : float
        Initial condition
    r : float
        Logistic map parameter
    steps : int
        Number of iterations

    Returns
    -------
    list
        Sequence of iterates
    """
    X = [x_init]
    for _ in range(steps - 1):
        X.append(logistic_map(X[-1], r))
    return X


def iterate_map_2d(map_func, x0, n_steps, *args, **kwargs):
    """Iterate a 2D map function `map_func(state, *args, **kwargs)`.

    Parameters
    ----------
    map_func : callable
        Map function to iterate
    x0 : array-like
        Initial condition [x, y]
    n_steps : int
        Number of iterations
    *args, **kwargs
        Additional arguments passed to map_func

    Returns
    -------
    tuple
        Two lists (X, Y) of length n_steps containing iterates
    """
    X = []
    Y = []
    state = list(x0)
    for _ in range(n_steps):
        xn, yn = map_func(state, *args, **kwargs)
        X.append(xn)
        Y.append(yn)
        state = [xn, yn]
    return X, Y


def compute_henon_lyapunov_exponents(
    a=1.2, b=0.4, iterations=490, initial_x=0.0, initial_y=0.0
):
    """Compute Lyapunov exponents for Henon map using QR decomposition method.

    Parameters
    ----------
    a : float, optional
        Henon map parameter. Defaults to 1.2.
    b : float, optional
        Henon map parameter. Defaults to 0.4.
    iterations : int, optional
        Number of iterations for convergence. Defaults to 490.
    initial_x : float, optional
        Initial x coordinate. Defaults to 0.0.
    initial_y : float, optional
        Initial y coordinate. Defaults to 0.0.

    Returns
    -------
    tuple
        (lyapunov_exp_1, lyapunov_exp_2) - the two Lyapunov exponents
    """
    from .attractors import henon

    # Initialize state
    x, y = initial_x, initial_y

    # Initialize tangent vectors (identity matrix)
    u1, u2 = np.array([1.0, 0.0]), np.array([0.0, 1.0])

    # Initialize Lyapunov exponent sums
    lyap_sum1, lyap_sum2 = 0.0, 0.0

    for _ in range(iterations):
        # Iterate the map
        x_new, y_new = henon([x, y], a=a, b=b)

        # Jacobian matrix of Henon map
        J = np.array([[-2 * a * x, 1], [b, 0]])

        # Apply Jacobian to tangent vectors
        u1_new = J @ u1
        u2_new = J @ u2

        # Gram-Schmidt orthogonalization
        # Normalize u1
        norm1 = np.linalg.norm(u1_new)
        u1_new = u1_new / norm1

        # Orthogonalize u2 against u1
        u2_new = u2_new - np.dot(u2_new, u1_new) * u1_new
        norm2 = np.linalg.norm(u2_new)
        u2_new = u2_new / norm2

        # Accumulate Lyapunov exponents
        lyap_sum1 += np.log(norm1)
        lyap_sum2 += np.log(norm2)

        # Update state and vectors
        x, y = x_new, y_new
        u1, u2 = u1_new, u2_new

    # Normalize by number of iterations
    lyap_exp_1 = lyap_sum1 / iterations
    lyap_exp_2 = lyap_sum2 / iterations

    return lyap_exp_1, lyap_exp_2
