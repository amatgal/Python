'''Escribir un programa que pregunte por una muestra de números,
separados por comas, los guarde en una lista y muestre por pantalla 
su media y desviación típica.'''

numeros = input("Introduce una muestra de números separados por comas: ")
numeros = numeros.split(',')
n = len(numeros)
for i in range(n):
    numeros[i] = int(numeros[i])
numeros = tuple(numeros)            
media = sum(numeros)/n
suma_desv = 0
for i in range(n):
    suma_desv += (numeros[i] - media)**2
desviacion = (suma_desv/n)**0.5
print("La media es " + str(media))
print("La desviación típica es " + str(desviacion)) 