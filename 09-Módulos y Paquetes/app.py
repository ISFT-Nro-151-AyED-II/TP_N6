# MARCO PRÁCTICO
# ==============
# 9.1 Hacer un paquete simple.
# 9.2 Crear un directorio de aplicaciones.
# 9.3 Scripts de nivel superior.

# Para cumplir con todas las consignas necesitamos modificar la carpeta de trabajo y crear algunos archivos. 
#  La estructura del proyecto quedaría de la siguiente manera:

# 09-Módulos y Paquetes/       <-- (Directorio de aplicación - Punto 9.2).
# │
# ├── mi_paquete/              <-- (El Paquete Simple - Punto 9.1).
# │   ├── __init__.py
# │   └── operaciones.py
# │
# └── app.py                   <-- (Script de Nivel Superior - Punto 9.3).

# A continuación se crean los archivos __init__.py y operaciones.py dentro del directorio mi_paquete, y luego 
# se escribe el código necesario en cada uno de ellos.
# Y aquí, en el archivo app.py residirá el Script de Nivel Superior que importará y utilizará las funciones 
# definidas en el paquete mi_paquete.

# Importamos funciones específicas desde nuestro propio módulo.
from mi_paquete.operaciones import sumar, restar

def main():
    print("\n==========================================")
    print(" Sistema de Cálculo Sencillo Inicializado ")
    print("==========================================\n")

    num1 = 25
    num2 = 10
    
    # Delegamos el procesamiento al paquete.
    resultado_suma = sumar(num1, num2)
    resultado_resta = restar(num1, num2)
    
    print(f"El resultado de la suma ({num1} + {num2}) es: {resultado_suma}")
    print(f"El resultado de la resta ({num1} - {num2}) es: {resultado_resta}")

if __name__ == "__main__":
    main()