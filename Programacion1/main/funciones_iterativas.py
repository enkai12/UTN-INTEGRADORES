# Este archivo contiene la función para calcular el promedio de números positivos de forma iterativa.

# --- Función Iterativa: 'calcular_promedio_positivos_iterativo' ---
# Esta función encuentra el promedio de números positivos usando un bucle (paso a paso).
def calcular_promedio_positivos_iterativo(lista_de_numeros):
    """
    Calcula el promedio de los números positivos en una lista.
    Usa un enfoque iterativo (con un bucle).
    
    Argumentos:
        lista_de_numeros (list): Una lista que contiene números (enteros o decimales).
        
    Devuelve:
        float: El promedio de los números positivos. Si no hay números positivos, devuelve 0.
    """
    # Aquí guardaremos la suma de todos los números positivos que encontremos.
    suma_de_positivos = 0
    # Aquí contaremos cuántos números positivos hemos sumado.
    cantidad_de_positivos = 0
    