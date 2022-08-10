# notas
nota1 = 0
nota2 = 0
notaF = 0

# ciclo para pedir nota 1
i = 1
while i < 2:
    nota1 = float(input("ingrese nota de proyecto semestral: "))

    if nota1 >= 1.0 and nota1 <= 7.0:
        i = i + 1
    else:
        print("nota ingresada no es válida, las notas deben ser entre 1.0 y 7.0")

# ciclo para pedir nota 2
i = 1
while i < 2:
    nota2 = float(input("ingrese nota de presentación e informes: "))

    if nota2 >= 1.0 and nota2 <= 7.0:
        i = i + 1
    else:
        print("nota ingresada no es válida, las notas deben ser entre 1.0 y 7.0")

notaF = nota1 * 0.6 + nota2 * 0.4
notaF = round(notaF, 1)
print("el promedio final es: ", notaF)
