# MARCO PRÁCTICO
# ==============
# 7.5 Extra 1: Identificador no encontrado (NameError)

# Enfoque analítico: NameError ocurre cuando se intenta usar una variable o función que no ha sido definida.

print("\n======================")
print(" Excepción: NameError ")
print("======================\n")

def main():
    try:
        # variable_fantasma no fue declarada en ninguna parte del script.
        print(variable_fantasma)
    except NameError as e:
        print(f"Excepción capturada (NameError): {e}. Asegurate de inicializar las variables antes de usarlas.")

if __name__ == "__main__":
    main()