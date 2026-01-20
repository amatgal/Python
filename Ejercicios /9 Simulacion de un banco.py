opcion = 0
saldo = 1000

def mostrar_saldo(saldo):
    print(f"Su saldo actual es: {saldo} euros")
def ingresar_dinero(saldo):
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    saldo += cantidad
    print(f"Ha ingresado {cantidad} euros.")
    return saldo
def retirar_dinero(saldo):
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= cantidad
        print(f"Ha retirado {cantidad} euros.")
    return saldo    
while opcion != 4:
    print("\n--- Menú del Banco ---")
    print("1. Mostrar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        mostrar_saldo(saldo)
    elif opcion == 2:
        saldo = ingresar_dinero(saldo)
    elif opcion == 3:
        saldo = retirar_dinero(saldo)
    elif opcion == 4:
        print("Gracias por usar el banco. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        