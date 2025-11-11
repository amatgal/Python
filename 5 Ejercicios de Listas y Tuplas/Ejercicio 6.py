'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir.'''

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "? "))
    notas.append(nota) 
for i in range(len(asignaturas)-1, -1, -1):
    if notas[i] >= 5:
        del asignaturas[i]
print("Tienes que repetir las siguientes asignaturas: " + str(asignaturas))
 
