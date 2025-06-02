# Este es el archivo principal que ejecuta las pruebas de rendimiento.

# Importamos las librerías necesarias.
import random         # Para generar números aleatorios de forma sencilla.
import timeit         # Para medir el tiempo de ejecución.
import sys            # Para ajustar el límite de recursión si es necesario.

# Importamos nuestras funciones desde los otros archivos.
# Asegúrate de que 'funciones_iterativas.py' y 'funciones_recursivas.py'
# estén en la misma carpeta que este archivo.
from funciones_iterativas import calcular_promedio_positivos_iterativo
from funciones_recursivas import calcular_promedio_positivos_recursivo