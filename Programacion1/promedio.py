import time, timeit

# --- Función de promedio --- #
def promedio(notas):
    start = time.time()
    suma = 0
    for i in range(len(notas)):
        suma += notas[i]
    promedio = round(suma / len(notas), 2)
    end = time.time()
    return promedio, (end-start) * 1000


notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(promedio(notas))


## Probando con timeit ##

tiempo = timeit.timeit(stmt= "promedio(notas)", setup= "from __main__ import promedio, notas", number= 10000)
print(tiempo * 1000)


