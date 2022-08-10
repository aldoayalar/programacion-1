miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
pos = []

for elemento in miLista:
    if elemento not in pos:
        pos.append(elemento)
#
print("La lista solo con elementos únicos:")
print(pos)

miLista = [1, 2, "in", True, "ABC"]

print(1 in miLista) # salida True
print("A" not in miLista) # salida True
print(3 not in miLista) # salida True
print(False in miLista) # salida False
