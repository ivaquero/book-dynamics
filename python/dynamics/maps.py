import numpy as np

from .attractors import logistic_map


def cobweb_points(x_init, r, steps):
    """Return the sequence of iterates for the cobweb (useful for plotting separately)."""
    X = [x_init]
    for _ in range(steps - 1):
        X.append(logistic_map(X[-1], r))
    return X


def iterate_map_2d(map_func, x0, n_steps, *args, **kwargs):
    """Iterate a 2D map function `map_func(state, *args, **kwargs)`.

    Returns two lists `(X, Y)` of length `n_steps` containing iterates.
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
        (h1, h2) Lyapunov exponents.
    """
    x, y = initial_x, initial_y
    vec1 = [1, 0]
    vec2 = [0, 1]

    for i in range(1, iterations + 1):
        # Henon map iteration
        x = 1 - a * x**2 + y
        y = b * x

        # Jacobian matrix
        J = np.array([[-2 * a * x, 1], [b, 0]])

        # Apply Jacobian to vectors
        vec1 = J @ vec1
        vec2 = J @ vec2

        # Gram-Schmidt orthogonalization
        dotprod_1 = vec1 @ vec1
        dotprod_2 = vec1 @ vec2
        vec2 = vec2 - np.multiply((dotprod_2 / dotprod_1), vec1)

        # Calculate lengths and area
        length_v1 = np.sqrt(dotprod_1)
        area = np.multiply(vec1[0], vec2[1]) - np.multiply(vec1[1], vec2[0])

        # Compute Lyapunov exponents
        h1 = np.log(length_v1) / i
        h2 = np.log(area) / i - h1

    return h1, h2


def draw_cobweb(ax, steps, x_init, r):
    """Draw cobweb plot on the given axes."""
    x, y = [x_init], [0]
    for _ in range(1, steps):
        x.append(x[-1])
        y.append(logistic_map(x[-1], r))
        x.append(y[-1])
        y.append(y[-1])
    ax.plot(x, y, color="blue")
