x = 1
prime = 0
mayor = 0
menor = 0
num = 0

while x <= 10:
    num = int(input("ingrese numero " + str(x) + ": "))

    if num > 0 and x == 1:
        prime = num
        x = x + 1

    elif num <= prime and x != 1:
        menor = menor + 1
        x = x + 1
        
    elif num >= prime and x != 1:
        mayor = mayor + 1
        x = x + 1

    else:
        print("el numero ingresado debe ser mayor que cero")
        

print("los mayores que", prime, "son", mayor)
print("los menores que", prime, "son: ", menor)
