promedio = 0.0
examen = 0.0
trabajo = 0.0

promedio = float(input("ingrese promedio de los 3 parciales: "))
examen = float(input("ingrese calificación del examen final: "))
trabajo = float(input("ingrese calificación del trabajo final: "))

promedio = promedio * 0.55
examen = examen * 0.3
trabajo = trabajo * 0.1

print("la nota final es: ", round(promedio + examen + trabajo, 2))
