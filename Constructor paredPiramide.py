bloques = 0
bloques = int(input("Ingrese el número de bloques:"))
altura = 0
x = 1
while x <= bloques:
    bloques -= x
    altura += 1
    x += 1
print("La altura de la pirámide:", altura)
