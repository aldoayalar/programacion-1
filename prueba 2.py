x = 1
y = 2

suma = 0

while x <= 11:
    if x % 2 == 1:
        print("+", x)
        suma = suma + x
        x = x + 2
        print("-", x)
        suma = suma - x

    else:
        print("+", y)
        suma = suma + y
        y = y + 2
        print("-", y)
        suma = suma - y
        y = y + 2

    x = x + 1
print("-------------")
print(suma)
