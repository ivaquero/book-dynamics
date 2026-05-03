import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import collins
from .ode.field_2d import gen_mesh, vector_field


def prepare_vector_field_data(xy_range=(0, 5, 0, 5), n_points=10, system_func=collins):
    """Prepare vector field data."""
    A, B = gen_mesh(xy_range, n_points)
    u, v = system_func(t=0, z=[A, B])
    return A, B, u, v


def plot_nullclines(ax, x_range=(0, 5, 0.1)):
    """Plot nullclines on given axes."""
    row, col = np.arange(*x_range), np.arange(*x_range)
    null_row, null_col = 5 / (1 + col**4), 5 / (1 + row**4)

    ax.plot(row, null_col)
    ax.plot(null_row, col)


def create_switch_collins_plot():
    """Create the main switch collins plot."""
    # System parameters
    xy_range = [0, 5, 0, 5]
    n_points = 10

    # Prepare vector field data
    A, B, u, v = prepare_vector_field_data(xy_range, n_points)

    # Create figure
    fig, ax = plt.subplots()

    # Plot vector field and nullclines
    vector_field(ax, A, B, u, v)
    plot_nullclines(ax)

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_switch_collins_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
