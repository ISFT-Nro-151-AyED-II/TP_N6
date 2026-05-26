# 📚 Marco Práctico 3: Colecciones en el Lenguaje

**Desarrollo Práctico en Python (Ejecución de Scripts Locales):**

### 🔢 3.1. Valores del 1 al 100 en una lista
> 💡 **Enfoque técnico:** Se utilizó la función `range(1, 101)` convertida a `list`. Es la forma más optimizada y pythónica de generar secuencias numéricas sin iterar manualmente. Para no saturar la salida, se imprimen los extremos de la lista.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\03-Colecciones en el Lenguaje>python Ejercicio_3.1.py
Lista generada con éxito. Primeros y últimos 5 elementos:
Inicio: [1, 2, 3, 4, 5] ... Fin: [96, 97, 98, 99, 100]
```

### 📅 3.2. Tupla de meses y consulta por índice
> 💡 **Enfoque técnico:** Se implementó una tupla debido a la inmutabilidad de los datos (los meses no varían). Se restó 1 al input del usuario porque los índices en Python comienzan en 0. Se agregó manejo de excepciones (`ValueError`) para evitar caídas del sistema por ingresos de texto.

**Prueba Exitosa:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\03-Colecciones en el Lenguaje>python Ejercicio_3.2.py
Ingresá un número de mes (1-12): 12
El mes correspondiente es: Diciembre
```

**Prueba Fuera de Rango:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\03-Colecciones en el Lenguaje>python ejercicio_3_2.py
Ingresá un número de mes (1-12): 15
Error: El número ingresado está fuera de rango.
```

### ✖️ 3.3. Tabla de multiplicar en una lista
> 💡 **Enfoque técnico:** Se utilizó *List Comprehension* (`[num * i for i in range(1, 11)]`), lo que permite iterar y poblar la lista en una sola operación atómica, mejorando la legibilidad y el rendimiento del algoritmo.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\03-Colecciones en el Lenguaje>python Ejercicio_3.3.py
Ingresá un número para calcular su tabla: 5
La tabla del 5 guardada en la lista es:
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

### 📖 3.4. Diccionario de contactos
> 💡 **Enfoque técnico:** Se usó un diccionario (`dict`) donde las claves (`keys`) son los nombres. Esto garantiza una búsqueda en tiempo constante $O(1)$ para la validación de duplicados (operador `in`). El bucle se controla con un `while True` y la sentencia `break` para salir.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\03-Colecciones en el Lenguaje>python ejercicio_3.4.py

===================
GESTOR DE CONTACTOS
===================

Ingresá el nombre del contacto (o escribí 'salir' para terminar): David
Ingresá el teléfono de Elena: 223 555 1234
Contacto agregado con éxito.

Ingresá el nombre del contacto (o escribí 'salir' para terminar): Ana
Ingresá el teléfono de David: 223 555-9876
Contacto agregado con éxito.

Ingresá el nombre del contacto (o escribí 'salir' para terminar): Elena
Ese nombre ya existe en la agenda. No se admiten duplicados.
Ingresá el nombre del contacto (o escribí 'salir' para terminar): salir

LISTA FINAL DE CONTACTOS
========================

- Elena: 223 555-1234
- David: 223 555-9876
```