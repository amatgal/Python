'''Escribir una función que reciba un número entero positivo y devuelva su factorial.'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Introduce un número entero positivo: "))
if num < 0:
    print("El número debe ser positivo.")
else:
    print(f"El factorial de {num} es {factorial(num)}") 
