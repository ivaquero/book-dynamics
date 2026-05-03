# book-dynamics python utilities

This folder contains example scripts and shared helper modules used by the book-dynamics Python examples.

Modules
- `dynamics.attractors` — ODE RHS, maps, pulsed factories and nullcline helpers (e.g. `FHN`, `pulsed_FHN_factory`, `fhn_nullclines`).
- `dynamics.bifurcations` — bifurcation RHSs and 1D utilities (e.g. `hopf`, `opinion`).
- `dynamics.maps` — helpers for discrete maps and cobweb drawing.
- `dynamics.plotting` — shared plotting & animation helpers:
  - `plot_phase(func, t_span, z, ax)` — phase portrait helper.
  - `plot_poincare(func, t_span, z, n_period, ax)` — Poincaré section helper.
  - `make_param_anim(ax, compute_xy_for_param, ...)` — returns `(init, animate)` for parameterized curves.
  - `make_multi_traj_anim(ax, compute_trajs_for_param, ...)` — animate multiple trajectories per parameter.
  - `time_series_from_pulsed_factory(start, stop, I_ext_value, ts, z0, integrator=None, factory_func=None)` — integrate pulsed FHN factories using `euler_fixed` by default.
- `ode.integrators` — numerical integrators (e.g. `euler_fixed`, `euler_delay`, `runge_kutta4`).
- `ode.field_2d` — mesh / vector-field helpers.

Quick usage examples

Integrate pulsed FHN using the built-in helper:

```python
import numpy as np
from dynamics.plotting import time_series_from_pulsed_factory
from ode.integrators import euler_fixed

ts = np.arange(0, 4, 0.01)
traj, times = time_series_from_pulsed_factory(1.0, 1.2, 0.01, ts, [0,0], integrator=euler_fixed)
# traj shape: (len(ts), 2)
```

Create a parameter animation (saddle / Hopf examples):

```python
from dynamics.plotting import make_param_anim
# implement compute_xy_for_param(param) -> (x_array, y_array)
# then:
# init, animate = make_param_anim(ax, compute_xy_for_param)
# FuncAnimation(fig, animate, frames=params)
```

Notes
- Examples are verified with `python3 -m compileall` to ensure import-time syntax correctness.
- To run animations interactively, ensure a display backend is available. For headless checks the `Agg` backend is recommended.

Dependencies
- numpy
- scipy
- matplotlib

If you want I can also add a short `requirements.txt` or a minimal test harness.
