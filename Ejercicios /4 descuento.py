#Me dan un precio y un descuento y scsmbio devulve el precio ya rebajado
Descuento = input("Introduce el descuento que ofrecen: ")
Precio = input("Introduce el precio original: ")

precio_final = float(Precio)-float(Descuento)/100 * float(Precio)
print (f"El prcio final es: {precio_final}")