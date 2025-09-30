#Calcular el perimetro y el área de un rectangulo
base = input ("Introduce la longitud de la base del rectangulo: ")
altura = input ("Introduce la longitud de la altura del rectangulo: ")
perimetro = float(base)*2 + float(altura)*2
area = float(base) * float(altura)
print (f"El perimetro del rectangulo es: {perimetro}")
print (f"El area del rectangulo es: {area}")