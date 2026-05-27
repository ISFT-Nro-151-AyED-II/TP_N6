# MARCO PRÁCTICO
# ==============
# 4.4 Escribí un programa que pida dos números enteros y escribí la lista de números consecutivos que hay entre 
# ellos, de menor a mayor.

# Enfoque analítico: Se utilizan las funciones nativas min() y max() para garantizar el orden ascendente sin 
# importar cómo los ingresó el usuario.

try:
    numA = int(input("Ingresá el primer número entero: "))
    numB = int(input("Ingresá el segundo número entero: "))
    
    # min y max se encargan de determinar cuál es el menor y cuál es el mayor, independientemente del orden de 
    # entrada.
    menor = min(numA, numB)
    mayor = max(numA, numB)
    
    # Se utiliza una lista por comprensión para almacenar la secuencia (excluyendo los límites, ya que pide 
    # los que están "entre" ellos).
    consecutivos = [i for i in range(menor + 1, mayor)]
    
    print(f"\nLos números consecutivos entre {menor} y {mayor} son:")
    print(consecutivos if consecutivos else "No hay números enteros entre ellos.")

except ValueError:
    print("Error crítico: Debés ingresar números enteros válidos.")