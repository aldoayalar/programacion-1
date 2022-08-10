#declaracion de variables
nota1=0.0
nota2=0.0
nota3=0.0
prom=0.0

#se solicita al usuario ingresar 3 notas
nota1=float(input("ingrese primera nota: "))
nota2=float(input("ingrese segunda nota: "))
nota3=float(input("ingrese tercera nota: "))

#se aceptan solo notas validas entre 1.0 y 7.0
if nota1 >= 1.0 and nota1 <= 7.0 and nota2 >= 1.0 and nota2 <= 7.0 and nota3 >= 1.0 and nota3 <= 7.0:
    prom = (nota1 + nota2 + nota3) / 3
    prom = round(prom, 2)

#si las notas son validas, indica si aprueba o reprueba
    if prom <= 4.0:
        print("reprobado con nota: ", prom)
    else:
        print("aprobado, con nota: ", prom)

#si las notas no son validas, le indica volver a comenzar y el rango de notas validas
else:
    print("ha introducido notas invalidas, las notas deben ser entre 1.0 y 7.0")
    print("vuelva a ingresar las notas")
