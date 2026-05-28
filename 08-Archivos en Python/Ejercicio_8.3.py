# MARCO PRÁCTICO
# ==============
# 8.3.Realizar un programa que realice los ejercicios 8.1 y 8.2 utilizando la estructura with.

# Enfoque analítico: El 'with' (Context Manager) delega el control de los recursos al intérprete. 
# Automáticamente invoca el método __enter__() al abrir y __exit__() al terminar el bloque, cerrando el archivo.

def main():
    nombre_archivo = "fichero_with.txt"
    
    print("\n================================")
    print(" Ejecutando con Estructura WITH ")
    print("================================\n")

    # Equivalente al Punto 1.
    with open(nombre_archivo, "a+", encoding="utf-8") as archivo:
        archivo.write("Estoy aprendiendo Python usando WITH\n")
        print("Frase añadida correctamente.\n")
        
        # Equivalente al Punto 2 (dentro del contexto).
        print("Metadatos del Archivo (Dentro del bloque)")
        print("-----------------------------------------\n")

        print(f"Nombre       : {archivo.name}")
        print(f"Modo         : {archivo.mode}")
        print(f"Codificación : {archivo.encoding}")
        print(f"Estado cerrado: {archivo.closed}")
    
    # Verificación fuera del contexto.
    print(f"\nFuera del bloque WITH. Estado cerrado: {archivo.closed}")

if __name__ == "__main__":
    main()