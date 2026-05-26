# ⚙️ Marco Práctico 2: Aspectos del Lenguaje (Entornos Virtuales)

**Desarrollo Práctico en Python:**

### 📁 2.1. Crear un entorno virtual nuevo
> 💡 **Explicación técnica:** Utilizamos el módulo nativo `venv` de Python. La sintaxis es `python -m venv <nombre_del_entorno>`. Por convención estándar en la industria, a la carpeta del entorno se la suele llamar `venv` o `env`.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\02-Aspectos del Lenguaje>python -m venv .venv
```
*(Nota: Este comando no devuelve ninguna salida por consola si se ejecuta correctamente, simplemente crea una carpeta llamada `.venv` en el directorio actual).*

### 🟢 2.2. Activar un entorno virtual
> 💡 **Explicación técnica:** En Windows, la activación se realiza ejecutando el script `activate` que se encuentra dentro de la subcarpeta `Scripts`. Vas a notar que la activación fue exitosa porque el nombre del entorno aparecerá entre paréntesis a la izquierda del prompt del sistema.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\02-Aspectos del Lenguaje>.venv\Scripts\activate
(.venv) D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\02-Aspectos del Lenguaje>
```

### 📥 2.3. Instalar el Paquete Flask
> 💡 **Explicación técnica:** Al estar el entorno activado `(venv)`, cualquier uso de `pip` instalará los paquetes de forma aislada en esta carpeta, sin ensuciar la instalación global de Python en el sistema operativo.

```cmd
(.venv) D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\02-Aspectos del Lenguaje>pip install Flask
Collecting Flask
  Downloading flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)
Collecting Werkzeug>=3.0.0 (from Flask)
  Downloading werkzeug-3.0.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask)
  Downloading jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.1.2 (from Flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting blinker>=1.6.2 (from Flask)
  Downloading blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask)
  Downloading MarkupSafe-2.1.5-cp314-cp314-win_amd64.whl.metadata (3.1 kB)
Collecting colorama (from click>=8.1.3->Flask)
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Downloading flask-3.0.3-py3-none-any.whl (101 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.7/101.7 kB 2.0 MB/s 0:00:00
Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 5.5 MB/s 0:00:00
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.4-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 kB 7.7 MB/s 0:00:00
Downloading werkzeug-3.0.3-py3-none-any.whl (227 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 227.3/227.3 kB 14.4 MB/s 0:00:00
Downloading MarkupSafe-2.1.5-cp314-cp314-win_amd64.whl (17 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: MarkupSafe, itsdangerous, colorama, blinker, Werkzeug, Jinja2, click, Flask
Successfully installed Flask-3.0.3 Jinja2-3.1.4 MarkupSafe-2.1.5 Werkzeug-3.0.3 blinker-1.8.2 click-8.1.7 colorama-0.4.6 itsdangerous-2.2.0
```

### 🔴 2.4. Desactivar un entorno virtual
> 💡 **Explicación técnica:** Para salir del entorno aislado y volver al intérprete global del sistema, basta con ejecutar el comando `deactivate`. El prefijo `(.venv)` desaparecerá del prompt.

```cmd
(.venv) D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\02-Aspectos del Lenguaje>deactivate
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\02-Aspectos del Lenguaje>
```

### 🗑️ 2.5. Borrar el entorno virtual
> 💡 **Explicación técnica:** Como los entornos son efímeros, para borrarlo simplemente se elimina la carpeta raíz del mismo. En Windows usamos `rmdir /s /q` desde CMD para borrar el directorio y todo su contenido sin que nos pida confirmación archivo por archivo.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\02-Aspectos del Lenguaje>rmdir /s /q .venv
```