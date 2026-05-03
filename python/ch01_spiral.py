from functools import partial

import matplotlib.pyplot as plt

from .dynamics.attractors import clarinet
from .ode.integrators import euler_fixed


def solve_trajectory(f, xy_init, step_size, period, integrator=euler_fixed):
    """Solve trajectory using specified integrator."""
    traj, t = integrator(f, xy_init, step_size, period)
    x = traj[:, 0]
    y = traj[:, 1]
    return x, y


def plot_trajectory(ax, x, y, **plot_kwargs):
    """Plot trajectory on given axes."""
    ax.plot(x, y, **plot_kwargs)


def setup_axis_limits(ax, xlim=None, ylim=None):
    """Setup axis limits."""
    if xlim:
        ax.set(xlim=xlim)
    if ylim:
        ax.set(ylim=ylim)


def create_spiral_plot():
    """Create the main spiral plot."""
    # System parameters
    xy_inits = [[0, 0.1], [1.2, 1.2]]
    step_sizes = [0.1, 0.1]
    periods = [150, 80]

    # Create figure
    fig, ax = plt.subplots()

    # Plot trajectories
    for xy_init, step_size, period in zip(xy_inits, step_sizes, periods, strict=True):
        f = partial(clarinet, a=1)
        x, y = solve_trajectory(f, xy_init, step_size, period)
        plot_trajectory(ax, x, y)

    # Setup axis properties
    setup_axis_limits(ax, xlim=(-2, 2))

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_spiral_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
