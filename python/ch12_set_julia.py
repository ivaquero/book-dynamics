import matplotlib.cm as cm
import matplotlib.pyplot as plt

from .dynamics.attractors import julia_set


def prepare_julia_set_data(complex_constant=complex(0.9, 0.5)):
    """Prepare Julia set data."""
    return julia_set(complex_constant)


def plot_julia_set(ax, julia, cmap=cm.gnuplot2, **imshow_kwargs):
    """Plot Julia set on given axes."""
    ax.imshow(julia, interpolation="nearest", cmap=cmap, **imshow_kwargs)
    ax.axis("off")


def create_julia_set_plot():
    """Create the main Julia set plot."""
    # Prepare data
    julia = prepare_julia_set_data()

    # Create figure
    fig, ax = plt.subplots()

    # Plot Julia set
    plot_julia_set(ax, julia)

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_julia_set_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
