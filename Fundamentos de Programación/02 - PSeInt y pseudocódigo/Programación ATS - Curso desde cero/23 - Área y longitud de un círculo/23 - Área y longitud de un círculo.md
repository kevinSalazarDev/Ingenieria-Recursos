# 23 - Área y longitud de un círculo

## Objetivo

Calcula el área de un círculo con π·r² y la longitud de su circunferencia con 2·π·r, a partir del radio ingresado.

## Código en PSeInt

```pseint
//Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia

Proceso ejercicio2
	definir radio,area,perimetro como reales;

	Escribir "Ingrese el radio del círculo: ";
	Leer radio;
	
	area <- pi * radio^2;
	perimetro <- 2*pi*radio;
	
	Escribir "El área de la círculo es: ",area;
	Escribir "El perímetro de la circunferencia es: ",perimetro;
	
	
	
FinProceso
```

## Explicación

Identifica las variables de entrada y las variables utilizadas para almacenar los resultados intermedios. Después sigue las operaciones en el mismo orden en que aparecen en el código y comprueba el resultado con valores de prueba.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 23 - Área y longitud de un círculo](23%20-%20%C3%81rea%20y%20longitud%20de%20un%20c%C3%ADrculo.svg)
