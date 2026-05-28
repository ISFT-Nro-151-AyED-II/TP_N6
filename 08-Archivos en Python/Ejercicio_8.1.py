# MARCO PRÁCTICO
# ==============
# 8.1 Crear un programa que abra un fichero en modo lectura y escritura; si no existe lo creará y añadir la 
# frase: “Estoy aprendiendo Python”.

# Enfoque analítico: El modo 'a+' (append + read) es el único que cumple los tres requisitos estrictos:
# 1) Permite escribir (añadir al final sin borrar lo anterior). 2) Permite leer. 3) Crea el archivo si no existe.
# Siempre definimos el encoding="utf-8" para evitar dolores de cabeza con caracteres especiales.

def main():
    nombre_archivo = "mi_fichero.txt"
    try:
        fichero = open(nombre_archivo, "a+", encoding="utf-8")
        fichero.write("Estoy aprendiendo Python\n")
        print(f"\nFrase añadida con éxito en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error inesperado al manipular el archivo: {e}")
    finally:
        # El bloque finally garantiza que el archivo se cierre, pase lo que pase.
        fichero.close()

if __name__ == "__main__":
    main()