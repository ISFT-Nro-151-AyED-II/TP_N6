# ⚠️ Marco Práctico 7: Excepciones en Python

**Desarrollo Práctico en Python (Ejecución de Scripts Locales y Adicionales de la Teoría):**

### ➗ 7.1. División por cero (`ZeroDivisionError`)
> 💡 **Enfoque técnico:** Se encapsuló la llamada a la función en un bloque `try...except`. [cite_start]Python detectó matemáticamente la operación ilógica e interrumpió el flujo, pero nuestro bloque atrapó el evento, manteniendo el programa vivo. 

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\07-Excepciones en Python>python Ejercicio_7.1.py

==============================
 Excepción: ZeroDivisionError
==============================

Error crítico evitado (ZeroDivisionError): No se puede dividir por cero. Detalle del motor: division by zero
```

### 🔠 7.2. Error de Tipos (`TypeError`)
> 💡 **Enfoque técnico:** Al intentar operar `+ 10` sobre un string `"cinco"`, el tipado dinámico fuerte de Python rechazó la coerción implícita, lanzando una excepción. 

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\07-Excepciones en Python>python Ejercicio_7.2.py

======================
 Excepción: TypeError
======================

Prueba 1: Ejecución normal
mas_10(15) = 25

Prueba 2: Forzando el TypeError
Excepción capturada (TypeError): Discrepancia de tipos de datos. Detalle: can only concatenate str (not "int") to str
```

### 📊 7.3. Desbordamiento de Índice (`IndexError`)
> 💡 **Enfoque técnico:** Iteramos una lista de 3 elementos obligando al puntero a llegar hasta el índice 4. La memoria lanza un error preventivo para evitar lecturas arbitrarias. 

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\07-Excepciones en Python>python Ejercicio_7.3.py

=======================
 Excepción: IndexError
=======================

Tamaño de la lista: 3
Iterando forzadamente hasta el índice 5...
Índice 0: Linux
Índice 1: Windows
Índice 2: macOS

Excepción capturada (IndexError): Te fuiste de los límites de la colección. Detalle: list index out of range
```

### 🔑 7.4. Clave Inexistente en Diccionario (`KeyError`)
> 💡 **Enfoque técnico:** Los diccionarios en Python usan tablas hash para búsquedas `O(1)`. [cite_start]Si el hash consultado no existe, el motor falla automáticamente en lugar de devolver nulo (a menos que usemos `.get()`). 

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\07-Excepciones en Python>python Ejercicio_7.4.py

=====================
 Excepción: KeyError
=====================

Host: localhost
Excepción capturada (KeyError): La clave solicitada 'usuario' no se encuentra en el diccionario.
```

---

### [cite_start]🛡️ Bonus Track de Scripts Extras: Completando el Marco Teórico

**🔹 Extra 1: Identificador no encontrado (`NameError`)**
> 💡 **Enfoque técnico:** Evidencia cómo Python aborta la ejecución al llegar a una línea donde el puntero lógico busca un espacio en la tabla de variables (`scope`) que jamás fue instanciado. 

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\07-Excepciones en Python>python Ejercicio_7.5.py

======================
 Excepción: NameError
======================

Excepción capturada (NameError): name 'variable_fantasma' is not defined. Asegurate de inicializar las variables antes de usarlas.
```

**🔹 Extra 2: Error en tiempo de ejecución y sentencia `raise` (`RuntimeError`)**
> 💡 **Enfoque técnico:** Se demostró la utilidad fundamental de la palabra reservada `raise`. Esto permite a los desarrolladores forzar la interrupción del sistema para proteger la integridad y lógica del software ante datos no deseados, utilizando la excepción base `RuntimeError`.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\07-Excepciones en Python>python Ejercicio_7.6.py

=========================
 Excepción: RunTimeError
=========================

Intentando ingresar con 16 años...
Excepción capturada y lanzada manualmente (RuntimeError): Regla de Negocio: Acceso denegado. El usuario debe ser mayor de edad.
```