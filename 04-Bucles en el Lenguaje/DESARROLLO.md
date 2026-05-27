# 🔄 Marco Práctico 4: Bucles en el Lenguaje

**Desarrollo Práctico en Python (Ejecución de Scripts Locales):**

### 🔢 4.1. Pares e impares en un rango definido
> 💡 **Enfoque técnico:** Se implementó una lógica de "paso dinámico" (`step = 1` o `-1`) dentro de la función `range()` para que el algoritmo funcione sin importar si el primer número es menor o mayor que el segundo, recorriendo la secuencia de manera bidireccional. La evaluación de paridad se realiza con la operación módulo (`% 2 == 0`).

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\04-Bucles en el Lenguaje>python Ejercicio_4.1.py
Ingresá el primer número entero: 12
Ingresá el segundo número entero: 9

Analizando números desde 12 hasta 9:
- El número 12 es PAR
- El número 11 es IMPAR
- El número 10 es PAR
- El número 9 es IMPAR
```

### ✅ 4.2. Validación persistente de un número positivo
> 💡 **Enfoque técnico:** Se aplicó un bucle `while True` con captura de excepciones (`try...except`) para validar no solo que el número cumpla la regla de negocio (ser mayor a cero), sino para evitar que el programa aborte por un ingreso alfanumérico inesperado.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\04-Bucles en el Lenguaje>python Ejercicio_4.2.py
Ingresá un número estrictamente positivo: -5
Error: El número debe ser mayor a 0. Intentá de nuevo.

Ingresá un número estrictamente positivo: hola
Error: Ingreso inválido. Por favor, escribí un número.

Ingresá un número estrictamente positivo: 8
Correcto. Ingresaste 8.0, el cual es positivo.
```

### 📈 4.3. Validación de número mayor al anterior
> 💡 **Enfoque técnico:** El bucle mantiene atrapado al usuario hasta que la validación relacional (`num2 > num1`) devuelva un booleano `True`, forzando la consistencia de los datos antes de seguir con el flujo de ejecución.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\04-Bucles en el Lenguaje>python Ejercicio_4.3.py
Ingresá el primer número entero: 5
Ingresá un número mayor que 5: 3
Error: 3 no es mayor que 5. Volvé a intentar.

Ingresá un número mayor que 5: 5
Error: 5 no es mayor que 5. Volvé a intentar.

Ingresá un número mayor que 5: 12

Proceso finalizado. Los números ingresados son: 5 y 12
```

### 🧮 4.4. Lista de números consecutivos ordenados
> 💡 **Enfoque técnico:** Para asegurar el orden "de menor a mayor" sin importar el input del usuario, se aplicaron las funciones `min()` y `max()`. Se excluyeron los extremos (ya que se solicitan los números "entre ellos") y la generación se resolvió eficientemente con una lista por comprensión.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\04-Bucles en el Lenguaje>python Ejercicio_4.4.py
Ingresá el primer número entero: 25
Ingresá el segundo número entero: 18

Los números consecutivos entre 18 y 25 son:
[19, 20, 21, 22, 23, 24]
```