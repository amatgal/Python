'''Escribir un programa que pregunte al usuario por el número de
horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde.'''

horas = float(input("¿Cuántas horas has trabajado? "))
coste = float(input("¿Cuánto cobras por hora? "))
paga = horas * coste
print("Tu paga es: " + str(paga) + "€")