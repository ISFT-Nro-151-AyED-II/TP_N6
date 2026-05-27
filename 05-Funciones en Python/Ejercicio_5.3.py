# MARCO PRÁCTICO
# ==============
# 5.3 Escribir un programa que permita crear una lista de palabras (que puede estar vacía). Para ello, el 
# programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, 
# el programa tiene que escribir la lista.

# Enfoque analítico: Separamos la recolección de datos en una función específica que retorna la colección armada.

def crear_lista_palabras(cantidad: int) -> list:
    """Itera 'cantidad' veces pidiendo palabras al usuario y retorna la lista generada."""
    palabras = []
    # Nota: -> list indica que la función retorna una lista, pero no especifica el tipo de elementos que contiene.
    for i in range(cantidad):
        palabra = input(f"Ingresá la palabra {i + 1}: ")
        # Nota: palabras.append(palabra) agrega la palabra ingresada a la lista 'palabras'. Este método es 
        # eficiente para construir listas dinámicamente.
        palabras.append(palabra)
    return palabras

def main():
    try:
        cantidad = int(input("¿Cuántas palabras querés agregar a la lista?: "))
        
        if cantidad < 0:
            print("Error: No podés crear una lista con una cantidad negativa de elementos.")
            return
            
        # El programa tiene que escribir la lista. Para esto, llamamos a la función 'crear_lista_palabras' 
        # con la cantidad ingresada por el usuario y luego imprimimos el resultado.
        lista_final = crear_lista_palabras(cantidad)
        print(f"\nLa lista creada es: {lista_final}")
        
    except ValueError:
        print("Error crítico: Tenés que ingresar un número entero.")

if __name__ == "__main__":
    main()