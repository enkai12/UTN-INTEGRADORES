
# Proyecto Integrador: Análisis de Eficiencia de Algoritmos

**Programación I — Comisión 22**  

Un análisis comparativo entre soluciones iterativas y recursivas para un problema de cálculo de promedios, desarrollado como proyecto final de la asignatura.

---

## 👥 Integrantes

- Agustín Emiliano Sotelo Carmelich  - Comisión 22
- Bruno Giuliano Vapore - Comisión 22

---

## 📺 Video Explicativo

[Ver video explicativo del proyecto integrador](https://youtu.be/wNkBKJ2LyiE)

---

## 1. Descripción del Proyecto

Este repositorio contiene el proyecto final integrador de la asignatura **Programación I**, enfocado en el diseño, implementación y análisis de eficiencia de algoritmos.

### 🎯 Problema Central

El objetivo es calcular el promedio de los números positivos contenidos dentro de una lista de enteros. Para simular un escenario realista, se utiliza una lista de notas de alumnos, donde valores negativos (como `-1`) representan ausencias y deben ser excluidos del cálculo.

### 💡 Enfoques Implementados

Se desarrollaron dos soluciones distintas para resolver el mismo problema, permitiendo una comparación directa de su rendimiento y estructura:

- 🔁 **Solución Iterativa:** Utiliza bucles (`for` y `while`) para recorrer la lista de manera secuencial.

- 🔙 **Solución Recursiva:** Resuelve el problema dividiéndolo en subproblemas idénticos más pequeños, con un caso base definido para detener las llamadas.

---

## 2. Estructura del Repositorio

```
Programacion1/
├── carpeta_digital/
│   ├── Trabajo Final Integrador - Programación I - Sotelo Carmelich y Vapore.pdf   # Informe final del proyecto
│   └── Presentación PowerPoint.pptx                                               # Diapositivas de la exposición
├── main/
│   ├── funciones_iterativas.py               # Función iterativa + pruebas de unidad
│   ├── funciones_recursivas.py               # Función recursiva + pruebas de unidad
│   └── prueba_rendimiento_principal.py       # Script para pruebas de rendimiento comparativo
├── README.md                                  # Documentación principal del proyecto
```

---

## 3. Metodología y Desarrollo

### 🔁 Enfoque Iterativo

La función `promedio_iterativo` recorre la lista una sola vez, utilizando dos acumuladores: uno para la suma de los números positivos y otro para el conteo de los mismos. Este enfoque es directo, fácil de entender y altamente eficiente en el uso de memoria, ya que no genera nuevas llamadas en el call stack.

### 🔙 Enfoque Recursivo

La función `promedio_recursivo` aborda el problema desde una perspectiva de "divide y vencerás". En cada llamada, procesa el primer elemento de la lista y se invoca a sí misma con el resto de la lista. El caso base que detiene la recursión es una lista vacía. Aunque es una solución conceptualmente elegante, su principal desventaja es el mayor consumo de memoria en la pila de llamadas (call stack) y el riesgo de provocar un desbordamiento de pila (stack overflow) al procesar listas de gran tamaño.

---

## 4. Pruebas y Análisis de Resultados

### ✅ Pruebas de Funcionalidad

Para garantizar la robustez y correctitud de ambos algoritmos, cada archivo (`funciones_iterativas.py` y `funciones_recursivas.py`) incluye una serie de pruebas de unidad utilizando `assert`. Estos tests cubren los siguientes casos:

- Listas vacías.  
- Listas que contienen únicamente valores positivos.  
- Listas que contienen únicamente valores negativos.  
- Listas mixtas con valores positivos y negativos.

### ⏱️ Análisis de Rendimiento

El script `prueba_rendimiento_principal.py` se dedica exclusivamente a comparar la eficiencia de ambas funciones. Utilizando la librería `timeit`, mide los tiempos de ejecución para procesar listas de gran tamaño y presenta los resultados en una tabla comparativa directamente en la terminal, facilitando una evaluación clara y visual del rendimiento.

### ⚙️ Manejo de Casos Especiales

Para poder realizar pruebas de rendimiento exigentes en la función recursiva sin que colapse, se aumenta manualmente el límite de recursión de Python al inicio del script de pruebas:

```python
# Permite realizar pruebas con listas de gran tamaño en la función recursiva
import sys
sys.setrecursionlimit(200000)
```

---

## 5. Material Complementario

- 📄 **Informe Final (PDF):** Documento detallado con el análisis completo del proyecto.  
- 📊 **Presentación (PowerPoint):** Diapositivas utilizadas en la defensa del proyecto.  
- 📺 **Video Explicativo (YouTube):** [Ver video explicativo del proyecto](https://youtu.be/wNkBKJ2LyiE)

---

## 6. Conclusión

Este proyecto nos permitió obtener una comprensión práctica y profunda sobre cómo la elección de un algoritmo impacta directamente en la eficiencia y escalabilidad de una solución. La principal lección aprendida es que la programación eficaz va más allá de la simple correctitud funcional.

> No alcanza con que el código funcione; también debe ser eficiente, robusto y adaptable a las restricciones del mundo real.
