import numpy as np

suma = 0
prom = 0

arreglo = np.zeros(10, dtype=int)
mayores = np.zeros(10, dtype=int)

# se solicitan 10 numeros al usuario y se muestra cuales son mayores al promedio
for i in range(10):
    print("ingrese número, posición[" + str(i) + "]", end="")
    arreglo[i] = int(input("-> "))
    suma = suma + arreglo[i]

prom = suma / 10
round(suma, 2)
print("Arreglo =", arreglo)
print("promedio = ", prom)

j = 0
for i in range(10):
    if prom < arreglo[i]:
        mayores[j] = arreglo[i]
        j = j + 1

mayores = np.trim_zeros(mayores)
print("los mayores que el promedio son: ", mayores)
