#Distribuidora de alcoholes "Sito Man Boy"

#Declaracion de variables, no necesario en python
compra=0
cant=0
desc=0

#solicitud de datos
compra=int(input("ingrese valor de la compra: "))
cant=int(input("ingrese la cantidad de productos: "))

#condiciona descuento, mayor a $100.000.- o mas de 10 productos
if compra >= 100000 or cant >= 10 :

    desc=compra * 0.1
    compra=compra - desc

    print("el descuento es:", desc)
    print("total a pagar:", compra)

else:
    print("No corresponde descuento, total a pagar", compra)

