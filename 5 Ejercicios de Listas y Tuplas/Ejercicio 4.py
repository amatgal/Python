'''Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor.'''

nboleto = []
for i in range(5):
    nboleto.append(int(input("Introduce un número ganador: ")))
nboleto.sort()
print("Los números ganadores son: " + str(nboleto))