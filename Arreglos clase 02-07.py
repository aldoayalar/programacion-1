import numpy as np

arregloA = np.zeros(10, dtype=int)
arregloB = np.zeros(10, dtype=int)
arregloC = np.zeros(10, dtype=int)

for i in range(0, 10, 1):
    arregloA[i] = 10 - i
    print("elemento posición[", i, "]", arregloA[i])

i = 0
while i <= 9:
    arregloB[i] = i + 1

    i = i + 1

i = 0
while i < 9:
    arregloC[i] = int(input("ingrese numero en la posición: [" + str(i) + "] -> "))
    if arregloC[i] < 0:
        print("numero debe ser mayor que 0")
    else:
        i = i + 1

print("A ->", arregloA)
print("B ->", arregloB)
