# Proyecto Integrador — Programación I

## Integrantes

- **Agustín Emiliano Sotelo Carmelich** — Comisión 22  
- **Bruno Giuliano Vapore** — Comisión 22

---

## Análisis de Eficiencia de Algoritmos Iterativos y Recursivos

Este repositorio contiene el proyecto final integrador de la asignatura **Programación I**, enfocado en el **Análisis de Algoritmos**.  
El objetivo principal es **comparar la eficiencia (en tiempo de ejecución)** de dos enfoques diferentes para resolver un mismo problema: el cálculo del **promedio de números positivos** dentro de una lista.

El proyecto implementa una **solución iterativa** (usando bucles) y una **solución recursiva** (donde la función se llama a sí misma).  
Las pruebas de rendimiento simulan un escenario de procesamiento de notas de alumnos, incluyendo valores no válidos (como `-1`) que deben ser ignorados.

---

## Características

- **Implementación Iterativa**  
  Una función eficiente que recorre la lista paso a paso para **sumar y contar** los números positivos.

- **Implementación Recursiva**  
  Una función que resuelve el problema dividiéndolo en partes más pequeñas hasta llegar a un **caso base**, manejando la **profundidad de la recursión**.

- **Pruebas de Funcionalidad**  
  Casos de prueba con `assert` incluidos en cada archivo de función para verificar su correcto funcionamiento con **diversos escenarios**.

- **Análisis de Rendimiento**  
  Un script principal que mide y compara los **tiempos de ejecución** de ambas funciones para distintos tamaños de listas, mostrando los resultados en una **tabla en la terminal**.

- **Manejo de Errores**  
  Se incluye el ajuste del **límite de recursión de Python** y la gestión de posibles `RecursionError` para pruebas con listas muy grandes.

---

## Estructura del Proyecto

📁 Progracion1/main/
├── funciones_iterativas.py # Función iterativa y pruebas básicas
├── funciones_recursivas.py # Función recursiva y pruebas básicas
├── prueba_rendimiento_principal.py # Script principal de pruebas y comparación
└── .gitignore # Archivos y carpetas a ignorar por Git

---

## Tecnologías Utilizadas

- **Python 3.x** — Lenguaje de programación principal.
- **random** — Generación de números aleatorios para los datos de prueba.
- **timeit** — Medición precisa del tiempo de ejecución.
- **sys** — Ajuste del límite de recursión del intérprete.

---
