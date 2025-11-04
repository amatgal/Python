'''Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.'''

num = int(input("Introduce un numero entero positivo: "))

for i in range(num):
    for j in range(i + 1):
        print("*", end="")
    print()

