num = 1

contarPrimo = 1

while contarPrimo <= 20:

    divisibles = 0

    for x in range(1, num + 1, 1):

        if num % x == 0:
            divisibles = divisibles + 1

    if divisibles == 2:
        print(contarPrimo, "->", num, "Primo")

        contarPrimo = contarPrimo + 1

    num = num + 1
