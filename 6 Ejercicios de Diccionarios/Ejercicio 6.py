'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
debe imprimirse el contenido del diccionario.'''

vacio = {}
vacio["nombre"] = input("Introduce tu nombre: ")
print(vacio)
vacio["edad"] = input("Introduce tu edad: ")
print(vacio)
vacio["sexo"] = input("Introduce tu sexo: ")
print(vacio)
vacio["teléfono"] = input("Introduce tu teléfono: ")
print(vacio)
vacio["correo electrónico"] = input("Introduce tu correo electrónico: ")
print(vacio)
print("Diccionario completo:",vacio)
