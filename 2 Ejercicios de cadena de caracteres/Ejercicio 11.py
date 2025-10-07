'''Escribir un programa que pregunte el nombre el un producto, su precio y un número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''

producto = input("Escribe el nombre del producto: ")
precio = input("Escribe el precio del producto: ")
cantidad = input("Introduce la cantidad del productos que quieres comprar:  ")
coste_total = float(precio) * int(cantidad)
print(f"{producto}: {float(precio):09.2f}€ x {int(cantidad):03d} unidades = {coste_total:010.2f}€")      
