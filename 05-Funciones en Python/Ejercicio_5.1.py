# MARCO PRÁCTICO
# ==============
# 5.1.Escribir un programa que pida la anchura y altura de un rectángulo y el caracter a utilizar en el dibujo.

# Enfoque analítico: Se define una función pura que se encarga exclusivamente de renderizar, aislando la lógica 
# del input del usuario.

def dibujar_rectangulo(ancho: int, alto: int, caracter: str) -> None: 
    """Imprime un rectángulo en consola usando el ancho, alto y caracter dados."""
    for _ in range(alto):
        print(caracter * ancho)
# Nota: -> None indica que la función no devuelve ningún valor, solo realiza una acción (imprimir).

def main():
    try:
        ancho = int(input("Ingresá la anchura del rectángulo: "))
        alto = int(input("Ingresá la altura del rectángulo: "))
        caracter = input("Ingresá el caracter a utilizar: ")
        
        if ancho <= 0 or alto <= 0:
            print("Error: La anchura y altura deben ser enteros positivos.")
            return
            
        if len(caracter) != 1:
            print("Error: Debés ingresar exactamente un (1) caracter.")
            return
            
        print("\nResultado:")
        dibujar_rectangulo(ancho, alto, caracter)
        
    except ValueError:
        print("Error crítico: Anchura y altura deben ser números enteros.")

if __name__ == "__main__":
    main()