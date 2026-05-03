import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import iterate_map as ppen


def prepare_logistic_map_data(
    initial_condition=0.4, r=4, n_iterations=500, x_range=(0, 1, 0.001)
):
    """Prepare logistic map data."""
    T = np.arange(0, n_iterations, 1)
    X = ppen(initial_condition, r, n_iterations)
    X_ = np.arange(*x_range)
    f = 4 * X_ * (1 - X_)
    return X, X_, f


def plot_logistic_map(ax, X, X_, f, **scatter_kwargs):
    """Plot logistic map on given axes."""
    ax.scatter(X[:-1], X[1:], **scatter_kwargs)
    ax.plot(X_, f)


def create_logistic_map_plot():
    """Create the main logistic map plot."""
    # Prepare data
    X, X_, f = prepare_logistic_map_data()

    # Create figure
    fig, ax = plt.subplots()

    # Plot logistic map
    plot_logistic_map(ax, X, X_, f)

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_logistic_map_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
