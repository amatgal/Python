'''Escribir una función que convierta un número decimal en binario y otra que convierta
un número binario en decimal.'''

def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    return binario  
def binario_a_decimal(b):
    decimal = 0
    potencia = 0
    for digito in reversed(b):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal
num_decimal = 10
num_binario = "1010"
print("Decimal a binario:", decimal_a_binario(num_decimal))
print("Binario a decimal:", binario_a_decimal(num_binario))     

