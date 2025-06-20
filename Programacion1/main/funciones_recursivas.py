# Función recursiva para calcular el promedio  
import sys
""" 
El módulo sys te da acceso a herramientas para interactuar con el Python.

La usamos específicamente para sys.setrecursionlimit(), que nos permite aumentar el número máximo de veces que 
una función puede llamarse a sí misma (recursión). Hacemos esto para que nuestras pruebas de rendimiento con listas 
muy grandes no fallen por el límite de recursión por defecto de Python. 
"""
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
    # Condición que detiene la recursión
    # si el indice actual es igual al tamaño de la lista (revisó toda la lista)
    if indice_actual == len(lista_de_numeros):
        if conteo_acumulado > 0:
            return suma_acumulada / conteo_acumulado # se calcula el promedio
        else:
            # devuelve 0 si no hay numeros positivos o si está vaciá
            return 0 
    
    # paso recursivo, se llama la función así misma
    numero_en_posicion_actual = lista_de_numeros[indice_actual] # obtengo el numero en la posicion actual
    
    
    if numero_en_posicion_actual > 0: # si es positivo..
        
        return calcular_promedio_positivos_recursivo(
            lista_de_numeros,
            suma_acumulada + numero_en_posicion_actual,     # se suma el numero actual
            conteo_acumulado + 1,                           # aumento el contador
            indice_actual + 1                               # paso al sgte numero
        )
    else:
        # si es 0 o negativo
        return calcular_promedio_positivos_recursivo(
            lista_de_numeros,
            suma_acumulada,
            conteo_acumulado,
            indice_actual + 1
        )
        
# chequeamos si nuestro codigo funciona bien
if __name__ == "__main__":
    print("\nTest y pruebas unitarias")
    # numeros positivos (1 + 2 + 3 + 4 + 5) / 5 = 3.0
    assert calcular_promedio_positivos_recursivo([1, 2, 3, 4, 5]) == 3.0, "Test 1 Recursivo Fallido: Lista con solo positivos"
    # numeros negativos = 0
    assert calcular_promedio_positivos_recursivo([-1, -2, -3]) == 0, "Test 2 Recursivo Fallido: Lista con solo negativos"
    # (10+20+30)/3 = 20.0
    assert calcular_promedio_positivos_recursivo([10, -5, 20, 0, 30]) == 20.0, "Test 3 Recursivo Fallido: Lista mixta"
    # lista vacía = 0
    assert calcular_promedio_positivos_recursivo([]) == 0, "Test 4 Recursivo Fallido: Lista vacía"
    # 7/1 = 7.0
    assert calcular_promedio_positivos_recursivo([7]) == 7.0, "Test 5 Recursivo Fallido: Un solo positivo"
    # numero negativo = 0
    assert calcular_promedio_positivos_recursivo([-7]) == 0, "Test 6 Recursivo Fallido: Un solo negativo"
    print("Todas las pruebas para la función recursiva pasaron correctamente.")
