import numpy as np

a = np.array([7, 1, 6, 9, 8, 0, 3, 5, 4, 10])
print("Arreglo original \n", a)

aux = 0
for i in range(5):
    aux = a[i]
    a[i] = a[9 - i]
    a[9 - i] = aux

print("orden invertido \n", a)
#print(len(a))
