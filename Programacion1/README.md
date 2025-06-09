# ✨ Proyecto Integrador — Programación I ✨

## 👥 Integrantes

**Agustín Emiliano Sotelo Carmelich** — Comisión 22  
**Bruno Giuliano Vapore** — Comisión 22

---

## 🚀 Análisis de Eficiencia de Algoritmos Iterativos y Recursivos

Este repositorio contiene el proyecto final integrador de la asignatura **Programación I**, con un enfoque central en el **Análisis de Algoritmos**.

Nuestro objetivo principal es comparar la eficiencia (medida en **tiempo de ejecución**) de dos enfoques distintos para resolver un problema común: el **cálculo del promedio de números positivos** dentro de una lista.

El proyecto desarrolla:

- una **solución iterativa** (usando bucles `for` y `while`)
- y una **solución recursiva** (donde la función se invoca a sí misma)

Para las pruebas de rendimiento, simulamos un escenario realista con **notas de alumnos**, incluyendo valores no válidos (como `-1`) que son inteligentemente **ignorados** en el cálculo.

---

## 💡 Características Destacadas

### 🔸 Implementación Iterativa

Una función optimizada que recorre la lista paso a paso, de forma secuencial, para **sumar y contar** de manera precisa los números positivos.

### 🔹 Implementación Recursiva

Una elegante función que aborda el problema **descomponiéndolo en sub-problemas más pequeños**, hasta alcanzar un caso base simple. Esta solución gestiona internamente la **profundidad de la recursión**.

---

## 🧪 Pruebas de Funcionalidad

Se incluyen **casos de prueba unitarios** con `assert` directamente en los archivos de cada función. Esto asegura y verifica su correcto funcionamiento en diversos escenarios:

- listas vacías
- solo valores positivos
- solo negativos
- listas mixtas

---

## ⏱️ Análisis de Rendimiento

Un script principal está dedicado a **medir y comparar los tiempos de ejecución** de ambas funciones.  
Los resultados se presentan de forma clara en una **tabla en la terminal**, facilitando el análisis visual de la eficiencia.

---

## ⚠️ Manejo de Errores Específicos

El código incorpora un ajuste del **límite de recursión** de Python y una gestión robusta de posibles `RecursionError`.  
Esto permite realizar pruebas con listas **excepcionalmente grandes** sin que el programa colapse, demostrando la **fiabilidad** de las soluciones.

---

## 📂 Estructura del Proyecto

```
Progracion1/main/
├── funciones_iterativas.py         # ➡️ Implementación de la función iterativa y pruebas básicas
├── funciones_recursivas.py         # ➡️ Implementación de la función recursiva y pruebas básicas
├── prueba_rendimiento_principal.py # ➡️ Script principal para pruebas de rendimiento y comparación
└── .gitignore                      # ➡️ Archivos y carpetas ignoradas por Git
```

---

## 🛠️ Tecnologías Utilizadas

### 🐍 Lenguaje de Programación

- **Python 3.x** — Lenguaje principal de desarrollo del proyecto

### 📚 Librerías Estándar de Python

- **random** — Generación eficiente de números aleatorios para las listas de prueba
- **timeit** — Medición precisa y fiaable del tiempo de ejecución
- **sys** — Ajuste programático del límite de recursión

---
