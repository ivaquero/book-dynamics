import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import poincare_derivatives


def solve_poincare_trajectory(initial_conditions, t_span, n_points=10000):
    """Solve Poincare trajectory."""
    sol = solve_ivp(poincare_derivatives, t_span, initial_conditions, dense_output=True)
    t = np.linspace(t_span[0], t_span[1], n_points)
    return sol.sol(t).T


def plot_poincare_section(ax, X, **plot_kwargs):
    """Plot Poincare section on given axes."""
    ax.plot(X[:, 0], X[:, 1], "r-", **plot_kwargs)
    ax.set(xlabel="x", ylabel="y", xlim=(-0.5, 1.5), ylim=(-0.5, 0.5))


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
