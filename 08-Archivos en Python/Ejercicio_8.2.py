# MARCO PRÁCTICO
# ==============
# 8.2 Crear un programa que abra el fichero editado anteriormente y muestre el estado del fichero, el modo en 
# el que fue abierto, el nombre y la codificación de caracteres del mismo.

# Enfoque analítico: Python expone los metadatos del objeto file a través de sus atributos nativos.

def main():
    nombre_archivo = "mi_fichero.txt"
    try:
        # Solo necesitamos leer, por ende modo 'r'.
        fichero = open(nombre_archivo, "r", encoding="utf-8")
        
        print("\n==============================")
        print(" Metadatos del Objeto Fichero ")
        print("==============================\n")

        print(f"Nombre del archivo : {fichero.name}")
        print(f"Modo de apertura   : {fichero.mode}")
        print(f"Codificación       : {fichero.encoding}")
        print(f"¿Está cerrado?     : {fichero.closed} (antes de llamar a close())")
        
        fichero.close()
        
        print(f"¿Está cerrado?     : {fichero.closed} (después de llamar a close())")
        
    except FileNotFoundError:
        print("Error: El archivo no existe. Ejecutá primero el ejercicio 8.1.")

if __name__ == "__main__":
    main()