# 🛠️ Marco Práctico 5: Funciones en Python

**Desarrollo Práctico en Python (Ejecución de Scripts Locales):**

### 📐 5.1. Dibujo de un rectángulo
> 💡 **Enfoque técnico:** Se encapsuló la lógica de renderizado en la función `dibujar_rectangulo(ancho, alto, caracter)`. Se validó que las dimensiones sean positivas y que el string de relleno tenga longitud 1. Para optimizar memoria, la impresión de cada fila se realiza multiplicando el string (`caracter * ancho`) en lugar de usar un bucle anidado.

```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\05-Funciones en Python>python Ejercicio_5.1.py
Ingresá la anchura del rectángulo: 10
Ingresá la altura del rectángulo: 4
Ingresá el caracter a utilizar: #

Resultado:
##########
##########
##########
##########
```

### 🗓️ 5.2. Verificador de Año Bisiesto
> 💡 **Enfoque técnico:** Se implementó la función pura `es_bisiesto(anio)` que devuelve un valor booleano (`True` o `False`). El cálculo se resuelve en una única sentencia lógica evaluando el módulo (`%`).

**Pruebas con los casos sugeridos:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\05-Funciones en Python>python Ejercicio_5.2.py
Ingresá un año para verificar si es bisiesto: 2012
El año 2012 ES bisiesto.

D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\05-Funciones en Python>python Ejercicio_5.2.py
Ingresá un año para verificar si es bisiesto: 1900
El año 1900 NO es bisiesto.

D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\05-Funciones en Python>python Ejercicio_5.2.py
Ingresá un año para verificar si es bisiesto: 2000
El año 2000 ES bisiesto.
```

### 📝 5.3. Generador de lista de palabras
> 💡 **Enfoque técnico:** La función `crear_lista_palabras(cantidad)` aísla el bucle `for` responsable de poblar la colección. Se implementó una guardia (`if cantidad < 0`) en el flujo principal para evitar que el bucle intente procesar iteraciones negativas. Si el usuario ingresa `0`, la función retorna una lista vacía `[]`, cumpliendo la consigna.

**Prueba con lista poblada:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\05-Funciones en Python>python Ejercicio_5.3.py
¿Cuántas palabras querés agregar a la lista?: 3
Ingresá la palabra 1: Sistema
Ingresá la palabra 2: Análisis
Ingresá la palabra 3: Python

La lista creada es: ['Sistema', 'Análisis', 'Python']
```

**Prueba con lista vacía:**
```cmd
D:\Repositorios de GitHub\ISFT N°151\Algoritmos y Estructuras de Datos II\Trabajos Prácticos\TP_N6\05-Funciones en Python>python Ejercicio_5.3.py
¿Cuántas palabras querés agregar a la lista?: 0

La lista creada es: []
```