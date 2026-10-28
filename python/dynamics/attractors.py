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
    "FHN",
    "HPG",
    "HPG2",
    "SEIR",
    "SIR",
    "FHN_coupled",
    "Holling_Tanner",
    # Visualization
    "arrows",
    "bz_reaction",
    # Systems
    "clarinet",
    "collins",
    # Fractals
    "complex_set",
    "compute_hpg_derivatives",
    "derivatives",
    "duffing",
    "duffing_simple",
    "fhn_lim_derivatives",
    "fhn_nullclines",
    "food_chain",
    "gen_mesh",
    "hamiltonian_4d",
    "hamiltonian_fun",
    "henon",
    "homoclinic",
    "iterate_map",
    "julia_set",
    "lienard",
    "logistic_eq",
    "logistic_map",
    "lorenz",
    "lotka_volterra",
    "mckey_glass",
    "plot_phase",
    "plot_poincare",
    "poincare_derivatives",
    "poincare_dx_dt",
    "prepare_hpg2_initial_conditions",
    "prepare_hpg_initial_conditions",
    "pulsed_FHN_coupled_factory",
    "pulsed_FHN_factory",
    "rossler",
    "solve_hpg2_trajectories",
    "solve_hpg_trajectory",
    # Trajectory solvers
    "solve_lorenz_trajectory",
    "solve_poincare_trajectory",
    "solve_rossler_trajectory",
    "stepwise",
    "vector_field",
]
