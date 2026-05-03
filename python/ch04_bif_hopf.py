import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

from .dynamics.bifurcations import hopf
from .dynamics.plotting import make_multi_traj_anim


def prepare_hopf_bifurcation_data(initial_conditions, t_span, n_points=20000):
    """Prepare Hopf bifurcation analysis data."""
    t = np.linspace(t_span[0], t_span[1], n_points)
    return t


def compute_hopf_trajectory_for_parameter(mu, initial_conditions, t_span, t):
    """Compute Hopf trajectory for a given parameter value."""
    sol = solve_ivp(hopf, t_span, initial_conditions, args=(mu,), dense_output=True)
    X = sol.sol(t).T
    return [X]


def create_hopf_bifurcation_animation():
    """Create Hopf bifurcation animation."""
    # Parameters
    initial_conditions = [1, 0]
    t_span = [0, 200]

    # Prepare data
    t = prepare_hopf_bifurcation_data(initial_conditions, t_span)

    # Create figure
    fig, ax = plt.subplots()

    # Create animation function
    def compute_trajs_for_param(mu):
        return compute_hopf_trajectory_for_parameter(mu, initial_conditions, t_span, t)

    animate = make_multi_traj_anim(ax, compute_trajs_for_param)

    # Create animation
    anim = FuncAnimation(fig, animate, frames=np.arange(-1, 1, 0.1), interval=100)

    return fig, ax, anim


def main():
    """Main function to create and display the animation."""
    fig, ax, anim = create_hopf_bifurcation_animation()
    plt.show()
    return fig, ax, anim


if __name__ == "__main__":
    main()
