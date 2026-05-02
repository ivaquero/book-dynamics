def pillar(X, Y, vec):
    x, y = [], []
    t = []
    for i in range(100):
        x.append(X[i * vec])
        y.append(Y[i * vec])
        t.append(i * vec)
    return x, y, t
