'''Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
diccionario generado con la función anterior y devuelva una tupla con la palabra más
repetida y su frecuencia.'''

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia                   
def palabra_mas_repetida(frecuencia):
    palabra_max = max(frecuencia, key=frecuencia.get)
    return (palabra_max, frecuencia[palabra_max])
cadena = "hola a todo el mundo voy con poco de todo"
frecuencia = contar_palabras(cadena)
print("Frecuencia de palabras:", frecuencia)
print("Palabra más repetida:", palabra_mas_repetida(frecuencia))    

