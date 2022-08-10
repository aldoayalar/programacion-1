x = 1
n = 0
mayor = 0
num = 0

n = int(input('cuantos numeros: '))

while x <= n:
	num = int(input('ingrese numero: '))
	if num >= mayor or x == 1:
		mayor = num
		
	x = x + 1
	
print('el numero mayor es: ', mayor)
