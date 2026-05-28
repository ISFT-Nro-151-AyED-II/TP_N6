# MARCO PRÁCTICO
# ==============
# 7.4.Crear un diccionario en Python y buscar una clave inexistente. Verificar: KeyError.

# Enfoque analítico: Los diccionarios explotan si se busca directamente una clave (key) que no existe.

print("\n=====================")
print(" Excepción: KeyError ")
print("=====================\n")

def main():
    configuracion = {"host": "localhost", "puerto": 3306}
    
    try:
        print(f"Host: {configuracion['host']}")
        # Buscamos una clave que no declaramos.
        print(f"Usuario: {configuracion['usuario']}")
    except KeyError as e:
        print(f"Excepción capturada (KeyError): La clave solicitada {e} no se encuentra en el diccionario.")

if __name__ == "__main__":
    main()