import numpy as np

a = np.array([2, 5, 7, 1, 4, 9])

print(a)

for i in range(11):
    for j in range(6):
        a[5 - j] = a[4 - j]

    #a[0] = int(input("ingrese numero " + str(i) + "-> "))
    print(a)

