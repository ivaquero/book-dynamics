function euler_improved(t, n_steps, y0)
	f = zeros(size(t))
	f[1] = 3 + exp(-t[1]) - 2 * y0
	y = zeros(size(t))
	y[1] = y0
	for ii ∈ 1:n_steps
		f[ii + 1] = 3 + exp(-(t[ii] + h)) - 2 * (y[ii] + h * f[ii])
		y[ii + 1] = y[ii] + (f[ii] + f[ii + 1]) * (h / 2)
	end
	return y
end
