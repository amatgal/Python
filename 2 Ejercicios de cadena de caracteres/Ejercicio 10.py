'''Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta.'''

cesta = input("Escribe productos de la cesta de la compra, separados por comas: ")
lista = cesta.split(",")
print("\n".join(lista))
