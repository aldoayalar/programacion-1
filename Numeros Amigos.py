# DESARROLLE UN PROGRAMA QUE SOLICITE DOS NúMEROS AL USUARIO Y  DESPLIEGUE SI SON AMIGOS
num1 = 1
num2 = 1
suma1 = 0
suma2 = 0

num1 = int(input("ingrese primer numero: "))
num2 = int(input("ingrese segundo numero: "))

x = 1
while x < num1:
    if num1 % x == 0:
        suma1 = suma1 + x
        print(x)
    x = x + 1

x = 1
while x < num2:
    if num2 % x == 0:
        suma2 = suma2 + x
    x = x + 1

#print(suma1, suma2)
if suma1 == num2 and suma2 == num1:
    print("son amigos")
else:
    print("no son amigos")
