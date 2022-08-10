import numpy as np

a = np.array([3, 7, 1, 5, 8, 4])

mayor = a[0]
menor = a[0]

for i in range(5):
    if a[i] > mayor:
        mayor = a[i]
    if a[i] < menor:
        menor = a[i]
print(mayor)
print(menor)
