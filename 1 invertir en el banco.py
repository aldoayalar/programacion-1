#declaracion de valiables
capital = 0
cmes = 0
interes = 0

#usuario ingresa capital a invertir
capital = int(input("ingrese monto a invertir: "))
cmes = int(input("ingrese cantidad de meses: "))

interes = capital * 0.02 * cmes
capital = capital + interes

print(capital)

