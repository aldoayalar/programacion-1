prime = 0
mayor = 0
menor = 0
hasta = 0

x = 1
while x < 2:
    hasta = int(input("cuantos números quiere ingresar: "))
    if hasta > 0:
        x = 2
    else:
        print("el numero ingresado debe ser mayor que cero")

print("el primer numero ingresado se compara con los demas, a fin de determinar los mayores y menores que este")
prime = int(input("ingrese numero 1: "))

while x <= hasta:
    num = int(input("ingrese numero " + str(x) + ": "))

    if num < prime:
        menor = menor + 1
        x = x + 1

    elif num > prime:
        mayor = mayor + 1
        x = x + 1

    else:
        print("el numero ingresado debe ser diferente que el primero ingresado")

print("los mayores que", prime, "son", mayor)
print("los menores que", prime, "son: ", menor)
