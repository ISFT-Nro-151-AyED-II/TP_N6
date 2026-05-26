# 🐍 Marco Práctico 1: Instalación y Entorno

**Desarrollo Práctico en Python:**

### 💻 1.1. Lanzar la Consola Interactiva y 1.2. Imprimir por Consola “Hola Mundo”
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\01-Instalación y Entorno>python
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hola Mundo!!!")
Hola Mundo!!!
>>> exit()
```

### 🖥️ 1.3. Lanzar el IDLE y repetir el punto 1.2
```cmd
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Hola Mundo!")
Hola Mundo!
```

### 📦 1.4. Añadir el Repositorio PIP: `python get-pip.py`
> 💡 **Aclaración técnica:** En las versiones modernas de Python (desde la 3.4), PIP ya viene instalado por defecto. Este paso suele pedirse en entornos Linux desactualizados o instalaciones rotas. Sin embargo, para cumplir con la consigna, ejecutamos lo siguiente:

**1. Descarga del script mediante `curl`:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\01-Instalación y Entorno>curl -O [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)
  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                 Dload  Upload  Total   Spent    Left   Speed
100  2.12M 100  2.12M   0      0  3.93M      0 --:--:-- --:--:-- --:--:-- 4.02M
```

**2. Ejecución e instalación:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\01-Instalación y Entorno>python get-pip.py
WARNING: Cache entry deserialization failed, entry ignored
Collecting pip
  Downloading pip-26.1.1-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.1.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 15.6 MB/s  0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 26.0
    Uninstalling pip-26.0:
      Successfully uninstalled pip-26.0
Successfully installed pip-26.1.1
```

### 🔄 1.5. Actualizar el PIP
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\01-Instalación y Entorno>python -m pip install --upgrade pip setuptools
Requirement already satisfied: pip in C:\Python314\Lib\site-packages (26.1.1)
Requirement already satisfied: setuptools in C:\Python314\Lib\site-packages (82.0.1)
WARNING: Cache entry deserialization failed, entry ignored
```

### 🧪 1.6. Probar PIP (list – show - update)

**📋 Listar paquetes instalados (`list`):**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\01-Instalación y Entorno>pip list
Package           Version
----------------- --------
asgiref           3.11.0
Django            6.0.1
flatbuffers       25.12.19
pip               26.1.1
protobuf          7.35.0
Pygments          2.20.0
PyYAML            6.0.3
setuptools        82.0.1
shellingham       1.5.4
sqlparse          0.5.5
typing_extensions 4.15.0
tzdata            2025.3
```

**🔍 Mostrar información de un paquete (`show`):**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\01-Instalación y Entorno>pip show pip
Name: pip
Version: 26.1.1
Summary: The PyPA recommended tool for installing Python packages.
Home-page: [https://pip.pypa.io/](https://pip.pypa.io/)
Author:
Author-email: The pip developers <distutils-sig@python.org>
License-Expression: MIT
Location: C:\Python314\Lib\site-packages
Requires:
Required-by:
```

**🚀 Actualizar (`update`):**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\01-Instalación y Entorno>python -m pip install --upgrade pip
Requirement already satisfied: pip in C:\Python314\Lib\site-packages (26.1.1)
```