'''Escribir un programa que pida al usuario que introduzca una frase en la consola y
una vocal, y después muestre por pantalla la misma frase pero con la vocal
introducida en mayúscula.'''

frase = input("Escribe una frase: ")
vocal = input("Esribe una vocal: ")
frase_cambiada = frase.replace(vocal, vocal.upper())
print ("La frase cambiada es: ", frase_cambiada)
