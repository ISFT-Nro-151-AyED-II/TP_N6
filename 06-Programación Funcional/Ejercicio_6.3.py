# MARCO PRÁCTICO
# ==============
# 6.3 Obtener la cantidad de elementos mayores a 5 en una tupla, usando reduce.

# Enfoque analítico: reduce() requiere importar functools. A diferencia de len(filter()), acá el acumulador 
# suma 1 si la condición se cumple, o se mantiene igual si no.

from functools import reduce

def main():
    valores = (2, 8, 4, 9, 5, 12, 1)
    
    # reduce(función, iterable, valor_inicial_del_acumulador)
    # La lambda recibe dos parámetros: el acumulador (acc) y el elemento actual (x).
    cantidad = reduce(lambda acc, x: acc + 1 if x > 5 else acc, valores, 0)
    
    print("\n================")
    print("Operación REDUCE")
    print("================\n")
    
    print(f"Tupla original: {valores}")
    print(f"Cantidad de elementos > 5 calculada con Reduce: {cantidad}")

if __name__ == "__main__":
    main()