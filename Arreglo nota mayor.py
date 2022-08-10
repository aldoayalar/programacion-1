import numpy as np

notas = np.zeros(10)

mayor = 0
i = 0
while i <= 9:
    notas[i] = float(input("ingrese nota [" + str(i + 1) + "]-> "))
    if notas[i] >= 1.0 and notas[i] <= 7.0:
        if notas[i] > mayor:
            mayor = notas[i]
            pos = i

        i = i + 1
    else:
        print("debe ingresar una nota entre 1.0 y 7.0")

print(notas)
print("la nota mayor es: ", mayor, "en la posición", pos + 1)
