diccionario = { "Fresa":"strawberry",
                "hola": "hello",
                "adiós": "goodbye",
                "gracias": "thank you",
                "por favor": "please",
                "perro": "dog",
                "gato": "cat",
                "casa": "house",
                "baya": "berry",
                "comida": "food",
                "agua": "water"
            }

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
    "water": "agua"
}

palabra = input("Introduce una palabra en inglés: ").lower()

if palabra in diccionario:
    print("Traducción:", diccionario[palabra])
else:
    print("No conozco esa palabra")
