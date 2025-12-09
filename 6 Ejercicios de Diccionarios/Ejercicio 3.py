'''Escribir un programa que guarde en un diccionario los precios de las frutas de la
tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
mostrar un mensaje informando de ello.'''

precios = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input("¿Qué fruta quieres?: ")
kilos = float(input("¿Cuántos kilos quieres?: "))
if fruta in precios:
    total = precios[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es {round(total,2)} euros.")
else:
    print("Lo siento, la fruta no esta disponible.")
