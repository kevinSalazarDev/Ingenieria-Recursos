# Auditoría inicial de ejercicios

**Fecha:** 10 de noviembre de 2026  
**Rama revisada:** `mejoras-documentacion`  
**Alcance:** revisión estática de los archivos de ejercicios. Este documento registra hallazgos; no modifica los programas.

## Resumen

Se localizaron 41 archivos Python, 34 archivos PSeInt (`.psc`), 100 archivos Flowgorithm (`.fprg`) y archivos de diagramas DFD (`.dfd`). Se revisó el contenido de los 41 archivos Python y se inspeccionaron ejemplos representativos de PSeInt y Flowgorithm. No se ejecutaron los programas en sus entornos respectivos, por lo que esta auditoría no equivale a una certificación de funcionamiento.

## Hallazgos en Python

| Archivo | Hallazgo | Prioridad |
|---|---|---|
| `Programación ATS/13 - Operadores - Ejercicio 1 - Operación aritmética.py` | Contiene una línea incompleta `prin`, que provoca un error de sintaxis e impide ejecutar el archivo. También contiene dos expresiones `print` aisladas que no muestran nada. | Alta |
| `Tutoriales Programación Ya/1.py` | La indentación de las líneas dentro del bloque principal es inconsistente; Python genera `IndentationError`. | Alta |
| `Programación ATS/18 - Condicionales - Estructura if-elif-else.py` | El ejercicio anuncia una estructura `if-elif-else`, pero solo evalúa si el número es positivo y luego imprime dos mensajes de prueba (`hola`, `hola2`). | Media |
| `Curso de Python - ejercicios/7_eliminar_prefijos.py` | `removeprefix()` devuelve una nueva cadena, pero el resultado no se guarda ni se imprime; por eso el valor original permanece. | Media |
| `CS50/hola7.py` | `split(" ")` espera exactamente dos partes. Un nombre de una sola palabra, varios espacios o más de dos palabras puede provocar `ValueError`. | Media |
| `Tutoriales Programación Ya/11 - Condicional - Comparar dos números.py` | En la rama de división, si el segundo número es cero, se produce `ZeroDivisionError`. | Media |
| `Tutoriales Programación Ya/18 - Condicionales anidados - Prueba de capacitación.py` | Si el total de preguntas es cero, el cálculo del porcentaje divide entre cero. | Media |
| `Programación ATS/13 - Operadores - Ejercicio 1 - Operación aritmética.py` | Si el valor de `b` es cero, el cálculo divide entre cero. | Media |
| `Tutoriales Programación Ya/13 - Condicional - Mostrar uno o dos dígitos.py` y `17 - Condicionales anidados - Cantidad de cifras.py` | No validan que el número sea positivo, aunque el enunciado del segundo sí lo exige; los negativos se clasifican incorrectamente. El primero tampoco distingue correctamente números de más de dos cifras. | Media |
| `Curso de Python - ejercicios/0_hello_world.py` | Hay errores tipográficos en el segundo mensaje (`coourse`, `wordl`). No impiden la ejecución, pero conviene corregirlos cuando se autorice editar contenido. | Baja |

Los demás archivos Python revisados no mostraron errores evidentes de sintaxis durante la lectura estática. Eso no garantiza que todos los resultados sean correctos para cualquier entrada.

## Hallazgos en PSeInt

- `22.2 - Estructura secuencial - Ejercicio 1.psc` contiene únicamente un proceso vacío (`Proceso sin_titulo ... FinProceso`). Parece un archivo de prueba o un ejercicio sin desarrollar.
- `22.1 - Estructura secuencial - Ejercicio 1.psc` contiene el algoritmo de conversión de horas, minutos y segundos a segundos y su estructura parece coherente en la inspección.
- Se inspeccionaron también ejemplos de condicionales y ciclos; no se certificó la ejecución de los 34 archivos en PSeInt.

## Hallazgos en Flowgorithm

- Se inspeccionaron ejemplos `.fprg` de TestingDocs y Art0xdev. Su estructura XML parece bien formada a simple vista y contiene nodos de flujo coherentes.
- La colección incluye 100 archivos `.fprg` y también diagramas `.dfd`. Los `.dfd` usan un formato distinto; no se validaron con Flowgorithm ni con el programa que los creó.
- Hay ejercicios con nombres repetidos o variantes numeradas (por ejemplo, variantes `13`/`13.1`, `21`/`21.1`, `4`/`4.1`). No deben eliminarse sin comparar sus contenidos y confirmar si son soluciones alternativas.

## Orden recomendado para la corrección

1. Corregir los dos errores de sintaxis de Python: `Programación ATS/13...` y `Tutoriales Programación Ya/1.py`.
2. Completar o identificar como borrador el archivo PSeInt vacío `22.2...`.
3. Revisar la lógica y los casos límite de los ejercicios indicados en la tabla.
4. Probar los 41 programas Python con entradas normales y casos límite.
5. Abrir los archivos PSeInt y Flowgorithm en sus aplicaciones para comprobarlos realmente, y comparar los ejercicios duplicados antes de decidir si se renombran o se mantienen.

## Garantía de alcance

Esta auditoría no ha modificado ningún archivo de código, pseudocódigo ni diagrama. Los hallazgos son observaciones para revisión posterior; las correcciones deben realizarse en una etapa separada y conservar los originales.
