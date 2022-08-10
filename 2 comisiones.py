base = 0
venta = 0

base = int(input("ingrese sueldo base: "))
venta = int(input("ingrese numero de ventas realizadas: "))

venta = base * 0.01 * venta
base = venta + base

print("el sueldo es:",base, "la comision fue de:",venta)



