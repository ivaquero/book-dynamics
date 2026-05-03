import matplotlib.pyplot as plt
import numpy as np

from .dynamics.bifurcations import track_in_3D


def prepare_3d_bifurcation_data(n_points=20, r_range=[0, 0.6], k_range=[0, 40]):
    """Prepare 3D bifurcation data."""
    rs = np.linspace(r_range[0], r_range[1], n_points)
    ks = np.linspace(k_range[0], k_range[1], n_points)
    stable_points, unstable_points = track_in_3D(rs, ks)
    return stable_points, unstable_points


def plot_3d_bifurcation_points(ax, stable_points, unstable_points, **scatter_kwargs):
    """Plot 3D bifurcation points on given axes."""
    ax.scatter(
        stable_points[0],
        stable_points[1],
        stable_points[2],
        color="g",
        **scatter_kwargs,
    )
    ax.scatter(
        unstable_points[0],
        unstable_points[1],
        unstable_points[2],
        color="r",
        **scatter_kwargs,
    )


def create_3d_bifurcation_plot():
    """Create the main 3D bifurcation plot."""
    # Prepare bifurcation data
    stable_points, unstable_points = prepare_3d_bifurcation_data()

    # Create figure with 3D projection
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot bifurcation points
    plot_3d_bifurcation_points(ax, stable_points, unstable_points)

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_3d_bifurcation_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
