palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord
userWord = input("ingrese una palabra: ")

userWord = userWord.upper()
for letra in userWord:
    # Completa el cuerpo del ciclo.
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        continue
    else:
        palabraSinVocal += letra

# Imprimir la palabra asignada a palabraSinVocal.
print(palabraSinVocal)
