import numpy as np

arreglo = np.zeros(10, dtype=int)

'''
elem = 2
for i in range(10):
    arreglo[i] = elem
    elem = elem + 2

print(arreglo)
'''

for i in range(10):
    if i % 2 == 0:
        arreglo[i] = 1

for i in range(10):
    print("posición [" + str(i) + "] ->", arreglo[i])

