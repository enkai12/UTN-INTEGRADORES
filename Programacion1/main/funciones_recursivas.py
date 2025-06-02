# Este archivo contiene la función para calcular el promedio de números positivos de forma recursiva.

import sys

# Ajustamos el límite de recursión de Python. Por defecto, Python detiene la recursión
# después de un cierto número de llamadas (normalmente 1000) para evitar que el programa
# se quede sin memoria. Lo aumentamos para poder probar con listas más grandes.
# ¡Importante! Un número demasiado alto puede causar problemas si tu computadora no tiene suficiente memoria.
sys.setrecursionlimit(200000) 