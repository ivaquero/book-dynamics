"""Dynamical systems attractors and utilities.

This module re-exports functions from the modularized dynamics submodules.
For better organization, functions have been split into:
- systems: Dynamical system definitions
- trajectory_solvers: Functions for solving system trajectories
- plotting: Plotting and plotting utilities
- fractals: Fractal generation functions
"""

# Import system definitions
# Import fractal functions
from .fractals import complex_set, julia_set

# Import plotting utilities
from .plotting import (
    arrows,
    derivatives,
    fhn_nullclines,
    gen_mesh,
    plot_phase,
    plot_poincare,
    vector_field,
)
from .systems import (
    FHN,
    HPG,
    HPG2,
    SEIR,
    SIR,
    FHN_coupled,
    Holling_Tanner,
    bz_reaction,
    clarinet,
    collins,
    duffing,
    duffing_simple,
    fhn_lim_derivatives,
    food_chain,
    hamiltonian_4d,
    hamiltonian_fun,
    henon,
    homoclinic,
    lienard,
    logistic_eq,
    logistic_map,
    lorenz,
    lotka_volterra,
    mckey_glass,
    poincare_derivatives,
    poincare_dx_dt,
    pulsed_FHN_coupled_factory,
    pulsed_FHN_factory,
    rossler,
)

# Import trajectory solvers
from .trajectory_solvers import (
    compute_hpg_derivatives,
    iterate_map,
    prepare_hpg2_initial_conditions,
    prepare_hpg_initial_conditions,
    solve_hpg2_trajectories,
    solve_hpg_trajectory,
    solve_lorenz_trajectory,
    solve_poincare_trajectory,
    solve_rossler_trajectory,
    stepwise,
)

# Re-export everything for backward compatibility
__all__ = [
    # Systems
    "clarinet",
    "collins",
    "HPG",
    "HPG2",
    "lorenz",
    "rossler",
    "lotka_volterra",
    "Holling_Tanner",
    "SIR",
    "SEIR",
    "duffing",
    "duffing_simple",
    "mckey_glass",
    "FHN",
    "FHN_coupled",
    "pulsed_FHN_factory",
    "pulsed_FHN_coupled_factory",
    "logistic_map",
    "henon",
    "poincare_derivatives",
    "poincare_dx_dt",
    "homoclinic",
    "lienard",
    "fhn_lim_derivatives",
    "hamiltonian_fun",
    "hamiltonian_4d",
    "logistic_eq",
    "food_chain",
    "bz_reaction",
    # Trajectory solvers
    "solve_lorenz_trajectory",
    "solve_rossler_trajectory",
    "solve_hpg_trajectory",
    "compute_hpg_derivatives",
    "prepare_hpg_initial_conditions",
    "prepare_hpg2_initial_conditions",
    "solve_hpg2_trajectories",
    "solve_poincare_trajectory",
    "iterate_map",
    "stepwise",
    # Visualization
    "arrows",
    "derivatives",
    "fhn_nullclines",
    "gen_mesh",
    "plot_phase",
    "plot_poincare",
    "vector_field",
    # Fractals
    "complex_set",
    "julia_set",
]
