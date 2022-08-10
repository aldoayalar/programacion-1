#declaracion de variables
num1 = 0
num2 = 0
num3 = 0
invalido = "ha introducido numeros invalidos\nlos numeros deben ser diferentes"

#se solicitan numeros al usuario
#se asumen numeros diferentes
num1 = int(input("ingrese primer numero: "))
num2 = int(input("ingrese segundo numero: "))
num3 = int(input("ingrese tercer numero: "))

#consola debe mostrar los numeros de mayor a menor
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print("ordenados son", num1, ">",num2, ">", num3)
    elif num2 < num3:
        print("ordenados son", num1, ">",num3, ">", num2)
    else:
        print(invalido)
if num2 > num1 and num2 > num3:
    if num1 > num3:
        print("ordenados son", num2, ">",num1, ">", num3)
    elif num1 < num3:
        print("ordenados son", num2, ">",num3, ">", num1)
    else:
        print(invalido)
if num3 > num1 and num3 > num2:
    if num1 > num2:
        print("ordenados son", num3, ">",num1, ">", num2)
    elif num1 < num2:
        print("ordenados son", num3, ">",num2, ">", num1)
    else:
        print(invalido)
else:
    print(invalido)
