function euler_backward(T, n_steps, y₀)
	f = zeros(n_steps + 1)
	y_new = zeros(n_steps + 1)
	y = zeros(n_steps + 1)
	y[1] = y₀

	for ii ∈ 1:n_steps
		T[ii + 1] = T[ii] + h
		f[ii] = 3 - 2 * y[ii] + exp(-T[ii])
		y_new[ii] = y[ii] + h * f[ii]
		f[ii + 1] = 3 - 2 * y_new[ii] + exp(-T[ii + 1])
		y[ii + 1] = y[ii] + f[ii + 1] * h
	end
	return y
end
