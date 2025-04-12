function euler_forward(t, n_steps, y₀)
    f = zeros(size(t))
    y = zeros(size(t))
    y[1] = y₀
    y[2] = f[end-1]

    for ii ∈ 1:n_steps
        f[ii] = 3 + exp(-t[ii]) - 2 * y[ii]
        y[ii+1] = y[ii] + f[ii] * h
    end
    return y
end
