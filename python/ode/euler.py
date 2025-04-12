def euler(t, tmax, y, func_dx, step=1.0):
    ys = []
    while t < tmax:
        y = y + step * dx(t, y)
        ys.append(y)
        t += step
    return ys


def dx(t, y):
    return y
