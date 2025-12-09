'''Escribir un programa que cree un diccionario simulando una cesta de la compra. El
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
compra y el coste total, con el siguiente formato'''

cesta = {}
while True:
    articulo = input("Introduce el artículo (o 'fin' para terminar): ")
    if articulo == 'fin':
        break
    precio = float(input(f"Introduce el precio de {articulo}: "))
    cesta[articulo] = precio
total = sum(cesta.values())
print("\nLista de la compra:")
for articulo, precio in cesta.items():
    print(f"- {articulo}: {precio} euros")
print(f"Coste total: {total} euros")
