'''Escribir una función que calcule el máximo común divisor de dos números y otra que
calcule el mínimo común múltiplo.'''

def maximo_comun_divisor(a, b):
    while b:
        a, b = b, a % b
    return a    
def minimo_comun_multiplo(a, b):
    return abs(a * b) // maximo_comun_divisor(a, b)
num1 = 12
num2 = 15
print("Máximo común divisor:", maximo_comun_divisor(num1, num2))    
print("Mínimo común múltiplo:", minimo_comun_multiplo(num1, num2))
    