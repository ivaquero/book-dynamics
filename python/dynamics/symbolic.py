from sympy import Eq, Function, Matrix, dsolve, rsolve, solve, symbols


def solve_first_order_difference(multiplier, x0, n_symbol=None):
    n = symbols("n") if n_symbol is None else n_symbol
    x = Function("x")
    f = x(n + 1) - multiplier * x(n)
    return rsolve(f, x(n), {x(0): x0})


def solve_second_order_linear(a, b, x0, x1, n_symbol=None):
    n = symbols("n") if n_symbol is None else n_symbol
    x = Function("x")
    f = x(n + 2) - a * x(n + 1) - b * x(n)
    return rsolve(f, x(n), {x(0): x0, x(1): x1})


def solve_logistic_ode(r, m, t_symbol=None):
    t = symbols("t") if t_symbol is None else t_symbol
    N = Function("N")
    eqn = Eq(N(t).diff(t), r * N(t) - m * N(t) * N(t))
    return dsolve(eqn, N(t))


def compute_fixed_points_and_jacobian(eqs, vars_):
    """Solve for fixed points and compute Jacobian and eigenvalues.

    - `eqs`: list of expressions (sympy) equal to zero at fixed points.
    - `vars_`: list/tuple of symbols.
    Returns list of dicts: { 'point': (xval, yval,...), 'jac': Matrix, 'eigenvals': list, 'eigenvects': list }
    """
    sols = solve(eqs, vars_)
    results = []
    jac = Matrix(eqs).jacobian(Matrix(vars_))
    for sol in sols:
        subs = list(zip(vars_, sol, strict=True))
        jac_sub = jac.subs(subs)
        eigvals = list(jac_sub.eigenvals().keys())
        eigvects = list(jac_sub.eigenvects())
        results.append(
            {"point": sol, "jac": jac_sub, "eigenvals": eigvals, "eigenvects": eigvects}
        )
    return results
