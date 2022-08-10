x = 1
while x <= 10:
    print(x, end='->')
    x = x + 1
    if x % 2 != 0:
        print("par")
    else:
        print("impar")
