# ✨ Proyecto Integrador — Programación I ✨

## 👥 Integrantes

- **Agustín Emiliano Sotelo Carmelich** — Comisión 22  
- **Bruno Giuliano Vapore** — Comisión 22

📺 [Ver video explicativo del proyecto integrador](https://youtu.be/wNkBKJ2LyiE)

---

## 🚀 Análisis de Eficiencia de Algoritmos Iterativos y Recursivos

Este repositorio contiene el **proyecto integrador final** de la asignatura **Programación I**, centrado en el **análisis de eficiencia de algoritmos**.

El objetivo principal es comparar el desempeño de dos enfoques distintos para resolver un mismo problema:  
> **Calcular el promedio de números positivos dentro de una lista.**

Se implementan:

- 🌀 Una **solución recursiva** (la función se llama a sí misma)
- 🔁 Una **solución iterativa** (usando bucles `for` y `while`)

Para las pruebas se simula un caso realista con **notas de alumnos**, donde valores como `-1` representan ausencias y son **excluidos del cálculo del promedio**.

---

## 💡 Características Destacadas

### 🔸 Enfoque Iterativo

Función optimizada que recorre la lista paso a paso, acumulando la suma y el conteo de números positivos de forma simple y eficiente.

### 🔹 Enfoque Recursivo

Solución elegante que resuelve el problema dividiéndolo en subproblemas más pequeños, utilizando una estructura recursiva con un caso base claro.

---

## 🧪 Pruebas de Funcionalidad

Cada archivo contiene **tests con `assert`** que validan el correcto funcionamiento de las funciones ante distintos escenarios:

- ✅ Listas vacías  
- ✅ Solo valores positivos  
- ✅ Solo valores negativos  
- ✅ Listas mixtas (positivos y negativos)

---

## ⏱️ Análisis de Rendimiento

Se incluye un script principal dedicado a:

- Medir tiempos de ejecución con `timeit`
- Comparar el rendimiento de ambas funciones
- Mostrar los resultados en una **tabla legible en la terminal**

Esto permite un análisis visual rápido y efectivo.

---

## ⚙️ Manejo de Casos Especiales

Para probar listas **muy grandes**, se aumenta el **límite de recursión** mediante:

```python
import sys
sys.setrecursionlimit(200000)
