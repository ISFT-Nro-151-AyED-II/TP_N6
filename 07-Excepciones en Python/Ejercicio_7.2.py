# MARCO PRÁCTICO
# ==============
# 7.2 Llamar a la función mas_10() con cualquier número. Verificar TypeError (ej: add_10(“cinco”)).

# Enfoque analítico: Demostramos cómo Python maneja el tipado dinámico fuerte. No permite operar un entero con 
# un string.

print("\n======================")
print(" Excepción: TypeError ")
print("======================\n")

def mas_10(valor):
    """Suma 10 al valor ingresado."""
    return valor + 10

def main():
    print("Prueba 1: Ejecución normal")
    print(f"mas_10(15) = {mas_10(15)}")
    
    print("\nPrueba 2: Forzando el TypeError")
    try:
        # Intentamos sumar un string y un entero.
        resultado = mas_10("cinco")
        print(resultado)
    except TypeError as e:
        print(f"Excepción capturada (TypeError): Discrepancia de tipos de datos. Detalle: {e}")

if __name__ == "__main__":
    main()