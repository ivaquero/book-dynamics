using CairoMakie

include("euler_backward.jl")
include("euler_forward.jl")
include("euler_improved.jl")

t₀ = 0;
tₙ = 10;
h = 0.05;
t = t₀:h:tₙ;
n_steps = length(t) - 1;
y₀ = 1;

y₁ = euler_forward(t, n_steps, y₀);
y₂ = euler_improved(t, n_steps, y₀);

T = zeros(n_steps + 1);
y₃ = euler_backward(T, n_steps, y₀);

colors = [:red, :green, :orange];
labels = ["Euler-Forward", "Euler-Improved", "Euler-Backward"];

fig = Figure(resolution = (600, 400));
ax = Axis(fig[1, 1], xlabel = "t", ylabel = "y(t)");

lines!(ax, t, y₁, color = colors[1], linewidth = 1.5, label = labels[1]);
lines!(ax, t, y₂, color = colors[2], linewidth = 1.5, label = labels[2]);
lines!(ax, T, y₃, color = colors[3], linewidth = 1.5, label = labels[3]);
axislegend(ax; position = :rb, labelsize = 12);
fig
