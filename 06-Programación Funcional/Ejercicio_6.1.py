# MARCO PRÁCTICO
# ==============
# 6.1 Obtener el cuadrado de todos los elementos de una lista.

# Enfoque analítico: map() aplica la función lambda (x elevado al cuadrado) a cada elemento del iterable.

def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # map() retorna un iterador, por lo que es necesario castearlo a list() para visualizarlo.
    cuadrados = list(map(lambda x: x**2, numeros))
    
    print("\n=============")
    print("Operación MAP")
    print("=============\n")
    
    print(f"Lista original de números: {numeros}")
    print(f"Elementos elevados al cuadrado: {cuadrados}")

if __name__ == "__main__":
    main()