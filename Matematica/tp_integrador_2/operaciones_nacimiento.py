import datetime

"""       
B. Operaciones con años de nacimiento

  1. Ingreso de los años de nacimiento (Si dos o más integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso).
  2. Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
  3. Si todos nacieron después del 2000, mostrar "Grupo Z".
  4. Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
  5. Implementar una función para determinar si un año es bisiesto.
  6. Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.

  Ingreso de los años de nacimiento. 
  
  """
#-----------------------------------------------------------------------------------------------
# Funciones auxiliares:

def es_bisiesto(anio: int) -> bool: # le pido que me devuelva un booleano (V o F)
    """
    Esta funcion determina si un año especifico es bisiesto
    
    Es bisiesto cuando es divisible por 4, excepto si es divisible por 100
    a menos que también sea divisible por 400
    
    Args:
        anio (int): año a verificar
        
    Returns:
            bool: True si el año es bisiesto, false si no lo es.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def calcular_producto_cartesiano(conjunto_a: list, conjunto_b: list) -> list:
    """
    Calcula el producto cartesiano entre dos conjuntos a traves de listas
    
    Args:
        conjunto_a - lista 1
        conjunto_b - lista 2
        
    Returns:
        list: devuelve una lista de tuplas que representa el producto cartesiano
    """
    producto = []
    
    for elemento_a in conjunto_a:
        for elemento_b in conjunto_b:
            producto.append((elemento_a, elemento_b))
    return producto

#-----------------------------------------------------------------------------------------------

# Programa principal:

# 1. operaciones con años de nacimiento:
anio_nacimiento_1 = int(input("Ingrese el primer año de nacimiento: "))
anio_nacimiento_2 = int(input("Ingrese el segundo año de nacimiento: "))

print(f"\n1er Año de nacimiento: {anio_nacimiento_1}")
print(f"\n2do Año de nacimiento: {anio_nacimiento_2}")

# 2. Contar cuantos nacieron en años pares e impares

lista_anios_nacimiento = [anio_nacimiento_1, anio_nacimiento_2]

contador_pares = 0
contador_impares = 0

for anio in lista_anios_nacimiento:
    if anio % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print(f"\n-- Analisis de años --")
print(f"Cantidad de años pares: {contador_pares}")
print(f"Cantidad de años impares: {contador_impares}")

# 3. Si todos nacieron despues del 2000, mostrar que pertenecen a la generacion Z.

if anio_nacimiento_1 > 2000 and anio_nacimiento_2 > 2000:
    print("Pertenecen - Grupo Z")
    
# 4. Si alguien nacio en año bisiesto, mostrar "Tenemos un año especial"
    # Reutilizo la funcion es_bisiesto
if es_bisiesto(anio_nacimiento_1) or es_bisiesto(anio_nacimiento_2):
    print("Nota: Tenemos un año especial!")
    
# 5. implementacion de la funcion es_bisiesto
print("\n-- Comprobador de año Bisiesto --")

anio_a_verificar = int(input("Ingrese un año para determinar si es bisiesto: "))

if es_bisiesto(anio_a_verificar):
    print(f"El año {anio_a_verificar} es Bisiesto!")
else:
    print(f"El año {anio_a_verificar} No es Bisiesto.")
    

# 6. Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales
print("\n--Calculo de Producto Cartesiano--")

anio_actual = datetime.datetime.now().year
edad_1 = anio_actual - anio_nacimiento_1
edad_2 = anio_actual - anio_nacimiento_2

print(f"Edad calculada para el 1er integrante: {edad_1} años.")
print(f"Edad calculada para el 2do integrante: {edad_2} años.")

# convierto el año y edad en texto, y se pasa a una lista en digitos individuales
digitos_anio_1 = list(str(anio_nacimiento_1))
digitos_edad_1 = list(str(edad_1))

digitos_anio_2 = list(str(anio_nacimiento_2))
digitos_edad_2 = list(str(edad_2))

# Calculamos y mostramos los productos cartesianos.
producto_1 = calcular_producto_cartesiano(digitos_anio_1, digitos_edad_1)
print(f"\nEl producto cartesiano de los digitos de {anio_nacimiento_1} y {edad_1} es:")
print(producto_1)

producto_2 = calcular_producto_cartesiano(digitos_anio_2, digitos_edad_2)
print(f"\nEl producto cartesiano de los digitos de {anio_nacimiento_2} y {edad_2} es:")
print(producto_2)