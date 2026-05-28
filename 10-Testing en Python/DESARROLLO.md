# 🧪 Marco Práctico 10: Testing en Python

## Parte 1: Fundamentos del Testing Automático

**10.1 ¿Qué se entiende por Testing?**
Es el proceso sistemático de evaluar y verificar que un producto de software hace exactamente lo que se supone que debe hacer. Su objetivo es identificar defectos, brechas de seguridad o requerimientos faltantes antes del despliegue en producción.

**10.2 Diferencia entre Test Manual y Automático:**
* **Manual:** Ejecutado por un humano (QA) que interactúa con el sistema, haciendo clics o ingresando datos para verificar resultados. Es lento, propenso al error humano y difícil de escalar.
* **Automático:** Consiste en escribir scripts de código que ejecutan la validación contra el código de producción. Es rápido, determinista, repetible y fundamental para la Integración Continua (CI/CD).

**10.3 ¿Qué es un Assert en Test Automáticos?**
Es una declaración lógica (una aserción) que evalúa si una condición específica es `True` o `False`. Si la evaluación es `True`, la prueba pasa. Si es `False`, la prueba falla y el framework lanza una excepción deteniendo ese caso específico.

**10.4 ¿Qué es `unittest` y cómo se implementa?**
`unittest` es el framework de pruebas unitarias nativo de la biblioteca estándar de Python, inspirado en JUnit (Java). Se implementa importando el módulo, creando una clase que herede de `unittest.TestCase` y definiendo métodos cuyos nombres comiencen obligatoriamente con la palabra `test_`.

---

## Parte 2: Análisis de Funciones Assert

Breve descripción analítica de los métodos de validación:
* **`.assertEqual(a, b)`:** Verifica la igualdad de valor ($a == b$).
* **`.assertTrue(x)`:** Valida que la expresión $x$ se evalúe estrictamente como verdadera.
* **`.assertFalse(x)`:** Valida que la expresión $x$ se evalúe estrictamente como falsa.
* **`.assertIs(a, b)`:** Verifica identidad en memoria (operador `is`), es decir, que ambas variables apunten exactamente al mismo objeto referenciado.
* **`.assertIsNone(x)`:** Verifica que el valor sea exactamente el tipo `None`.
* **`.assertIn(a, b)`:** Valida pertenencia; comprueba si el elemento $a$ existe dentro de la colección o iterable $b$.
* **`.assertIsInstance(a, b)`:** Verifica el tipado, asegurando que el objeto $a$ sea una instancia de la clase $b$.
* **`.assertRaises(x)`:** Verifica que, al ejecutar un bloque de código, se lance obligatoriamente la excepción $x$ (ej: `ZeroDivisionError`).

---

## Parte 3: Análisis de Código (Punto 10.5)

**Explicación del código de cálculo de media:**
El sistema está modularizado. En `funciones.py` tenemos una función que acepta un número variable de argumentos posicionales (`*args`). Al recibir una lista dentro de `args`, utiliza el desempaquetado lógico para sumar los elementos y dividirlos por la cantidad, obteniendo la media aritmética. 
En `tests.py`, la clase `TestCalculaMedia` automatiza la validación inyectando vectores de prueba estáticos (`[10, 10, 10]` y `[5, 3, 4]`) y usando `.assertEqual` para corroborar que la salida del algoritmo coincide matemáticamente con el resultado esperado de negocio (10 y 4 respectivamente).

**Ejecución en consola:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\10-Testing en Python>python tests.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

---

## Parte 4: Ciclo de Vida del Test (Marco Práctico 10.1)

**¿Qué permite usar `setUp` y `tearDown` en UnitTest?**
Garantizan el principio de **Aislamiento de las pruebas (Test Isolation)**. 
* `setUp()` se ejecuta de manera implícita *justo antes* de cada método `test_`. Sirve para preparar el entorno (ej: abrir una conexión a base de datos, instanciar objetos).
* `tearDown()` se ejecuta *justo después* de cada prueba, sin importar si esta falló o pasó. Se encarga de la limpieza de memoria (ej: cerrar conexiones, borrar archivos temporales).

**Explicación y Ejecución del código del Marco Práctico 10.1:**
El siguiente output demuestra el ciclo de vida. Observamos cómo el entorno se construye y se destruye alrededor de cada caso de prueba de manera atómica. El flag `-v` (verbose) nos detalla qué prueba se está ejecutando.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\10-Testing en Python>python -m unittest -v test_ejemplos.py
test_1 (test_ejemplos.TestEjemplos) ... -> Entra setUp (Prepara el entorno)

Ejecutando Test: test_1
-> Entra tearDown (Limpia el entorno)
ok
test_2 (test_ejemplos.TestEjemplos) ... -> Entra setUp (Prepara el entorno)

Ejecutando Test: test_2
-> Entra tearDown (Limpia el entorno)
ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```