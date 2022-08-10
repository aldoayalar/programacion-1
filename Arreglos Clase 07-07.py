import numpy as np

a = np.array([3, 7, 1, 5, 8, 4])

print(a)

for n in range(10):

    num = int(input("Ing. número :"))

    for x in range(5, 0, -1):
        a[x] = a[x - 1]

    a[0] = num

print(a)

