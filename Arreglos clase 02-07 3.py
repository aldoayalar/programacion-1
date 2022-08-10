import numpy as np

arreglo = np.zeros(10, dtype=int)

'''
elem = 1
elem2 = 10
for i in range(0, elem2):
    if i < elem2 // 2:
        arreglo[i] = elem
        elem = elem + 2
    else:
        arreglo[i] = elem2
        elem2 = elem2 - 2

print(arreglo)
'''

elemento = 1
for i in range(5):
    arreglo[i] = elemento
    elemento = elemento + 1
    arreglo[9 - i] = elemento
    elemento = elemento + 1

print("Arreglo =", arreglo)
