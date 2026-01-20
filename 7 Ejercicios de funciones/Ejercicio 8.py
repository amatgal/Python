'''Escribir una función que reciba una muestra de números en una lista y devuelva un
diccionario con su media, varianza y desviación típica.'''

lista = [1,2,3,4,5]
def calcular_estadisticas(numeros):
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    desviacion_tipica = varianza ** 0.5
    return {
        'media': media,
        'varianza': varianza,
        'desviacion_tipica': desviacion_tipica
    }
print(calcular_estadisticas(lista))

