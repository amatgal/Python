'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La
función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el
total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá
aplicar un 21%.'''

def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total = cantidad_sin_iva + iva
    return total
cantidad = float(input("Introduce la cantidad sin IVA: "))
porcentaje = input("Introduce el porcentaje de IVA (o deja en blanco para 21%): ")
if porcentaje:
    porcentaje = float(porcentaje)
    total_factura = calcular_total_factura(cantidad, porcentaje)
else:
    total_factura = calcular_total_factura(cantidad)
print(f"El total de la factura es: {total_factura:.2f} euros")  
