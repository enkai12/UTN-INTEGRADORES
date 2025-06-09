# # ✨ Proyecto Integrador — Programación I ✨

## ## 👥 Integrantes

* **Agustín Emiliano Sotelo Carmelich** — Comisión 22
* **Bruno Giuliano Vapore** — Comisión 22

📺 [Ver video explicativo del proyecto integrador](https://youtu.be/wNkBKJ2LyiE)

---

## ## 📂 Estructura del Repositorio

```
Programacion1/
├── carpeta_digital/                         
│   ├── Trabajo Final Integrador - Programación I - Sotelo Carmelich y Vapore.pdf   # Informe final del proyecto
│   └── Presentación PowerPoint.pptx                                               # Diapositivas de la exposición
├── main/
│   ├── funciones_iterativas.py               # Función iterativa + pruebas
│   ├── funciones_recursivas.py               # Función recursiva + pruebas
│   └── prueba_rendimiento_principal.py       # Script para pruebas de rendimiento
├── README.md                                  # Documentación principal del proyecto
```

---

## ## 🚀 Análisis de Eficiencia de Algoritmos Iterativos y Recursivos

Este repositorio contiene el **proyecto integrador final** de la asignatura **Programación I**, centrado en el **análisis de eficiencia de algoritmos**.

### ### 🔹 Problema a Resolver

> **Calcular el promedio de números positivos dentro de una lista.**

### ### 🔹 Enfoques Implementados

* 🔀 Una **solución recursiva** (la función se llama a sí misma)
* 🔁 Una **solución iterativa** (usando bucles `for` y `while`)

Para las pruebas se simula un caso realista con **notas de alumnos**, donde valores como `-1` representan ausencias y son **excluidos del cálculo del promedio**.

---

## ## 💡 Características Destacadas

### ### 🔘 Enfoque Iterativo

Función optimizada que recorre la lista paso a paso, acumulando la suma y el conteo de números positivos de forma simple y eficiente.

### ### 🔙 Enfoque Recursivo

Solución elegante que resuelve el problema dividiéndolo en subproblemas más pequeños, utilizando una estructura recursiva con un caso base claro.

---

## ## 🧪 Pruebas de Funcionalidad

Cada archivo contiene **tests con `assert`** que validan el correcto funcionamiento de las funciones ante distintos escenarios:

* Listas vacías
* Solo valores positivos
* Solo valores negativos
* Listas mixtas (positivos y negativos)

---

## ## ⏱️ Análisis de Rendimiento

Se incluye un script principal dedicado a:

* Medir tiempos de ejecución con `timeit`
* Comparar el rendimiento de ambas funciones
* Mostrar los resultados en una **tabla legible en la terminal**

Esto permite un análisis visual rápido y efectivo.

---

## ## ⚙️ Manejo de Casos Especiales

Para probar listas **muy grandes**, se aumenta el **límite de recursión** mediante:

```python
import sys
sys.setrecursionlimit(200000)
```

Esto permite realizar pruebas de rendimiento más exigentes sin que la función recursiva colapse por el límite predeterminado de Python.

---

## ## 📌 Material Complementario

* 📄 Informe PDF del trabajo final
* 📊 Presentación PowerPoint
* 🎥 Video explicativo del proyecto

---

## ## ✅ Conclusión

Este proyecto nos permitió entender en profundidad cómo se comportan los algoritmos en diferentes contextos, y nos dejó un mensaje clave:

> **No alcanza con que el código funcione, también debe ser eficiente, robusto y adaptable al mundo real.**
