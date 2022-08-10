x = 1
z = 3
suma = 1

while x <= 9:
    print("+", x)
    print("-", z)

    x = x + suma
    z = z + suma

    if suma == 1:
        suma = 3
    else:
        suma = 1
