# MARCO PRÁCTICO
# ==============
# 4.2 Pedí un número positivo al ususario una y otra vez hasta que el usuario lo haga correctamente.

# Enfoque analítico: Bucle While infinito que se rompe (break) solo cuando se cumple la condición de negocio 
# (número > 0).

while True:
    try:
        numero = float(input("Ingresá un número estrictamente positivo: "))

        if numero > 0:
            print(f"Correcto. Ingresaste {numero}, el cual es positivo.")
            break
        else:
            print("Error: El número debe ser mayor a 0. Intentá de nuevo.\n")

    except ValueError:
        print("Error: Ingreso inválido. Por favor, escribí un número.\n")