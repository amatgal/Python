'''Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es el día tiene un descuento del 60%. Escribir un
programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el
precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total.'''

precio_barras = 3.49
descuento = 0.60
barras_no_dia = input("Ingrese el número de barras vendidas que no son del día: ")
numero_barras_vendidas = int(barras_no_dia)
precio_descuento = precio_barras * descuento
precio_final = (precio_barras - precio_descuento) * numero_barras_vendidas 

print ("El precio habitual de una barra de pan es: ", precio_barras)
print ("El descuento por no ser fresca es de: ", precio_descuento)
print ("El coste final total es de: ", round(precio_final,2))
