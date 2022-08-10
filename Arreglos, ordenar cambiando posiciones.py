import numpy as np

a = np.array([10, 7, 1, 5, 8, 4, 6, 2, 9, 3])

aux = 0
for i in range(10):
    for j in range(10):
        if a[i] < a[j]:
            aux = a[i]
            a[i] = a[j]
            a[j] = aux

print(a)
