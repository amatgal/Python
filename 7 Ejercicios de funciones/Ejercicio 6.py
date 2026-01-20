'''Escribir una función que reciba una muestra de números en una lista y devuelva su
media.'''

lista = [1,2,3,4,5]

def calcular_media(numeros):
    return (sum(numeros) / len(numeros))

print(calcular_media(lista))