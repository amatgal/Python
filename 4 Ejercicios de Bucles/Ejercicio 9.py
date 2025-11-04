'''Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.'''

almacen = "contraseña"
contraseña = ""

while contraseña != almacen:
    contraseña = input("Introduzca su contraseña: ")
print("Contraseña correcta")