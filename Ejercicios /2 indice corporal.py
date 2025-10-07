def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    Fórmula: IMC = peso (kg) / (altura (m))^2
    """
    return peso / (altura ** 2)

# Programa principal
try:
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))

    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")

    # Clasificación según la OMS
    if imc < 18.5:
        print("Clasificación: Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Clasificación: Peso normal")
    elif 25 <= imc < 29.9:
        print("Clasificación: Sobrepeso")
    else:
        print("Clasificación: Obesidad")
except ValueError:
    print("Por favor, introduce valores numéricos válidos.")
