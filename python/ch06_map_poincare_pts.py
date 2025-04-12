import numpy as np
from scipy.integrate import odeint


def dx_dt(x, t):
    return [
        -x[1] - x[0] * np.sqrt(x[0] ** 2 + x[1] ** 2),
        x[0] - x[1] * np.sqrt(x[0] ** 2 + x[1] ** 2),
    ]


t = np.linspace(0, 9 * 2 * np.pi, 900000)
xs = odeint(dx_dt, [1, 0], t)

for i in range(9):
    print(f"{i} = {xs[100000*i, 0]}")

# r0= 1.0
# r1 = 0.13730247618333363
# r2 = 0.0737116398245952
# r3= 0.050378946444256625
# r4= 0.03826617811397822
# r5= 0.03084905202922912
# r6= 0.02584041437408372
# r7= 0.022231002965186188
# r8= 0.019506343238878496
