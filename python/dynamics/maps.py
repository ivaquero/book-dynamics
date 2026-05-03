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
