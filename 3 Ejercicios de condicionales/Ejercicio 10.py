'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
● Ingredientes vegetarianos: Pimiento y tofu.
● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''

pizza = input("Ingrese el tipo de pizza que desea vegana / no vegana: ")
if pizza == "vegana":
    print("Los ingredientes disponibles son: Pimiento y tofu")
    ingrediente = input("Ingrese el ingrediente que desea: ")
    print("Su pizza es vegana y lleva mozzarella, tomate y " + ingrediente)
else:
    print("Los ingredientes disponibles son: Peperoni, Jamón y Salmón")
    ingrediente = input("Ingrese el ingrediente que desea: ")
    print("Su pizza no es vegana y lleva mozzarella, tomate y " + ingrediente)

