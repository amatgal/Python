'''Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.'''

precio = input("Escribe el precio de un producto en euros con dos decimales: ")
euros = precio.split(".")[0]
centimos = precio.split(".")[1]
print("El precio del producto es de ", euros, "euros y", centimos, "céntimos")      