# MARCO PRÁCTICO
# ==============
# Creá una tupla con los meses del año, pedile números al usuario, si el número está entre 1 y la 
# longitud máxima de la tupla, mostrá el contenido de esa posición sino mostrá un mensaje de error.

# Usamos una tupla porque los meses son una colección inmutable (no cambian).

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

try:
    numero = int(input("Ingresá un número de mes (1-12): "))
    # Validamos que el número esté entre 1 y la longitud de la tupla (12).
    if 1 <= numero <= len(meses):
        print(f"El mes correspondiente es: {meses[numero - 1]}")
    else:
        print("Error: El número ingresado está fuera de rango.")
        
except ValueError:
    print("Error: Tenés que ingresar un número entero válido.")