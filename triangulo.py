x = 1
z = 1

while x < 9:
    print(x, end="  ")
    while z <= x:
        print(z, end="  ")
        z = z + 1
    print()
    z = 1
    x = x + 1

while x > 0:
    print(x, end="  ")
    while z <= x:
        print(z, end="  ")
        z = z + 1
    print()
    z = 1
    x = x - 1