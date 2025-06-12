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








































nac_1 = int(input("Ingrese el primer año de nacimiento: "))
nac_2 = int(input("Ingrese el segundo año de nacimiento: "))

print(f"Año de Nacimiento N°1: {nac_1}")
print(f"Año de Nacimiento N°2: {nac_2}")

#   Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.

listaAños = []
listaAños.append(nac_1)
listaAños.append(nac_2)

contadorPar = 0
contadorImpar = 0 

for i in listaAños:
    if i % 2 == 0:
        contadorPar += 1
    else:
        contadorImpar += 1

print(f"La cantidad de años pares es: {contadorPar}. Y la cantidad de años impares es: {contadorImpar}")

#   Si todos nacieron después del 2000, mostrar "Grupo Z".

if nac_1 > 2000 and nac_2 > 2000:
    print("Grupo Z")

#   Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".

if ((nac_1 % 4 == 0 and nac_1 % 100 != 0) or (nac_1 % 400 == 0)) or ((nac_2 % 4 == 0 and nac_2 % 100 != 0) or (nac_2 % 400 == 0)):  # Se evalúa los dos años ingresados (or),
    print("Tenemos un año especial")                                                                                                # al menos uno de ellos debe ser bisiesto

#   Implementar una función para determinar si un año es bisiesto.

def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return print("El año es bisiesto")
    else:
        return print("El año NO es bisiesto")

año = int(input("Ingrese un año para determinar si es bisiesto: "))
bisiesto(año)

#   Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.

listaNac1 = []                  # Creamos listas vacias para incoporar cada digito del año como elemento
listaNac2 = []
for i in str(nac_1):            # Es necesario transformar el entero en cadena (str) para poder iterar
    listaNac1.append(i)
for i in str(nac_2):
    listaNac2.append(i)

añoActual = datetime.datetime.now().year  # Obtenemos el año actual para luego calcular la edad (sin considerar día/mes)
edad1 = añoActual - nac_1
edad2 = añoActual - nac_2

listaEdad1 = []                  # Repetimos el proceso de armar una lista para la edad
listaEdad2 = []                   
for i in str(edad1):           
    listaEdad1.append(i)
for i in str(edad2):
    listaEdad2.append(i)

def productoCartesiano(conjuntoAño, conjuntoEdad):  # Creamos una función para armar el producto cartesiano con blucles
    producto = []                                   # Definimos una variable como lista vacia
    for a in conjuntoAño:                           # El bucle recorre la lista del año ingresada
        for b in conjuntoEdad:                          # Y por cada iteración, el bucle anidado recorre la lista de la edad ingresada
            producto.append((a, b))                         # En cada iteración se agrega a la lista 'producto' los valores determinados por a y b
    return producto

print(f"El producto cartesiando de {listaNac1} x {listaEdad1} es {productoCartesiano(listaNac1, listaEdad1)}")
print(f"El producto cartesiando de {listaNac2} x {listaEdad2} es {productoCartesiano(listaNac2, listaEdad2)}")