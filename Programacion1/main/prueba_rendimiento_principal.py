# Archivo "main" que ejecuta las pruebas

# Importamos las librerías necesarias.
import random         # Para generar números aleatorios de forma sencilla.
import timeit         # Para medir el tiempo de ejecución.
import sys            # Para ajustar el límite de recursión si es necesario.

# Importamos nuestras funciones:
from funciones_iterativas import calcular_promedio_positivos_iterativo
from funciones_recursivas import calcular_promedio_positivos_recursivo

# Pruebas - Medición 
"""
Ajustamos el límite de recursión de Python. Por defecto, Python detiene la recursión
después de un cierto número de llamadas (normalmente 1000) para evitar que el programa
se quede sin memoria. Lo aumentamos para poder probar con listas más grandes.
Un número demasiado alto puede causar problemas de memoria 
"""
sys.setrecursionlimit(200000) 

# Definimos los diferentes tamaños de lista para ejecutar nuestras pruebas, queremos notar y ver
# la diferencia de tiempos.
tamanos_de_lista = [100, 1000, 5000, 10000, 50000, 100000]

# inicializamos listas vacías para guardar los tiempos que medimos para cada función
tiempos_funcion_iterativa = []
tiempos_funcion_recursiva = []