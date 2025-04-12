using ModelingToolkit
using DifferentialEquations: solve

include("rk.jl")

@variables ts ys(ts);
@parameters e

D = Differential(ts);
@named runge_kutta_s = ODESystem(D(ys) ~ -2ys + e^(-ts) + 3);

prob = ODEProblem(runge_kutta_s, [ys => 1.0], (0.0, 10.0), [e => ℯ]);
sol = solve(prob);

t₀ = 0;
tₙ = 10;
h = 0.05;
t = t₀:h:tₙ;
n_steps = length(t) - 1;
y₀ = 1;

y = runge_kutta(t, n_steps, y₀)

fig = Figure(resolution = (600, 400))
ax = Axis(fig[1, 1],
	xlabel = "t",
	ylabel = "Solution, y(t)",
	title = "Solutions of: y′ + 2y - e⁻ᵗ = 3, y₀ = 1")

lines!(ax, t, y, linewidth = 1.5, label = "Runge-Kutta Method")
lines!(ax, sol.t, vcat(sol.u...), linewidth = 1.5, label = "Analytic solution")
axislegend(ax, position = :rb, labelsize = 12)

fig
