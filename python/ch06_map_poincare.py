import matplotlib.pyplot as plt
import numpy as np

from .dynamics.attractors import solve_poincare_trajectory
from .dynamics.plotting import plot_poincare_section


def create_poincare_plot():
    """Create the main Poincare section plot."""
    # Parameters
    t_span = [0, 16 * np.pi]
    initial_conditions = [1, 0]

    # Solve trajectory
    X = solve_poincare_trajectory(initial_conditions, t_span)

    # Create figure
    fig, ax = plt.subplots()

    # Plot Poincare section
    plot_poincare_section(ax, X)

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_poincare_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
