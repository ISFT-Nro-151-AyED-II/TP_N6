# MARCO PRÁCTICO
# ==============
# 4.1 Escribí un programa que pida dos números enteros y escriba cuáles números son pares y cuáles impares desde 
# el primero hasta el segundo.

# Enfoque analítico: Se evalúa la dirección del rango. Si el primero es mayor que el segundo, el bucle debe 
# decrementar (paso -1).

try:
    num1 = int(input("Ingresá el primer número entero: "))
    num2 = int(input("Ingresá el segundo número entero: "))
    
    print(f"\nAnalizando números desde {num1} hasta {num2}:\n")
    
    # Determinamos el paso del range dependiendo de si sube o baja.
    paso = 1 if num1 <= num2 else -1
    limite = num2 + 1 if num1 <= num2 else num2 - 1
    
    # Recorremos el rango desde num1 hasta num2 con el paso determinado.
    for i in range(num1, limite, paso):
        if i % 2 == 0:
            print(f"- El número {i} es PAR")
        else:
            print(f"- El número {i} es IMPAR")

except ValueError:
    print("Error crítico: Se esperaba el ingreso de números enteros.")