# MARCO PRÁCTICO
# ==============
# 3.3 Pedí un número por teclado y guardá en una lista su tabla de multiplicar hasta el 10. Por ejemplo, 
# si pide el 5 la lista tendrá: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.

# Aplicamos List Comprehension para generar la lista en una sola línea lógica.

try:
    num = int(input("Ingresá un número para calcular su tabla: "))
    tabla = [num * i for i in range(1, 11)]
    print(f"La tabla del {num} guardada en la lista es:\n{tabla}")
    
except ValueError:
    print("Error: Ingreso inválido. Se esperaba un número entero.")