function runge_kutta(t, n_steps, y₀)
	k₁ = zeros(1, n_steps)
	k₂ = k₁
	k₃ = k₁
	k₄ = k₁
	y = zeros(n_steps + 1)
	y[1] = y₀

	for ii ∈ 1:n_steps
		k₁[ii] = 3 + exp(-t[ii]) - 2y[ii]
		k₂[ii] = 3 + exp(-(t[ii] + h / 2)) - 2(y[ii] + k₁[ii] * h / 2)
		k₃[ii] = 3 + exp(-(t[ii] + h / 2)) - 2(y[ii] + k₂[ii] * h / 2)
		k₄[ii] = 3 + exp(-(t[ii] + h)) - 2(y[ii] + k₃[ii] * h)
		y[ii + 1] = y[ii] + h * (k₁[ii] + 2k₂[ii] + 2k₃[ii] + k₄[ii]) / 6
	end
	return y
end
