from sympy import symbols

from .dynamics.symbolic import solve_logistic_ode

t = symbols("t")
r, m = symbols("r m")


def main():
    sol = solve_logistic_ode(r, m, t_symbol=t)
    print(sol)


if __name__ == "__main__":
    main()
