'''Escribir una función que reciba una muestra de números en una lista y devuelva otra
lista con sus cuadrados.'''

lista = [1,2,3,4,5]

def calcular_cuadrados(numeros):
    cuadrados = []
    for numero in numeros:
        cuadrados.append(numero ** 2)
    return cuadrados

print(calcular_cuadrados(lista))
