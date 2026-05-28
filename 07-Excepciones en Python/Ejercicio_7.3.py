# MARCO PRÁCTICO
# ==============
# 7.3.Crear una lista e iterar más allá del límite del index. Verificar: IndexError.

# Enfoque analítico: Demostramos el desbordamiento de memoria lógico al pedir una posición de memoria que la estructura no reservó.

print("\n=======================")
print(" Excepción: IndexError ")
print("=======================\n")

def main():
    sistemas_operativos = ["Linux", "Windows", "macOS"]
    
    print(f"Tamaño de la lista: {len(sistemas_operativos)}")
    print("Iterando forzadamente hasta el índice 5...")
    
    try:
        for i in range(5):
            print(f"Índice {i}: {sistemas_operativos[i]}")
    except IndexError as e:
        print(f"\nExcepción capturada (IndexError): Te fuiste de los límites de la colección. Detalle: {e}")

if __name__ == "__main__":
    main()