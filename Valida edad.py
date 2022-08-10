edad = 0
adultos = 0
menor = 0
am = 0
x = 1
while x <= 10:
    print("Ingrese edades", x)
    edad = int(input())
    if edad > 0:
        if edad <= 17:
            menor = menor + 1
        else:
            if edad <= 60:
                adultos = adultos + 1
            else:
                am = am + 1
        x = x + 1
    else:
        print("debe ingresar un número válido")

print("menores", menor)
print("adultoooo", adultos)
print("esta es una persona mayor, no por morir", am)