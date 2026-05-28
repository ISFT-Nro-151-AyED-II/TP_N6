# MARCO PRÁCTICO
# ==============
# 7.6 Extra 2: Error en tiempo de ejecución y sentencia raise (RuntimeError).

# Enfoque analítico: RuntimeError es una excepción genérica que ocurre cuando un error no entra en ninguna otra 
# categoría.
# Acá aprovechamos para mostrar qué es 'raise': nos permite a los programadores LANZAR una excepción de forma 
# manual si se viola una regla de negocio del sistema, sin que sea un error de sintaxis nativo de Python.

print("\n=========================")
print(" Excepción: RunTimeError ")
print("=========================\n")

def validar_edad_acceso(edad: int):
    if edad < 18:
        # Lanzamos intencionalmente la excepción.
        raise RuntimeError("Regla de Negocio: Acceso denegado. El usuario debe ser mayor de edad.")
    return "Acceso concedido."

def main():
    try:
        print("Intentando ingresar con 16 años...")
        resultado = validar_edad_acceso(16)
        print(resultado)
    except RuntimeError as e:
        print(f"Excepción capturada y lanzada manualmente (RuntimeError): {e}")

if __name__ == "__main__":
    main()