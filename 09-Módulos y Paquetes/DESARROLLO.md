# 📦 Marco Práctico 9: Módulos y Paquetes

**Desarrollo Práctico en Python (Arquitectura y Ejecución):**

### 🏗️ 9.1. y 9.2. Paquete Simple y Directorio de Aplicaciones
> 💡 **Enfoque técnico:** Se estructuró el directorio de trabajo separando el script de ejecución principal (`app.py`) de la lógica de negocio (`mi_paquete`). El uso del archivo `__init__.py` convierte el directorio en un espacio de nombres (namespace) válido para que el intérprete de Python pueda resolver las importaciones relativas y absolutas.

**Estructura del Proyecto Creada:**
```text
📂 09-Módulos y Paquetes/
 ├── 📄 app.py (Script de nivel superior)
 └── 📂 mi_paquete/ (Paquete simple)
      ├── 📄 __init__.py (Inicializador del paquete)
      └── 📄 operaciones.py (Módulo con lógica de negocio)
```

### 🚀 9.3. Scripts de Nivel Superior
> 💡 **Enfoque técnico:** El script `app.py` actúa como el punto de entrada del sistema (Entry Point). No realiza cálculos pesados; importa las herramientas necesarias desde `mi_paquete.operaciones` y orquesta el flujo de datos. Esto garantiza escalabilidad.

**Ejecución del Script:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\09-Módulos y Paquetes>python app.py

==========================================
 Sistema de Cálculo Sencillo Inicializado
==========================================

El resultado de la suma (25 + 10) es: 35
El resultado de la resta (25 - 10) es: 15
```