# MARCO PRÁCTICO
# ==============
# 7.1 Crear una función que divida hasta cero, ej: dividir(27, 0). Verificar: ZeroDivisionError.

# Enfoque analítico: Capturamos la excepción matemática para evitar la caída del sistema.

print("\n==============================")
print(" Excepción: ZeroDivisionError ")
print("==============================\n")

def dividir(numerador: float, denominador: float) -> float:
    """Retorna el resultado de la división."""
    return numerador / denominador

def main():
    try:
        resultado = dividir(27, 0)
        print(f"El resultado es {resultado}")
    except ZeroDivisionError as e:
        print(f"Error crítico evitado (ZeroDivisionError): No se puede dividir por cero. Detalle del motor: {e}")

if __name__ == "__main__":
    main()