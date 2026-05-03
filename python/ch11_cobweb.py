import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import logistic_map
from .dynamics.maps import cobweb_points
from .dynamics.plotting import draw_cobweb


def prepare_cobweb_data(r=4, x_init=0.01, steps=50, t_resolution=0.001):
    """Prepare cobweb plot data."""
    # Time series data
    T_series = np.arange(0, steps, 1)
    X_series = cobweb_points(x_init, r, len(T_series))

    # Function curve data
    T_curve = np.arange(0, 1, t_resolution)
    X_curve = logistic_map(T_curve, r)

    return T_series, X_series, T_curve, X_curve


def plot_cobweb_diagram(ax, T_series, X_series, T_curve, X_curve, r, x_init, steps):
    """Plot cobweb diagram on given axes."""
    # Draw cobweb
    ax.set(xlim=(0, 1), ylim=(0, 1.1))
    draw_cobweb(ax, steps, x_init, r)

    # Plot function curve and identity line
    ax.plot(T_curve, X_curve, color="black")
    ax.plot(T_curve, T_curve, color="grey")


def plot_time_series(ax, T_series, X_series):
    """Plot time series on given axes."""
    ax.set(xlim=(0, len(T_series)), ylim=(0, 1.1))
    ax.plot(T_series, X_series, color="b")
    ax.scatter(T_series, X_series, color="black")


def create_cobweb_plot():
    """Create the main cobweb plot with diagram and time series."""
    # Parameters
    r = 4
    x_init = 0.01
    steps = 50

    # Prepare data
    T_series, X_series, T_curve, X_curve = prepare_cobweb_data(r, x_init, steps)

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=1)

    # Plot cobweb diagram
    plot_cobweb_diagram(ax1, T_series, X_series, T_curve, X_curve, r, x_init, steps)

    # Plot time series
    plot_time_series(ax2, T_series, X_series)

    return fig, (ax1, ax2)


def main():
    """Main function to create and display the plot."""
    fig, axes = create_cobweb_plot()
    plt.show()
    return fig, axes


if __name__ == "__main__":
    main()
