import datetime

#       B. Operaciones con años de nacimiento

#   Ingreso de los años de nacimiento (Si dos o más integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso).
#   Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
#   Si todos nacieron después del 2000, mostrar "Grupo Z".
#   Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
#   Implementar una función para determinar si un año es bisiesto.
#   Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.

#   Ingreso de los años de nacimiento.

nac_1 = int(input("Ingrese el primer año de nacimiento: "))
nac_2 = int(input("Ingrese el segundo año de nacimiento: "))

print(f"Año de Nacimiento N°1: {nac_1}")
print(f"Año de Nacimiento N°2: {nac_2}")


#   Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.




#   Si todos nacieron después del 2000, mostrar "Grupo Z".

if nac_1 > 2000 and nac_2 > 2000:
    print("Grupo Z")



#   Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".

def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return print("Tenemos un año especial")

print(bisiesto(nac_1))
print(bisiesto(nac_2))


#   Implementar una función para determinar si un año es bisiesto.

def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return print("El año es bisiesto")
    else:
        return print("El año NO es bisiesto")

año = int(input("Ingrese un año para determinar si es bisiesto: "))
print(bisiesto(año))

#   Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.


añoActual = datetime.datetime.now().year

conjuntoAño1 = [nac_1]
conjuntoAño2 = [nac_2]

conjuntoEdad1 = [añoActual - nac_1]
conjuntoEdad2 = [añoActual - nac_2]

def productoCartesiano(conjuntoAño, conjuntoEdad):
    producto = []
    for i in conjuntoAño:
        for x in conjuntoEdad:
            producto.append((i, x))

print(productoCartesiano(conjuntoAño1, conjuntoEdad1))

