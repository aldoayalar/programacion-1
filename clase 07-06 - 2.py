x = 1
n = 1000
suma = 0

while x <= n:
    if x % 2 != 0:
        print("+"+str(x))
        suma = suma + x
    else:
        print("-"+str(x))
        suma = suma - x
    x = x + 1
print("--------------------")
print("resultado operatoria", suma)

print("prueba")