# 📁 Marco Práctico 8: Archivos en Python

**Desarrollo Práctico en Python (Ejecución de Scripts Locales):**

### ✍️ 8.1. Escritura y creación de archivo
> 💡 **Enfoque técnico:** Se utilizó el modo de apertura `a+` (Append and Read). Es la decisión técnica correcta porque `w+` trunca (borra) el archivo antes de escribir, y `r+` falla si el archivo no existe. `a+` cumple con el requerimiento de crear si no existe y añadir (append) al final. Se utilizó `encoding="utf-8"` por estándar de la industria y un bloque `finally` para asegurar el cierre (`close()`).

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\08-Archivos en Python>python Ejercicio_8.1.py

Frase añadida con éxito en 'mi_fichero.txt'.
```

### 🔍 8.2. Lectura de estado y metadatos
> 💡 **Enfoque técnico:** Se consultaron los atributos internos del objeto `io.TextIOWrapper` que retorna la función `open()`. Se demuestra el cambio de estado del atributo booleano `.closed` antes y después de liberar el recurso en memoria.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\08-Archivos en Python>python Ejercicio_8.2.py

==============================
 Metadatos del Objeto Fichero
==============================

Nombre del archivo : mi_fichero.txt
Modo de apertura   : r
Codificación       : utf-8
¿Está cerrado?     : False (antes de llamar a close())
¿Está cerrado?     : True (después de llamar a close())
```

### 🛡️ 8.3. Context Managers (Estructura `with`)
> 💡 **Enfoque técnico:** Se refactorizaron los dos algoritmos anteriores aplicando un manejador de contexto (`with`). Esta estructura garantiza el principio de "limpieza segura" (safe cleanup), ejecutando el cierre del archivo de manera implícita al salir de la indentación, incluso si ocurre una excepción de hardware o software en el medio.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\08-Archivos en Python>python Ejercicio_8_3.py

================================
 Ejecutando con Estructura WITH
================================

Frase añadida correctamente.

Metadatos del Archivo (Dentro del bloque)
-----------------------------------------

Nombre       : fichero_with.txt
Modo         : a+
Codificación : utf-8
Estado cerrado: False

Fuera del bloque WITH. Estado cerrado: True
```