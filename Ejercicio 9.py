'''Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión.'''

cantidad = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (en %): "))
num_años = int(input("Ingrese el número de años: "))
capital_obtenido = cantidad * (1 + interes_anual / 100) ** num_años
print(f"El capital obtenido después de {num_años} años es: {capital_obtenido:.2f}")
