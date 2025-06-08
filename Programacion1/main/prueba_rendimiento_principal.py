# Archivo "main" que ejecuta las pruebas
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

# inicializamos listas vacías para guardar los tiempos para cada función
tiempos_funcion_iterativa = []
tiempos_funcion_recursiva = []

ejecuciones_por_medicion = 100 # cuantas veces se repetira cada medicion (nos aseguramos de obtener resultados mas precisos)

# --- INICIANDO PRUEBAS DE RENDIMIENTO ---

print("\n- INICIANDO PRUEBAS DE RENDIMIENTO -")

for tamano_actual in tamanos_de_lista:
    # Creamos una lista de números aleatorios entre -1 y 10, simulando notas de alumnos
    lista_para_prueba = [random.randint(-1, 10) for _ in range(tamano_actual)]

    print(f"\nProbando con una lista de tamaño: {tamano_actual} elementos.")

    # - Medición de la función iterativa -
    # Preparamos el código que 'timeit' ejecutará.
    configuracion_iterativa = f"""
from funciones_iterativas import calcular_promedio_positivos_iterativo
lista_prueba = {lista_para_prueba} 
"""

    # Medimos el tiempo total y calculamos el promedio por ejecución
    tiempo_total_iterativa = timeit.timeit(
        stmt="calcular_promedio_positivos_iterativo(lista_prueba)", 
        setup=configuracion_iterativa, 
        number=ejecuciones_por_medicion 
    )
    tiempo_promedio_iterativa = tiempo_total_iterativa / ejecuciones_por_medicion

    tiempos_funcion_iterativa.append(tiempo_promedio_iterativa)
    print(f"  Tiempo Iterativo (promedio de {ejecuciones_por_medicion} ejecuciones): {tiempo_promedio_iterativa:.6f} segundos")


    # - Medición de la función recursiva -
    configuracion_recursiva = f"""
from funciones_recursivas import calcular_promedio_positivos_recursivo
import sys
sys.setrecursionlimit(max(sys.getrecursionlimit(), {tamano_actual + 100})) 
lista_prueba = {lista_para_prueba}
"""
    try:
        # Intentamos medir el tiempo. Puede fallar por 'RecursionError'
        tiempo_total_recursiva = timeit.timeit(
            stmt="calcular_promedio_positivos_recursivo(lista_prueba)",
            setup=configuracion_recursiva,
            number=ejecuciones_por_medicion
        )
        tiempo_promedio_recursiva = tiempo_total_recursiva / ejecuciones_por_medicion
        tiempos_funcion_recursiva.append(tiempo_promedio_recursiva)
        print(f"  Tiempo Recursivo (promedio de {ejecuciones_por_medicion} ejecuciones): {tiempo_promedio_recursiva:.6f} segundos")
    except RecursionError:
        # Informamos si hubo un error de recursión
        print(f"  Error de Recursión,lLa lista de tamaño {tamano_actual} es demasiado grande para la recursión.")
        tiempos_funcion_recursiva.append(float('nan')) 

print("\n- PRUEBAS DE RENDIMIENTO FINALIZADAS -")

# --- Presentación Final de los Resultados en una Tabla en la Terminal ---
# Esta sección toma todos los tiempos que guardamos y los organiza en una tabla fácil de leer
# que se mostrará directamente en la terminal.
print("\n--- RESUMEN DE TIEMPOS DE EJECUCIÓN ---")

# Imprimimos los encabezados de la tabla.
# '{:<15}' significa: "reserva 15 espacios y alinea el texto a la izquierda".
# Esto ayuda a que las columnas se vean ordenadas.
print("{:<15} {:<25} {:<25}".format("Tamaño Lista", "Tiempo Iterativo (s)", "Tiempo Recursivo (s)"))
# Imprimimos una línea de guiones para separar los encabezados de los resultados.
print("-" * 65) 

# Recorremos nuestras listas de 'tamanos_de_lista' y los tiempos que guardamos
# 'enumerate()' nos da el índice 'i' y el valor 'tamano' en cada vuelta.
for i, tamano in enumerate(tamanos_de_lista):
    # Obtenemos el tiempo iterativo y lo formateamos a 6 decimales.
    tiempo_iterativo_formateado = f"{tiempos_funcion_iterativa[i]:.6f}" 
    
    # Obtenemos el tiempo recursivo, condición:
    # Si el tiempo es 'nan' = Not a number (que guardamos cuando hubo un error de recursión),
    # mostramos el texto "(Error de Recursión)".
    # Si no es 'nan', lo formateamos a 6 decimales.
    tiempo_recursivo_formateado = f"{tiempos_funcion_recursiva[i]:.6f}" if not float('nan') == tiempos_funcion_recursiva[i] else "(Error de Recursión)"
    
    # Imprimimos la fila completa de la tabla, usando el mismo formato para las columnas.
    print(f"{tamano:<15} {tiempo_iterativo_formateado:<25} {tiempo_recursivo_formateado:<25}")

