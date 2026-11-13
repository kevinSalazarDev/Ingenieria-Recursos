# 27 - Notas de un alumno

## Objetivo

Calcula la calificación final de un alumno combinando el promedio de tres parciales (55 %), el examen final (30 %) y el trabajo final (15 %).

## Código en PSeInt

```pseint
//Un alumno desea saber cual sera su calificacion final en la
//materia de Algortimos. Dicha calificacion se compone de los siguientes porcentajes:


Proceso ejercicio6
	Definir parcial1,parcial2,parcial3,promedio_parcial,examen_final,trabajo_final como real;
	definir nota1,nota2,nota3,nota_final como real;
	
	Escribir "Ingrese la nota del primer parcial: ";
	Leer parcial1;
	Escribir "Ingrese la nota del segundo parcial: ";
	Leer parcial2;
	Escribir "Ingrese la nota del tercer parcial: ";
	Leer parcial3;
	
	promedio_parcial <- (parcial1+parcial2+parcial3)/3;
	
	Escribir "Ingrese la calificacón del examen final: ";
	Leer examen_final;
	Escribir "Ingrese la calificacion del trabajo final: ";
	Leer trabajo_final;
	
	nota1 <- promedio_parcial*55/100;
	nota2 <- examen_final*30/100;
	nota3 <- trabajo_final*15/100;
	nota_final <- nota1+nota2+nota3;
	
	Escribir "La nota final es: ", nota_final;

	
	
	
	
	
	
FinProceso
```

## Explicación

El programa recibe los datos necesarios y evalúa las condiciones en el orden escrito. Cuando una condición se cumple, ejecuta el bloque correspondiente; de lo contrario, continúa por la alternativa indicada con `SiNo`. Prueba valores de entrada distintos para comprobar cada camino posible.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 27 - Notas de un alumno](27%20-%20Notas%20de%20un%20alumno.svg)
