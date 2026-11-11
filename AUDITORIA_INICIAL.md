# Auditoría inicial y registro de correcciones

**Última actualización:** 11 de noviembre de 2026  
**Estado:** correcciones iniciales integradas en `main`.

## Resumen del inventario

En la revisión inicial se localizaron 41 archivos Python, 34 archivos PSeInt (`.psc`), 100 archivos Flowgorithm (`.fprg`) y archivos DFD. Se revisó estáticamente el contenido de los archivos Python y se inspeccionaron ejemplos representativos de PSeInt y Flowgorithm. No se ejecutó toda la colección en sus aplicaciones respectivas.

## Correcciones Python integradas

Se corrigieron diez archivos Python y los cambios se incorporaron a la rama principal mediante el Pull Request [#2](https://github.com/kevinSalazarDev/Programacion/pull/2):

| Archivo | Corrección |
|---|---|
| `Programación ATS/13 - Operadores - Ejercicio 1 - Operación aritmética.py` | Se eliminó el texto suelto que causaba error de sintaxis y se añadió validación para evitar división entre cero cuando `b == 0`. |
| `Tutoriales Programación Ya/1.py` | Se corrigió la indentación y se completó el texto de entrada del precio. |
| `Programación ATS/18 - Condicionales - Estructura if-elif-else.py` | Se implementaron los casos positivo, negativo y cero; se quitaron mensajes de prueba. |
| `Curso de Python - ejercicios/7_eliminar_prefijos.py` | Se guardó e imprimió la cadena devuelta por `removeprefix()`. |
| `CS50/hola7.py` | Se modificó la separación del nombre para admitir uno o más nombres sin provocar `ValueError`. |
| `Tutoriales Programación Ya/11 - Condicional - Comparar dos números.py` | Se añadió control para no dividir entre cero. |
| `Tutoriales Programación Ya/18 - Condicionales anidados - Prueba de capacitación.py` | Se validó que el total de preguntas sea mayor que cero y que las respuestas correctas estén dentro del rango permitido. |
| `Tutoriales Programación Ya/13 - Condicional - Mostrar uno o dos dígitos.py` | Se validó el rango de números positivos de uno o dos dígitos. |
| `Tutoriales Programación Ya/17 - Condicionales anidados - Cantidad de cifras.py` | Se validó el rango de números positivos de hasta tres cifras. |
| `Curso de Python - ejercicios/0_hello_world.py` | Se corrigieron erratas del mensaje en inglés. |

### Verificación y límites

Los diez archivos modificados se volvieron a leer y pasaron una comprobación sintáctica con `ast.parse` durante la revisión. Después se añadió el script `scripts/check_python_syntax.py` y un flujo de GitHub Actions. La primera ejecución en la rama principal terminó correctamente: el flujo comprobó la sintaxis de los 41 archivos Python detectados.

Además, se realizaron 26 pruebas puntuales de comportamiento simulando entradas en los diez ejercicios corregidos. Se incluyeron casos normales, límites, nombres de una o varias palabras, valores cero y entradas fuera de rango. Las 26 comprobaciones de salida esperada pasaron.

Estas pruebas puntuales **no equivalen a una suite exhaustiva ni demuestran que toda la lógica sea correcta**. La comprobación automática revisa sintaxis, no ejecuta los programas. Es necesario continuar probando los ejercicios con datos reales y contrastar su comportamiento con los enunciados originales.

## Pendientes de PSeInt

- `22.2 - Estructura secuencial - Ejercicio 1.psc` contiene únicamente un proceso vacío. No se inventó una solución ni se modificó el archivo porque hace falta confirmar qué ejercicio debía contener.
- `22.1 - Estructura secuencial - Ejercicio 1.psc` contiene un algoritmo de conversión de horas, minutos y segundos a segundos que parece coherente en la inspección.
- No se certificó la ejecución de los 34 archivos en PSeInt.

## Pendientes de Flowgorithm y DFD

- Se inspeccionaron ejemplos `.fprg` de TestingDocs y Art0xdev. Su estructura XML parece bien formada a simple vista.
- No se validaron los 100 archivos `.fprg` ejecutándolos en Flowgorithm ni los diagramas `.dfd` en su aplicación correspondiente.
- Hay ejercicios con nombres repetidos o variantes numeradas. No deben eliminarse sin comparar sus contenidos y confirmar si son soluciones alternativas.

## Próximas mejoras recomendadas

1. Ejecutar los diez ejercicios Python corregidos con entradas normales, límites y entradas inválidas.
2. Revisar los otros 31 archivos Python con pruebas de ejecución y resultados esperados.
3. Identificar el enunciado correcto del archivo PSeInt vacío antes de completarlo.
4. Abrir y comprobar los archivos PSeInt y Flowgorithm en sus aplicaciones.
5. Comparar los ejercicios duplicados antes de decidir si se mantienen o renombran.
6. Verificar la procedencia y las condiciones de uso de los archivos binarios y materiales externos.

## Alcance y conservación

La reorganización documental y las correcciones iniciales de Python se integraron en `main` mediante los Pull Requests #1 y #2. No se borraron ejercicios durante esas tareas. Los archivos PSeInt, Flowgorithm y DFD no se modificaron en la etapa de correcciones Python.
