
diccionario = {
    "hello": "hola",
    "goodbye": "adios",
    "thank you": "gracias",
    "please": "por favor",
    "dog": "perro",
    "cat": "gato",
    "house": "casa",
    "berry": "baya",
    "food": "comida",
    "water": "agua",
    'fox': 'zorro',
    'quick': 'rápido',
    'brown': 'marrón',
    'jumps': 'salta',
    'over': 'sobre',
    'lazy': 'perezoso',
    'fast': 'veloz',
    'fat': 'gordo',
}

palabra = input("Introduce una palabra en inglés: ").lower()

if palabra in diccionario:
    print("Traducción:", diccionario[palabra])
else:
    print("No conozco esa palabra")
