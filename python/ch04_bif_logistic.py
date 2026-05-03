import matplotlib.pyplot as plt
import numpy as np

from .dynamics.bifurcations import number_track


def prepare_bifurcation_data(h_range=(0, 1, 20), a_range=(0, 1, 20)):
    """Prepare bifurcation data."""
    h_vals = np.linspace(*h_range)
    a_vals = np.linspace(*a_range)
    matrix = number_track(h_vals, a_vals)
    return matrix, h_vals, a_vals


def plot_bifurcation_matrix(ax, matrix, extent=(0, 1, 0, 1), **imshow_kwargs):
    """Plot bifurcation matrix on given axes."""
    return ax.imshow(matrix, extent=extent, aspect="auto", **imshow_kwargs)


def create_bifurcation_plot():
    """Create the main bifurcation plot."""
    # Prepare bifurcation data
    matrix, _, _ = prepare_bifurcation_data()
    extent = [0, 1, 0, 1]

    # Create figure
    fig, ax = plt.subplots()

    # Plot bifurcation matrix
    image = plot_bifurcation_matrix(ax, matrix, extent)

    return fig, ax, image


def main():
    """Main function to create and display the plot."""
    fig, ax, image = create_bifurcation_plot()
    plt.show()
    return fig, ax, image


if __name__ == "__main__":
    main()
