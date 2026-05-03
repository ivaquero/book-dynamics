import matplotlib.pyplot as plt

from .dynamics.attractors import rossler
from .dynamics.integrators import euler_fixed


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

    traj, times = euler_fixed(rossler, initial_conditions, dt, step_count)
    return traj, times


def plot_rossler_attractor(ax, traj, **plot_kwargs):
    """Plot Rossler attractor on given axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        3D axes instance for plotting.
    traj : numpy.ndarray
        Trajectory array of shape (n_points, 3) containing [x, y, z] coordinates.
    **plot_kwargs : dict
        Additional keyword arguments passed to ax.plot().

    Returns
    -------
    matplotlib.lines.Line2D
        The plotted line object.
    """
    xs = traj[:, 0]
    ys = traj[:, 1]
    zs = traj[:, 2]

    line = ax.plot(xs, ys, zs, lw=0.5, **plot_kwargs)
    ax.set(xlabel="x", ylabel="y", zlabel="z", title="Rossler Attractor")
    return line


def create_rossler_plot(
    initial_conditions=None, dt=0.01, step_count=50000, **plot_kwargs
):
    """Create complete Rossler attractor plot.

    Parameters
    ----------
    initial_conditions : list, optional
        Initial [x, y, z] conditions. Defaults to [1.0, 1.0, 1.0].
    dt : float, optional
        Time step size. Defaults to 0.01.
    step_count : int, optional
        Number of integration steps. Defaults to 50000.
    **plot_kwargs : dict
        Additional keyword arguments passed to ax.plot().

    Returns
    -------
    tuple
        (fig, ax, line) containing the figure, axes, and plotted line objects.
    """
    traj, _ = solve_rossler_trajectory(initial_conditions, dt, step_count)

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    line = plot_rossler_attractor(ax, traj, **plot_kwargs)

    return fig, ax, line


def main():
    """Main function to generate Rossler attractor plot."""
    fig, ax, line = create_rossler_plot()
    plt.show()


if __name__ == "__main__":
    main()
