# MARCO PRÁCTICO
# ==============
# 6.2 Obtener la cantidad de elementos mayores a 5 en una tupla.

# Enfoque analítico: filter() extrae solo los elementos que devuelven True en la evaluación lógica de la lambda.

def main():
    valores = (2, 8, 4, 9, 5, 12, 1)
    
    # filter() también retorna un iterador. Lo casteamos a tuple para respetar el tipo de dato original.
    mayores_a_cinco = tuple(filter(lambda x: x > 5, valores))
    
    # La cantidad se obtiene con la función nativa len().
    cantidad = len(mayores_a_cinco)
    
    print("\n================")
    print("Operación FILTER")
    print("================\n")

    print(f"Tupla original: {valores}")
    print(f"Elementos filtrados (> 5): {mayores_a_cinco}")
    print(f"Cantidad de elementos obtenidos: {cantidad}")

if __name__ == "__main__":
    main()