'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.'''

cantidad = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (en %): "))
n_años = int(input("Ingrese el número de años de la inversión: "))

for año in range(1, n_años + 1):
    cantidad *= (1 + interes_anual / 100)
    print(f"Al final del año {año}, el capital es: {cantidad:.2f}") 