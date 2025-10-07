'''Imagina que acabas de abrir una nueva cuenta de ahorros que
te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la
cuenta de ahorros, introducida por el usuario. Después el
programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer años. Redondear cada
cantidad a dos decimales.'''

cantidad = float(input("Ingrese la cantidad a depositar en la cuenta de ahorros: "))
interes_anual = 0.04  
primer_año = cantidad * (1 + interes_anual)
segundo_año = primer_año * (1 + interes_anual)
tercer_año = segundo_año * (1 + interes_anual)

print ("La cantidad ahorrada el primer año es de: {:.2f}".format(primer_año))
print ("La cantidad ahorrada el segundo año es de: {:.2f}".format(segundo_año))
print ("La cantidad ahorrada el tercer año es de: {:.2f}".format(tercer_año))
