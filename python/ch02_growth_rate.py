import matplotlib.pyplot as plt

from .dynamics.attractors import lotka_volterra
from .ode.field_2d import gen_mesh, vector_field
from .ode.integrators import euler_fixed


def prepare_growth_rate_data(xy_range=[0, 100, 0, 100], n_points=15):
    """Prepare growth rate data on a grid."""
    # create a grid
    X, Y = gen_mesh(xy_range, n_points)
    # compute growth rate on the grid
    U, V = lotka_volterra(t=0, z=[X, Y])
    return X, Y, U, V


def solve_trajectory_with_step_size(lotka_volterra_func, xy_init, step_size, period):
    """Solve trajectory for a given step size."""
    traj, _ = euler_fixed(lotka_volterra_func, xy_init, step_size, period)
    x = traj[:, 0]
    y = traj[:, 1]
    return x, y


def plot_growth_rate_trajectory(ax, x, y, X, Y, U, V, step_size, **plot_kwargs):
    """Plot growth rate trajectory on given axes."""
    ax.scatter(x, y, **plot_kwargs)
    vector_field(ax, X, Y, U, V)
    ax.set(title=f"δt = {step_size}")


def create_growth_rate_comparison_plot():
    """Create growth rate comparison plot for different step sizes."""
    # Prepare data
    X, Y, U, V = prepare_growth_rate_data()

    # Create figure
    fig, axes = plt.subplots(1, 2)

    # Parameters
    step_sizes = [0.01, 0.1]
    xy_init = [80, 60]
    period = 10000

    # Plot for each step size
    for ind, step in enumerate(step_sizes):
        x, y = solve_trajectory_with_step_size(lotka_volterra, xy_init, step, period)
        plot_growth_rate_trajectory(axes[ind], x, y, X, Y, U, V, step)

    return fig, axes


def main():
    """Main function to create and display the plot."""
    fig, axes = create_growth_rate_comparison_plot()
    plt.show()
    return fig, axes


if __name__ == "__main__":
    main()
