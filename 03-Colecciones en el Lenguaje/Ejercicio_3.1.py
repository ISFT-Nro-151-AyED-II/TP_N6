# MARCO PRÁCTICO
# ==============
# 3.1 Meté los valores del 1 al 100 en una lista.
# Usamos list(range()) porque es más eficiente en memoria y tiempo de ejecución que un bucle for tradicional.

lista_numeros = list(range(1, 101))

print("Lista generada con éxito. Primeros y últimos 5 elementos:")
print(f"Inicio: {lista_numeros[:5]} ... Fin: {lista_numeros[-5:]}")