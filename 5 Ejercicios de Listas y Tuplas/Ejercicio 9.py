'''Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.'''

palabra = input("Escriba una palabra: ").lower()
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    print("La vocal " + vocal + " aparece " + str(palabra.count(vocal)) + " veces") 

