'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.'''

num = int(input("Ingrese un número entero: "))
i = 2
while num % i != 0:
    i += 1
if i == num:
    print(str(num) + " es primo")
else:
    print (str(num) + " no es primo ")