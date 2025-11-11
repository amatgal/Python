'''Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.'''

while True:
    texto = input("Escribe algo (escribe 'salir' para terminar): ")
    if texto.lower() == "salir":
        break
    print(texto)
    
        