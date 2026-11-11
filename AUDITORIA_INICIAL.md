# Auditoría inicial y registro de correcciones

**Fecha:** 10 de noviembre de 2026  
**Rama de auditoría:** `mejoras-documentacion`  
**Rama de correcciones:** `correcciones-python-iniciales`

## Resumen

Se localizaron 41 archivos Python, 34 archivos PSeInt (`.psc`), 100 archivos Flowgorithm (`.fprg`) y archivos DFD. Se revisó el contenido de los 41 archivos Python y se inspeccionaron ejemplos representativos de PSeInt y Flowgorithm. No se ejecutaron los programas en sus entornos respectivos, por lo que esta revisión no equivale a una certificación completa.

## Correcciones realizadas en Python

Se corrigieron diez archivos en la rama `correcciones-python-iniciales`:

| Archivo | Corrección |
|---|---|
| `Programación ATS/13 - Operadores - Ejercicio 1 - Operación aritmética.py` | Se eliminó el texto suelto que causaba error de sintaxis y se añadió validación para evitar división entre cero cuando `b == 0`. |
| `Tutoriales Programación Ya/1.py` | Se corrigió la indentación y se completó el texto de entrada del precio. |
| `Programación ATS/18 - Condicionales - Estructura if-elif-else.py` | Se implementaron los tres casos: positivo, negativo y cero; se quitaron mensajes de prueba. |
| `Curso de Python - ejercicios/7_eliminar_prefijos.py` | Se guardó e imprimió la cadena devuelta por `removeprefix()`. |
| `CS50/hola7.py` | Se cambió la separación del nombre para admitir uno o más nombres sin provocar `ValueError`. |
| `Tutoriales Programación Ya/11 - Condicional - Comparar dos números.py` | Se añadió control para no dividir entre cero. |
| `Tutoriales Programación Ya/18 - Condicionales anidados - Prueba de capacitación.py` | Se validó que el total de preguntas sea mayor que cero y que las respuestas correctas estén dentro del rango permitido. |
| `Tutoriales Programación Ya/13 - Condicional - Mostrar uno o dos dígitos.py` | Se validó el rango de números positivos de uno o dos dígitos. |
| `Tutoriales Programación Ya/17 - Condicionales anidados - Cantidad de cifras.py` | Se validó el rango de números positivos de hasta tres cifras. |
| `Curso de Python - ejercicios/0_hello_world.py` | Se corrigieron las erratas del mensaje en inglés. |

### Verificación realizada

Los diez archivos modificados se volvieron a leer desde la rama de correcciones y se comprobó su sintaxis con el analizador AST de Python (`ast.parse`). Los diez pasaron esa comprobación sintáctica.

Esta prueba **no equivale a ejecutar los programas con entradas reales**. Todavía se deben probar casos normales y extremos, y confirmar que el comportamiento corresponde exactamente a los enunciados originales. En particular, se recomienda revisar con el material fuente si la intención pedagógica de cada ejercicio coincide con las validaciones añadidas.

## Pendientes de PSeInt

- `22.2 - Estructura secuencial - Ejercicio 1.psc` contiene únicamente un proceso vacío. No se inventó una solución ni se modificó el archivo porque hace falta confirmar qué ejercicio debía contener.
- `22.1 - Estructura secuencial - Ejercicio 1.psc` contiene un algoritmo de conversión de horas, minutos y segundos a segundos que parece coherente en la inspección.
- No se certificó la ejecución de los 34 archivos en PSeInt.

## Pendientes de Flowgorithm y DFD

- Se inspeccionaron ejemplos `.fprg` de TestingDocs y Art0xdev. Su estructura XML parece bien formada a simple vista.
- No se validaron los 100 archivos `.fprg` ejecutándolos en Flowgorithm ni los diagramas `.dfd` en su aplicación correspondiente.
- Hay ejercicios con nombres repetidos o variantes numeradas. No deben eliminarse sin comparar sus contenidos y confirmar si son soluciones alternativas.

## Próximos pasos recomendados

1. Probar los diez archivos Python corregidos con entradas normales, valores límite y entradas inválidas.
2. Revisar los 31 archivos Python restantes con pruebas de ejecución y resultados esperados.
3. Identificar el enunciado correcto del archivo PSeInt vacío antes de completarlo.
4. Abrir y comprobar los archivos PSeInt y Flowgorithm en sus aplicaciones.
5. Comparar los ejercicios duplicados antes de decidir si se mantienen o renombran.

## Alcance y conservación

Las correcciones se hicieron en una rama separada. La rama `main` y la rama `mejoras-documentacion` no se modificaron con estas correcciones. No se borraron ejercicios ni se alteraron archivos PSeInt, Flowgorithm o DFD.
