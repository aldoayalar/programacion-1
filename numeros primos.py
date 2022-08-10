num = 0
count = 0

num = int(input("ingrese numero a evaluar: "))

x = 1
while x <= num:
    if num % x == 0:
        count = count + 1

    x = x + 1
print(num, "tiene", count, "divisores")
if count == 2:
    print("is cousin")
else:
    print("not cousin")
