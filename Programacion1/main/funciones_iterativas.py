# Encuentra el promedio de números positivos usando un bucle (paso a paso).
def calcular_promedio_positivos_iterativo(lista_de_numeros):
    """
    Calcula el promedio de los números positivos en una lista.
    Usa un bucle.
    
    Argumentos:
        lista_de_numeros (list): Una lista que contiene números (enteros o decimales).
        
    Devuelve:
        float: El promedio de los números positivos. Si no hay números positivos devuelve 0.
    """
    # Se inicializan las variables
    suma_de_positivos = 0
    cantidad_de_positivos = 0
    
    # Recorremos cada número
    # Se revisa cada elemento de la lista - uno por uno.
    for numero_actual in lista_de_numeros:
        # Este número es positivo?
        if numero_actual > 0:
            # Si es positivo se suma a la variable
            suma_de_positivos += numero_actual 
            # aumenta el contador
            cantidad_de_positivos += 1    
    
    if cantidad_de_positivos > 0:
        # Cálculamos el promedio:
        return suma_de_positivos / cantidad_de_positivos
    else:
        # Si no encontramos ningún número positivo o la lista estaba vacía, el promedio es 0.
        return 0         
    
# Investigamos cómo comprobar si el bucle funciona cómo debería
# Para ver si nuestra función devuelve el resultado esperado utilizamos "assert"
# Lo que hace es probar/depurar el código. Es una verificación de una condición que debería ser verdadera.
# Evalúa la condición: Python mira si la condición es True o False.
# Si es False lanza un error llamado AssertionError.
if __name__ == "__main__":
    print("Pruebas Unitarias")
    # 1 + 2 + 3 + 4 + 5 / 5 = 3
    assert calcular_promedio_positivos_iterativo([1, 2, 3, 4, 5]) == 3.0, "Test 1 Fallido: Lista con solo positivos"
    # Una lista de sólo números negativos el promedio debería ser = 0
    assert calcular_promedio_positivos_iterativo([-1, -2, -3]) == 0, "Test 2 Fallido: Lista con solo negativos"
    #(10+20+30)/3 = 20.0
    assert calcular_promedio_positivos_iterativo([10, -5, 20, 0, 30]) == 20.0, "Test 3 Fallido: Lista mixta"
    # lista vacía el promedio es 0
    assert calcular_promedio_positivos_iterativo([]) == 0, "Test 4 Fallido: Lista vacía"
    # 7/1 = 7.0
    assert calcular_promedio_positivos_iterativo([7]) == 7.0, "Test 5 Fallido: Un solo positivo"
    # número negativo el promedio es = 0
    assert calcular_promedio_positivos_iterativo([-7]) == 0, "Test 6 Fallido: Un solo negativo"
    print("Todas las pruebas para la función pasaron correctamente.")

