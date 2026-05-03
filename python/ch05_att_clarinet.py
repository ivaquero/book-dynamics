import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

from .dynamics.attractors import clarinet
from .dynamics.plotting import make_multi_traj_anim


def prepare_clarinet_initial_conditions(
    n_angles=5, outer_radius=1.5, inner_radius=0.05
):
    """Prepare initial conditions for clarinet attractor analysis."""
    θs = np.linspace(0, 2 * np.pi, n_angles)
    coordinates = []

    for θ in θs:
        coordinates.extend(
            [
                [outer_radius * np.cos(θ), outer_radius * np.sin(θ)],
                [inner_radius * np.cos(θ), inner_radius * np.sin(θ)],
            ]
        )

    return coordinates


def solve_clarinet_trajectories_for_parameter(a, coordinates, t_span, t):
    """Solve clarinet trajectories for a given parameter value."""
    trajs = []
    for coordinate in coordinates:
        x_i, y_i = coordinate
        sol = solve_ivp(clarinet, t_span, [x_i, y_i], args=(a,), dense_output=True)
        X = sol.sol(t).T
        trajs.append(X)
    return trajs


def create_clarinet_animation():
    """Create clarinet attractor animation."""
    # Prepare initial conditions
    coordinates = prepare_clarinet_initial_conditions()

    # Parameters
    a_list = np.arange(0.1, 2, 0.1)[::-1]
    t_span = [0, 10]
    t = np.linspace(t_span[0], t_span[1], 100)

    # Create figure
    fig, ax = plt.subplots()

    # Create animation function
    def compute_trajs_for_param(a):
        return solve_clarinet_trajectories_for_parameter(a, coordinates, t_span, t)

    animate = make_multi_traj_anim(
        ax, compute_trajs_for_param, xlim=(-2, 2), ylim=(-1, 1), xlabel="x", ylabel="y"
    )

    # Create animation
    anim = FuncAnimation(fig, animate, frames=a_list, interval=100)

    return fig, ax, anim


def main():
    """Main function to create and display the animation."""
    fig, ax, anim = create_clarinet_animation()
    plt.show()
    return fig, ax, anim


if __name__ == "__main__":
    main()
