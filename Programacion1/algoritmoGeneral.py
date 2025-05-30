import promedio, promedioRecursivo

# --- Algoritmo general --- #

notas = []              # Inicializamos la variable notas como una lista vacía
num = float('inf')      # Inicializamos la variable num como flotante (infinito) para comenzar el bucle while

while num != 0:
    num = float(input("Ingrese las notas del alumno (0 para finalizar): "))     # El programa pide números positivos hasta que se ingrese el 0.

    if num > 0:
        notas.append(num)       # Si el numero es positivo, se agrega a la lista de notas.
    elif num < 0:               
        print("¡Error!, no puede ingresar números negativos")  # Si el numero es negativo, no se agrega y salta mensaje de error.
    else:
        print("Ha finalizado el ingreso de notas")            # Cuando se ingresa 0 y la condición del while se vuelve falsa y termine el bucle.

print(f"Con las notas ingresadas {notas}, el promedio es {promedio(notas)}") # Llamado a la función
print(f"Con las notas ingresadas {notas}, el promedio es {promedioRecursivo(notas)}") # Llamado a la función recursiva