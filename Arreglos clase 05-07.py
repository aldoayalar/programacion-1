import numpy as np

a = np.array([2, 5, 7, 1, 4, 9])
b = np.array([8, 1, 5, 2, 0, 3])
c = np.zeros(6, dtype=int)

print(a)
print(b)

for i in range(6):
    c[i] = a[5 - i] + b[i]

print(c)
