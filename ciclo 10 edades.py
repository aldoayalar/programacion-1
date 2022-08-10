#declaracion de variables
edad = 0
menor = 0
adulto = 0
aMayor = 0

#inicializacion
i = 1
#ciclo
while i <= 10:
    print("ingrese edad",i)
    edad = int(input("->"))
    #Menores de edad
    if edad >= 0 and edad <= 17:
        menor = menor + 1
        i = i + 1
    #Adultos
    elif edad >= 18 and edad <= 60:
        adulto = adulto + 1
        i = i + 1
    #Adultos Mayores
    elif edad >= 61 and edad <= 130:
        aMayor = aMayor +1
        i = i + 1
    #todas las opciones ingresadas son invalidas
    else:
        print("edad ingresada no es válida, vuelva a ingresar edad ")

#mostrar en pantalla estadística
print("los menores de edad son:", menor)
print("los adultos son:", adulto)
print("los adultos mayores son:", aMayor)

print("fin del programa")
