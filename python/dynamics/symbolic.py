"""Symbolic computation utilities for dynamical systems.

This module contains functions for symbolic mathematics, including
Groebner basis computation, polynomial operations, and Julia set analysis.
"""

from sympy import (
    LM,
    LT,
    Eq,
    Function,
    I,
    Matrix,
    Rational,
    S,
    dsolve,
    expand,
    im,
    integrate,
    lambdify,
    lcm,
    re,
    rsolve,
    solve,
    sqrt,
    symbols,
)


def compute_julia_unstable(a, b):
    """Compute the instability measure used in the Julia example.

    Parameters
    ----------
    a : float
        Real part of parameter
    b : float
        Imaginary part of parameter

    Returns
    -------
    sympy expression
        Numeric expression for 2*abs(x1 + y1*I)
    """
    x1 = (re(0.5 + sqrt(0.25 - (a + b * I)))).expand(complex=True)
    y1 = (im(0.5 + sqrt(0.25 - (a + b * I)))).expand(complex=True)
    return 2 * abs(x1 + y1 * I)


def s_polynomial_sym(f, g):
    """Compute the S-polynomial of two polynomials (sympy objects).

    Parameters
    ----------
    f : sympy expression
        First polynomial
    g : sympy expression
        Second polynomial

    Returns
    -------
    sympy expression
        S-polynomial
    """
    return expand(lcm(LM(f), LM(g)) * (1 / LT(f) * f - 1 / LT(g) * g))


def compute_reduced(f, polys):
    """Wrapper around sympy.reduced.

    Parameters
    ----------
    f : sympy expression
        Polynomial to reduce
    polys : list
        List of divisor polynomials

    Returns
    -------
    tuple
        Reduced polynomial and remainder
    """
    from sympy import reduced

    return reduced(f, polys)


def groebner_basis(polys, symbols_tuple, order="lex"):
    """Compute a Groebner basis for given polynomials.

    Parameters
    ----------
    polys : list
        List of polynomials
    symbols_tuple : tuple
        Symbols to use
    order : str, optional
        Monomial order, by default "lex"

    Returns
    -------
    sympy expression
        Groebner basis
    """
    from sympy import groebner

    return groebner(polys, *symbols_tuple, order=order)


def build_piecewise_time_lambdas(tmax=10):
    """Build a list of lambdified functions for recursive time-step definition.

    Parameters
    ----------
    tmax : int, optional
        Maximum time, by default 10

    Returns
    -------
    tuple
        (functions_list, tmax) where each function is numpy-callable
    """
    xi, t = symbols("xi t")
    x = []
    for j in range(tmax + 1):
        if j == 0:
            x.append(S.One)
        else:
            prev = x[j - 1]
            prev_at_jm1 = prev.subs(t, j - 1)
            integrand = prev.subs(t, xi - 1)
            expr = prev_at_jm1 - integrate(integrand, (xi, j - 1, t))
            x.append(expr)

    funcs = [lambdify(t, expr, "numpy") for expr in x]
    return funcs, tmax


def tent_map(x, mu):
    """Tent map: works with sympy Rational or numeric values.

    Parameters
    ----------
    x : float or Rational
        Input value
    mu : float or Rational
        Map parameter

    Returns
    -------
    float or None
        mu*x for x < 1/2, mu*(1-x) for x > 1/2, else None
    """
    half = Rational(1, 2)
    try:
        if x < half:
            return mu * x
        if x > half:
            return mu * (1 - x)
    except TypeError:
        # Fallback for numpy floats
        if float(x) < 0.5:
            return mu * x
        if float(x) > 0.5:
            return mu * (1 - x)
    return None


