import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from .dynamics.attractors import logistic_eq


def solve_logistic_trajectory(x_init, t_span, n_points=1000):
    """Solve logistic equation trajectory for given initial condition."""
    t = np.linspace(t_span[0], t_span[1], n_points)
    sol = solve_ivp(logistic_eq, t_span, [x_init], dense_output=True)
    X = sol.sol(t).T
    return t, X


def plot_logistic_trajectories(ax, x_inits, t_span, **plot_kwargs):
    """Plot multiple logistic trajectories on given axes."""
    for x_init in x_inits:
        t, X = solve_logistic_trajectory(x_init, t_span)
        ax.plot(t, X, label=f"X = {x_init}", **plot_kwargs)


def setup_logistic_plot(ax, title="The Logistics Equation"):
    """Setup logistic plot properties."""
    ax.legend()
    ax.set(xlabel="Time", ylabel="X", title=title)


def create_logistic_equation_plot():
    """Create the main logistic equation plot."""
    # System parameters
    x_inits = [1, 50, 200]
    t_span = [0, 200]

    # Create figure
    fig, ax = plt.subplots()

    # Plot trajectories
    plot_logistic_trajectories(ax, x_inits, t_span)

    # Setup plot properties
    setup_logistic_plot(ax)

    return fig, ax


def main():
    """Main function to create and display the plot."""
    fig, ax = create_logistic_equation_plot()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    main()
