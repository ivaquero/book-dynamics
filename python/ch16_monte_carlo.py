from secrets import randbits

import numpy as np

success = 0
attempts = 10000

for _ in range(attempts):
    heads = np.array([randbits(1) for _ in range(4)])
    if heads.sum == 3:
        success += 1

print(f"Number of attempts = {attempts}")
print(f"Number of success = {success}")
