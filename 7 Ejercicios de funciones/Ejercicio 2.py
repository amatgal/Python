'''Escribir una función a la que se le pase una cadena <nombre> y muestre por
pantalla el saludo ¡hola <nombre>!.'''

def saludar(nombre):
    print("Hola " + nombre)   
nombre = input("Introduce tu nombre: ")
saludar(nombre)