def compute_stability_2d(eigen_values):
    """Classify 2D linear stability from eigenvalues.

    Parameters
    ----------
    eigen_values : array-like
        Two eigenvalues to classify

    Returns
    -------
    tuple
        (stab_type, one_hot_vector) where stab_type is string description
        and one_hot_vector indicates stability type
    """
    import numpy as _np

    eig1, eig2 = tuple(eigen_values)
    stability = _np.zeros(5)
    if im(eig1) < 1e-10 and im(eig2) < 1e-10:
        if eig1 < 0 and eig2 < 0:
            stab_type = "Stable node"
            stability[0] = 1
        elif eig1 > 0 and eig2 > 0:
            stab_type = "Unstable node"
            stability[1] = 1
        else:
            stab_type = "Saddle point"
            stability[2] = 1
    elif re(eig1) < 0:
        stab_type = "Stable spiral"
        stability[3] = 1
    else:
        stab_type = "Unstable spiral or limit cycle"
        stability[4] = 1
    return stab_type, stability


def solve_power_series(ode, func, n=8, ics=None):
    """Solve an ODE using sympy power-series method (wrapper).

    Parameters
    ----------
    ode : sympy expression
        Ordinary differential equation
    func : sympy Function
        Function to solve for
    n : int, optional
        Order of power series, by default 8
    ics : dict, optional
        Initial conditions

    Returns
    -------
    sympy expression
        Power series solution
    """
    return dsolve(ode, hint="1st_power_series", n=n, ics=ics)


def solve_analytic(ode, n=None, ics=None):
    """Wrapper around sympy.dsolve for analytic solution requests.

    Parameters
    ----------
    ode : sympy expression
        Ordinary differential equation
    n : int, optional
        Number of terms hint passed to dsolve
    ics : dict, optional
        Initial conditions

    Returns
    -------
    sympy expression
        Analytic solution
    """
    return dsolve(ode, n=n, ics=ics)


def solve_first_order_difference(multiplier, x0, n_symbol=None):
    """Solve the first-order linear difference equation x(n+1) = multiplier * x(n).

    Parameters
    ----------
    multiplier : sympy expression
        Common ratio of the difference equation
    x0 : sympy expression
        Initial value x(0)
    n_symbol : sympy Symbol, optional
        Symbol for the index, by default a fresh `n`

    Returns
    -------
    sympy expression
        Closed-form solution for x(n)
    """
    n = symbols("n") if n_symbol is None else n_symbol
    x = Function("x")
    f = x(n + 1) - multiplier * x(n)
    return rsolve(f, x(n), {x(0): x0})


def solve_second_order_linear(a, b, x0, x1, n_symbol=None):
    """Solve the second-order linear difference equation x(n+2) = a x(n+1) + b x(n).

    Parameters
    ----------
    a, b : sympy expressions
        Coefficients of the recurrence
    x0, x1 : sympy expressions
        Initial values x(0) and x(1)
    n_symbol : sympy Symbol, optional
        Symbol for the index, by default a fresh `n`

    Returns
    -------
    sympy expression
        Closed-form solution for x(n)
    """
    n = symbols("n") if n_symbol is None else n_symbol
    x = Function("x")
    f = x(n + 2) - a * x(n + 1) - b * x(n)
    return rsolve(f, x(n), {x(0): x0, x(1): x1})


def solve_logistic_ode(r, m, t_symbol=None):
    """Solve the logistic ODE dN/dt = r N - m N^2 via dsolve.

    Parameters
    ----------
    r, m : sympy expressions
        Growth and saturation coefficients
    t_symbol : sympy Symbol, optional
        Symbol for time, by default a fresh `t`

    Returns
    -------
    sympy expression
        General solution for N(t)
    """
    t = symbols("t") if t_symbol is None else t_symbol
    N = Function("N")
    eqn = Eq(N(t).diff(t), r * N(t) - m * N(t) * N(t))
    return dsolve(eqn, N(t))


def compute_fixed_points_and_jacobian(eqs, vars_):
    """Solve for fixed points and compute Jacobian and eigenvalues.

    - `eqs`: list of expressions (sympy) equal to zero at fixed points.
    - `vars_`: list/tuple of symbols.

    Returns
    -------
    list of dict
        Each dict has keys 'point', 'jac', 'eigenvals', 'eigenvects'.
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
