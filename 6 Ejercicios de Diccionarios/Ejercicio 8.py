'''Escribir un programa que cree un diccionario de traducción español-inglés. El
usuario introducirá las palabras en español e inglés separadas por dos puntos, y
cada par <palabra>:<traducción> separados por comas. El programa debe
crear un diccionario con las palabras y sus traducciones. Después pedirá una frase
en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra
no está en el diccionario debe dejarla sin traducir.'''

palabras = input("Introduce las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas: ")
traducciones = {}
for palabra in palabras.split(','):
    esp, ing = palabra.split(':')
    traducciones[esp.strip()] = ing.strip()
frase = input("Introduce una frase en español: ")
frase_traducida = []
for palabra in frase.split():
    frase_traducida.append(traducciones.get(palabra, palabra))
print("Frase traducida:", ' '.join(frase_traducida))    


