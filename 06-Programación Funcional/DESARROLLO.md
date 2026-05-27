# ⚙️ Marco Práctico 6: Programación Funcional en Python

**Desarrollo Práctico en Python (Ejecución de Scripts Locales):**

### 🧮 6.1. Cuadrado de elementos con MAP
> 💡 **Enfoque técnico:** Se aplicó la función de orden superior `map()` junto con una función anónima `lambda x: x**2`. Esta combinación proyecta la transformación matemática sobre cada elemento de la lista original $O(N)$ en tiempo de ejecución, delegando la iteración al motor interno de Python.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\06-Programación Funcional>python Ejercicio_6.1.py

=============
Operación MAP
=============

Lista original de números: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Elementos elevados al cuadrado: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 🔍 6.2. Cantidad de elementos mayores a 5 con FILTER
> 💡 **Enfoque técnico:** Se utilizó `filter()` con el predicado `lambda x: x > 5`. A diferencia de `map`, `filter` no transforma los datos, sino que descarta aquellos que evalúan a `False`. Finalmente, se utilizó `len()` para obtener la métrica solicitada (cantidad) sobre el iterable resultante.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\06-Programación Funcional>python Ejercicio_6.2.py

================
Operación FILTER
================

Tupla original: (2, 8, 4, 9, 5, 12, 1)
Elementos filtrados (> 5): (8, 9, 12)
Cantidad de elementos obtenidos: 3
```

### 📉 6.3. Cantidad de elementos mayores a 5 con REDUCE
> 💡 **Enfoque técnico:** Se importó el módulo `functools.reduce`. La expresión `lambda acc, x: acc + 1 if x > 5 else acc` actúa como un acumulador condicional. Se inicializó el tercer parámetro de `reduce` en `0` (el acumulador). Es una resolución matemáticamente elegante que elimina la necesidad de variables contadoras externas y bucles explícitos.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\06-Programación Funcional>python Ejercicio_6.3.py

================
Operación REDUCE
================

Tupla original: (2, 8, 4, 9, 5, 12, 1)
Cantidad de elementos > 5 calculada con Reduce: 3
```