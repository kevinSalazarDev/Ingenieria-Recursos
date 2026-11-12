# 24 - Porcentaje de hombres y mujeres

## Objetivo

Calcula el total de estudiantes y el porcentaje que representan hombres y mujeres respecto del total.

## Código en PSeInt

```pseint
// Un maestro desea saber que porcentaje de hombres y que porcentaje
// de mujeres hay en un grupo de estudiantes.
Proceso ejercicio3
	Definir hombres, mujeres, total_estudiantes, porcentaje_hombres, porcentaje_mujeres Como Real;
	Escribir 'Ingrese el número de hombres: ';
	Leer hombres;
	Escribir 'Ingrese el número de mujeres: ';
	Leer mujeres;
	
	total_estudiantes <- hombres+mujeres;
	porcentaje_hombres <- hombres/total_estudiantes*100;
	porcentaje_mujeres <- mujeres/total_estudiantes*100;
	
	Escribir 'El porcentaje de hombres es: ', porcentaje_hombres,"%";
	Escribir 'El porcentaje de mujeres es: ', porcentaje_mujeres,"%";
FinProceso
```

## Explicación

Identifica las variables de entrada y las variables utilizadas para almacenar los resultados intermedios. Después sigue las operaciones en el mismo orden en que aparecen en el código y comprueba el resultado con valores de prueba.
