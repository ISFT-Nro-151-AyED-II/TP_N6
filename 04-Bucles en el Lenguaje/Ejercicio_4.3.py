# MARCO PRÁCTICO
# ==============
# 4.3 Escribí un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras 
# no sea mayor que el primero. El programa terminará escribirndo los dos números.

# Enfoque analítico: Se captura el primer número fuera del bucle, y luego se fuerza la validación relacional 
# dentro del while.

try:
    num1 = int(input("Ingresá el primer número entero: "))
    
    while True:
        num2 = int(input(f"Ingresá un número mayor que {num1}: "))

        if num2 > num1:
            break
        else:
            print(f"Error: {num2} no es mayor que {num1}. Volvé a intentar.\n")
            
    print(f"\nProceso finalizado. Los números ingresados son: {num1} y {num2}")

except ValueError:
    print("Error crítico: Debés ingresar números enteros válidos.")