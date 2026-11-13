# 30 - Condicionales - Alumno aprobado o desaprobado

## Objetivo

Calcula el promedio de tres calificaciones y utiliza una condición para indicar si el alumno aprueba con 70 o más.

## Código en PSeInt

```pseint
//Determinar si un alumon aprueba o reprueba un curso,
//sabiendo que aprobara si su promedio de tres calificaciones
//es mayo o igual a 70; repureba caso contrario.
//(diagrama  de flujo)

Proceso ejercicio1
	Definir nota1,nota2,nota3,promedio como reales;
	
	Escribir "Ingrese las tres notas: ";
	Leer nota1,nota2,nota3;
	
	promedio <- (nota1+nota2+nota3)/3;
	
	si promedio >= 70 Entonces
		Escribir "Aprobado con: ", promedio;
	SiNo
		Escribir "Reprobado con: ",promedio;
	FinSi
	
FinProceso
```

## Explicación

El programa recibe los datos necesarios y evalúa las condiciones en el orden escrito. Cuando una condición se cumple, ejecuta el bloque correspondiente; de lo contrario, continúa por la alternativa indicada con `SiNo`. Prueba valores de entrada distintos para comprobar cada camino posible.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 30 - Condicionales - Alumno aprobado o desaprobado](30%20-%20Condicionales%20-%20Alumno%20aprobado%20o%20desaprobado.svg)
