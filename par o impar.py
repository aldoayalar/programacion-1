#leer un número entero positivo
#(asuma que el número cumple las condiciones),
#imprimir PAR si el número es par e IMPAR si es impar.

num = 0

num = int(input("ingrese un numero: "))

if num % 2 == 0:
    print("Es par")
else:
    print("es impar")
