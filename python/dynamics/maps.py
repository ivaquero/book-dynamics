from .attractors import logistic_map


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


def cobweb_points(x_init, r, steps):
    """Return the sequence of iterates for the cobweb (useful for plotting separately)."""
    X = [x_init]
    for _ in range(steps - 1):
        X.append(logistic_map(X[-1], r))
    return X
