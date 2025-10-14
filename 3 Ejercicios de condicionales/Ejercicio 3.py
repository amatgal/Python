'''Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.'''

numero1 = int(input("Introduce un numero que va a actuar como dividendo: "))
numero2 = int(input("Introduce otro numero que va a actuar como divisor: "))

print ("La division es: ", float(numero1/numero2))

if numero2 == 0:
    print ("Error")
