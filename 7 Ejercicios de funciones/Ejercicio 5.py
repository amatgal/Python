'''Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función.'''

def area_circulo(radio):
    import math
    return math.pi * radio ** 2
def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)
    volumen = area_base * altura
    return volumen
radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))
volumen = volumen_cilindro(radio, altura)
print(f"El volumen del cilindro es: {volumen:.2f}")