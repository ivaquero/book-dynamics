import matplotlib.pyplot as plt

from .dynamics.attractors import henon
from .dynamics.maps import iterate_map_2d


def prepare_henon_data(a=1.2, b=0.4, num_iterations=10000, warmup_iterations=100):
    """Prepare Henon map data."""
    X0 = [(1 - b) / 2, (1 - b) / 2]

    # warmup iterates (discarded)
    _, _ = iterate_map_2d(henon, X0, warmup_iterations, a, b)

    # main iterations
    X, Y = iterate_map_2d(henon, X0, num_iterations, a, b)
    return X, Y


def plot_henon_map(ax, X, Y, **plot_kwargs):
    """Plot Henon map on given axes."""
    ax.plot(X, Y, "b.", ms=1, **plot_kwargs)


def create_henon_map_plot():
    """Create the main Henon map plot."""
    # Prepare data
    X, Y = prepare_henon_data()

    # Create figure
    fig, ax = plt.subplots()

    # Plot Henon map
    plot_henon_map(ax, X, Y)

    # Setup axis properties
    ax.set(xlabel="x", ylabel="y")

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_henon_map_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
