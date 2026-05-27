# MARCO PRÁCTICO
# ==============
# 5.2 Escribir un programa que pida un año y que escriba si es bisiesto o no.
# Nota: Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los 
# múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 Es Bisiesto, 2010 No es Bisiesto, 
# 2000 Es Bisiesto, 1900 No es Bisiesto.

# Enfoque analítico: La función retorna un booleano (True/False) en lugar de imprimir directamente. Esto hace que 
# la función sea escalable y reutilizable.

def es_bisiesto(anio: int) -> bool:
    """Evalúa las condiciones matemáticas para determinar si un año es bisiesto."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    # lógica: un año es bisiesto si es divisible por 4 y no es divisible por 100, o si es divisible por 400.

def main():
    try:
        anio = int(input("Ingresá un año para verificar si es bisiesto: "))
        
        if anio < 0:
            print("Error: Ingresá un año válido (positivo).")
            return
            
        if es_bisiesto(anio):
            print(f"El año {anio} ES bisiesto.")
        else:
            print(f"El año {anio} NO es bisiesto.")
            
    except ValueError:
        print("Error crítico: El año debe ser un número entero.")

if __name__ == "__main__":
    main()