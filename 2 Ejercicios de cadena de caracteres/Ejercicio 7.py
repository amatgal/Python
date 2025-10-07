'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
de la arroba @) pero con dominio ceu.es.'''

correo = input("Escribe tu correo electrónico: ")
nombre_user = correo.split("@")[0]
nuevo_correo = nombre_user + "@ceu.es"
print("Tu nuevo correo es: ", nuevo_correo)
