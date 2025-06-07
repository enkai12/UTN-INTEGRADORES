#       A. Operaciones con DNIs

#   Ingreso de los DNIs (reales o ficticios).
#   Generación automática de los conjuntos de dígitos únicos.
#   Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
#   Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
#   Suma total de los dígitos de cada DNI.
#   Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas


# Ingreso de los DNIs

dni_1 = input("Ingrese el primer DNI: ")
dni_2 = input("Ingrese el segundo DNI: ")

print(f"DNI: {dni_1}")
print(f"DNI: {dni_2}\n")


#   Generación automática de los conjuntos de dígitos únicos.

conjuntoDni1 = set(dni_1)
conjuntoDni2 = set(dni_2)

print(f"Conjunto de digitos únicos del DNI N°1: {conjuntoDni1}")
print(f"Conjunto de digitos únicos del DNI N°2: {conjuntoDni2}\n")


#   Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.

print(f"Siendo los conjuntos A = {conjuntoDni1} y B = {conjuntoDni2}")

# UNIÓN
union = conjuntoDni1.union(conjuntoDni2)
print(f"A ∪ B = {union}")

# INTERSECCIÓN
inter = conjuntoDni1 & conjuntoDni2
print(f"A ∩ B = {inter}")

# DIFERENCIAS
difA_B = conjuntoDni1.difference(conjuntoDni2)
difB_A = conjuntoDni2.difference(conjuntoDni1)
print(f"A - B = {difA_B}")
print(f"B - A = {difB_A}")

# DIFERENCIA SIMETRICA
difSimetrica = conjuntoDni1 ^ conjuntoDni2
print(f"A Δ B = {difSimetrica}\n")


#   Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.

def frecuencia(dni):
    listaContadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for digito in str(dni):
        listaContadores[int(digito)] += 1
    return (f"Cero: {listaContadores[0]}\nUno: {listaContadores[1]}\nDos: {listaContadores[2]}\nTres: {listaContadores[3]}\nCuatro: {listaContadores[4]}\nCinco: {listaContadores[5]}\nSeis: {listaContadores[6]}\nSiete: {listaContadores[7]}\nOcho: {listaContadores[8]}\nNueve: {listaContadores[9]}\n ")

print(f"En el primer DNI la frecuencia de cada dígito es:\n{frecuencia(dni_1)}") 
print(f"En el segundo DNI la frecuencia de cada dígito es:\n{frecuencia(dni_2)}\n") 

#  Suma total de los dígitos de cada DNI.

sumaDni_1 = 0
sumaDni_2 = 0

for i in dni_1:
    sumaDni_1  += int(i)
print(f"La suma de los dígitos de {dni_1} es: {sumaDni_1}")

for i in dni_2:
    sumaDni_2  += int(i)
print(f"La suma de los dígitos de {dni_2} es: {sumaDni_2}\n")

#   Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas

#   Expresión N°1:
print("Hay al menos un dígito en el conjunto A que se repite en el conjunto B")

if conjuntoDni1 & conjuntoDni2:
    print(f"Verdadero. Hay al menos un número que se repite: {conjuntoDni1 & conjuntoDni2}\n")
else:
    print(f"Falso. No se repite ningún número\n")

#   Expresión N°2:
print("El mayor dígito del conjunto B no supera al mayor dígito del conjunto A")

maxDni1 = max(conjuntoDni1)
maxDni2 = max(conjuntoDni2)
if maxDni2 > maxDni1:
    print(f"Falso. El mayor número del conjunto B es {maxDni2} y del conjunto A es {maxDni1}. Por lo tanto {maxDni2} > {maxDni1}")
else:
    print(f"Verdadero. El mayor número del conjunto B es {maxDni2} y del conjunto A es {maxDni1}. Por lo tanto {maxDni2} < {maxDni1}")