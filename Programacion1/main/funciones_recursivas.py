# Función recursiva para calcular el promedio  

""" 
El módulo sys te da acceso a herramientas para interactuar con el sistema Python 
que está ejecutando tu código.

La usamos específicamente para sys.setrecursionlimit(), que nos permite aumentar el número máximo de veces que 
una función puede llamarse a sí misma (recursión). Hacemos esto para que nuestras pruebas de rendimiento con listas 
muy grandes no fallen por el límite de recursión por defecto de Python. 
"""

import sys

sys.setrecursionlimit(200000)

def calcular_promedio_positivos_recursivo(lista_de_numeros, suma_acumulada=0, conteo_acumulado=0, indice_actual=0): # inicializamos las variables
    """
    - Calcula el promedio de los números en una lista
    - Usa un enfoque recursivo (la función se llama a sí misma)
    
    Argumentos:
        - lista_de_numeros (list): Una lista que contiene números
        - suma_acumulada (float): La suma de positivos hasta ahora (uso interno)
        - conteo_acumulado (int): La cantidad de positivos hasta ahora (uso interno)
        - indice_actual (int): La posición actual que estamos revisando en la lista (uso interno)
        
    Retorna:
        float: El promedio de los números positivos y si no hay devuelve 0.
    """