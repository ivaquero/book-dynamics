import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import duffing_simple


def solve_duffing_trajectory(initial_conditions, t_span, epsilon=0.01, n_points=2000):
    """Solve Duffing equation trajectory."""
    sol = solve_ivp(
        duffing_simple, t_span, initial_conditions, args=(epsilon,), dense_output=True
    )
    t = np.linspace(t_span[0], t_span[1], n_points)
    X = sol.sol(t).T[:, 0]
    return t, X


def calculate_perturbation_difference(X, t):
    """Calculate perturbation difference from cosine reference."""
    x_perturb = np.cos(t)
    return X - x_perturb


def plot_duffing_perturbation(ax, t, perturb_diff, **plot_kwargs):
    """Plot Duffing perturbation difference on given axes."""
    ax.plot(t, perturb_diff, **plot_kwargs)
    ax.set(xlabel="t", ylabel="$x_N-x_0$")


def create_duffing_plot():
    """Create the main Duffing equation perturbation plot."""
    # Parameters
    epsilon = 0.01
    initial_conditions = [1, 0]
    t_span = [0, 100]

    # Solve trajectory
    t, X = solve_duffing_trajectory(initial_conditions, t_span, epsilon)

    # Calculate perturbation
    perturb_diff = calculate_perturbation_difference(X, t)

    # Create figure
    fig, ax = plt.subplots()

    # Plot perturbation
    plot_duffing_perturbation(ax, t, perturb_diff)

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_duffing_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
