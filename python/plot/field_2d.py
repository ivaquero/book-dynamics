import matplotlib.pyplot as plt
import numpy as np


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
