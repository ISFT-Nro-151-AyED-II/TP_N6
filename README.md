# 🐍 Trabajo Práctico N°2 - Unidad N°2 - Segunda Parte

**Instituto Superior de Formación Técnica Nº 151**  
**Carrera:** Tecnicatura Superior en Análisis de Sistemas  
**Materia:** Algoritmos y Estructuras de Datos II  
**Tema:** Fundamentos de Python: Introducción a Python, Estructuras, Programación Funcional y Testing   
**Alumno:** David Hernán Bravo  

---

## 🎯 Objetivo del Repositorio
Este repositorio contiene la resolución íntegra y documentada del Trabajo Práctico enfocado en el aprendizaje y dominio del lenguaje Python. El desarrollo está estructurado bajo principios de ingeniería de software, priorizando la modularización, el manejo eficiente de memoria, el paradigma funcional y la implementación de pruebas unitarias (Test-Driven Development).

---

## 📂 Arquitectura del Proyecto y Desarrollo Práctico

El trabajo se dividió lógicamente en 10 módulos. Cada directorio contiene sus respectivos scripts (`.py`) para aislar la lógica de negocio, junto con un archivo `DESARROLLO.md` que evidencia la ejecución, las salidas de consola y el análisis técnico de cada solución.

### ⚙️ [1. Instalación y Entorno](./01-Instalación%20y%20Entorno/DESARROLLO.md)
* **Resumen:** Configuración global del intérprete de Python, despliegue de la consola interactiva (REPL), IDLE, y gestión de paquetes a nivel de sistema operativo utilizando `pip`.
* [Ver Desarrollo y Ejecución](./01-Instalación%20y%20Entorno/DESARROLLO.md)

### 📦 [2. Aspectos del Lenguaje (Entornos Virtuales)](./02-Aspectos%20del%20Lenguaje/DESARROLLO.md)
* **Resumen:** Implementación de buenas prácticas de aislamiento de dependencias. Creación, activación y destrucción de entornos virtuales (`venv`) para instalar paquetes de terceros (como Flask) sin corromper el entorno global.
* [Ver Desarrollo y Ejecución](./02-Aspectos%20del%20Lenguaje/DESARROLLO.md)

### 📚 [3. Colecciones en el Lenguaje](./03-Colecciones%20en%20el%20Lenguaje/DESARROLLO.md)
* **Resumen:** Manipulación eficiente de memoria a través de listas, tuplas y diccionarios. Implementación de búsquedas en tiempo constante $O(1)$ usando hashes (diccionarios) y optimización de secuencias con *List Comprehensions*.
* [Ver Desarrollo y Ejecución](./03-Colecciones%20en%20el%20Lenguaje/DESARROLLO.md)

### 🔄 [4. Bucles y Control de Flujo](./04-Bucles%20en%20el%20Lenguaje/DESARROLLO.md)
* **Resumen:** Desarrollo de algoritmos iterativos (`for`, `while`). Aplicación estricta de validaciones de input de usuario y captura de excepciones para garantizar la estabilidad del flujo de ejecución del programa.
* [Ver Desarrollo y Ejecución](./04-Bucles%20en%20el%20Lenguaje/DESARROLLO.md)

### 🛠️ [5. Funciones en Python](./05-Funciones%20en%20Python/DESARROLLO.md)
* **Resumen:** Transición de código procedimental a modular. Encapsulamiento de lógica matemática y procesamiento de datos en funciones puras para maximizar la reutilización del código y aislar la captura de datos del usuario.
* [Ver Desarrollo y Ejecución](./05-Funciones%20en%20Python/DESARROLLO.md)

### 🧮 [6. Programación Funcional](./06-Programación%20Funcional/DESARROLLO.md)
* **Resumen:** Aplicación del paradigma declarativo puro. Transformación y filtrado de colecciones inmutables utilizando funciones de orden superior como `map()`, `filter()` y `reduce()` apoyadas en expresiones anónimas (`lambda`).
* [Ver Desarrollo y Ejecución](./06-Programación%20Funcional/DESARROLLO.md)

### ⚠️ [7. Excepciones en Python](./07-Excepciones%20en%20Python/DESARROLLO.md)
* **Resumen:** Diseño de sistemas tolerantes a fallos. Captura, análisis y manejo preventivo de excepciones nativas (`ZeroDivisionError`, `IndexError`, `KeyError`, `TypeError`, `NameError`) y forzado de reglas de negocio mediante la sentencia `raise` (`RuntimeError`).
* [Ver Desarrollo y Ejecución](./07-Excepciones%20en%20Python/DESARROLLO.md)

### 📁 [8. Archivos (Persistencia I/O)](./08-Archivos%20en%20Python/DESARROLLO.md)
* **Resumen:** Interacción con el sistema de archivos del sistema operativo. Apertura, lectura y escritura de ficheros con control de codificación (`utf-8`). Implementación del estándar de industria mediante Context Managers (`with`) para el manejo seguro de recursos y limpieza de memoria.
* [Ver Desarrollo y Ejecución](./08-Archivos%20en%20Python/DESARROLLO.md)

### 🏗️ [9. Módulos y Paquetes](./09-Módulos%20y%20Paquetes/DESARROLLO.md)
* **Resumen:** Diseño de arquitectura de software. Separación estructural entre scripts de nivel superior (Entry Points) y la lógica de negocio almacenada en paquetes locales instanciables mediante el uso de espacios de nombres (`__init__.py`).
* [Ver Desarrollo y Ejecución](./09-Módulos%20y%20Paquetes/DESARROLLO.md)

### 🧪 [10. Testing Automático](./10-Testing%20en%20Python/DESARROLLO.md)
* **Resumen:** Fundamentos de la calidad de software. Análisis teórico de aserciones (`asserts`) e implementación del framework nativo `unittest`. Demostración del ciclo de vida y aislamiento de pruebas unitarias mediante entornos efímeros (`setUp` y `tearDown`).
* [Ver Desarrollo, Análisis y Ejecución](./10-Testing%20en%20Python/DESARROLLO.md)

---

## 🚀 Buenas Prácticas Implementadas
* **Aislamiento:** Archivo `.gitignore` configurado en la raíz para evitar subir binarios locales y la carpeta de entornos virtuales (`venv/`).
* **Tipado:** Uso de Type Hints en la definición de funciones para mejorar la legibilidad y el análisis estático.
* **Manejo de Errores:** Bloques `try-except` estandarizados para que los scripts no aborten ante inputs de usuario inválidos.
* **Documentación:** Trazabilidad completa de la ejecución en consola dentro de los archivos `DESARROLLO.md`.
