'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>.'''

datos_usuario = {}
datos_usuario["nombre"] = input("Introduce tu nombre: ")
datos_usuario["edad"] = input("Introduce tu edad: ")
datos_usuario["dirección"] = input("Introduce tu dirección: ")
datos_usuario["teléfono"] = input("Introduce tu teléfono: ")
print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['dirección']} y su número de teléfono es {datos_usuario['teléfono']}.")
