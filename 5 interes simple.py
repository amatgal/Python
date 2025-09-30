#Calcular el interes financiero
Capital_inicial = input("Introduce tu capital inicial: ")
Tasa_interes = input("Introduce la tasa de interes en porcentaje: ")
Tiempo = input("Introduce el periodo de tiempo: ")

Interes_calculo = float(Tasa_interes)/100*float(Capital_inicial)*float(Tiempo)
print (f"El interes conseguido es de: {Interes_calculo}")