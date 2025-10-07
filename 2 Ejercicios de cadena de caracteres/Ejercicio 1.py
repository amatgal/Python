'''Escribir un programa que pregunte el nombre del usuario en la consola y un número
entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
como el número introducido.'''

nombre = input("Escriba su nombre: ")
numero = input("Escriba un número entero: ")
numero_entero = int(numero)
for i in range(numero_entero):
    print(nombre)   




