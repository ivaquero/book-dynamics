from sympy import Matrix, simplify, solve, symbols

x, y = symbols("x y", negative=False)
β, γ, c, d = symbols("β γ c d")
eq1 = β * x - γ * x * y
eq2 = -d * y + c * x * y
sol = solve([eq1, eq2], [x, y])
print(sol)
# [(0, 0), (d/c, β/γ)]

eqMat = Matrix([eq1, eq2])
Mat = Matrix([x, y])
jacMat = eqMat.jacobian(Mat)


for item in sol:
    eqmat = jacMat.subs([(x, item[0]), (y, item[1])])
    eigenvals = list(eqmat.eigenvals().keys())
    print(
        f"The eigenvalues for the fixed point {item[0], item[1]} are: [{simplify(eigenvals)[0], simplify(eigenvals[1])}]\n"
    )

# The eigenvalues for the fixed point (0, 0) are: [β, -d]
# The eigenvalues for the fixed point (d/c, β/γ) are: [-sqrt(-β*d), sqrt(-β*d)]
