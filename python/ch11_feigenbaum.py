import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import logistic_map


def prepare_feigenbaum_data(
    r_range=(0, 4, 2000), initial_x=0.1, warmup_iterations=500, recording_iterations=50
):
    """Prepare Feigenbaum bifurcation data."""
    ys = []
    rs = np.linspace(*r_range)

    for r in rs:
        x = initial_x
        # Warmup iterations to reach steady state
        for _ in range(warmup_iterations):
            x = logistic_map(x, r)
        # Recording iterations
        for _ in range(recording_iterations):
            x = logistic_map(x, r)
            ys.append([r, x])

    return np.array(ys)


def plot_feigenbaum_bifurcation(ax, ys, **plot_kwargs):
    """Plot Feigenbaum bifurcation diagram on given axes."""
    ax.plot(ys[:, 0], ys[:, 1], "r.", markersize=0.8, **plot_kwargs)


def create_feigenbaum_plot():
    """Create the main Feigenbaum bifurcation plot."""
    # Prepare bifurcation data
    ys = prepare_feigenbaum_data()

    # Create figure
    fig, ax = plt.subplots()

    # Plot bifurcation diagram
    plot_feigenbaum_bifurcation(ax, ys)

    # Setup axis properties
    ax.set(xlabel="$μ$", ylabel="x")

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_feigenbaum_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
