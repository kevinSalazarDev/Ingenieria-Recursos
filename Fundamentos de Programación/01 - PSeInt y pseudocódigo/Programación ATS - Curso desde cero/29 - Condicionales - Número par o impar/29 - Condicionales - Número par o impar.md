# 29 - Condicionales - Número par o impar

## Objetivo

Determina si un número entero es par o impar comprobando el residuo de dividirlo para dos con el operador Mod.

## Código en PSeInt

```pseint
//Ejercicio 1: Ingrese un numero entero y reportar si es par o impar.

Proceso ejercicio1
	
	Definir num como entero;
	
	Escribir "Ingrese un número: ";
	Leer num;
	
	si	num mod 2 = 0 Entonces
		Escribir "El número ",num," es par";
	SiNo
		Escribir "El número ",num," es impar";
	FinSi
	
FinProceso
```

## Explicación

El programa recibe los datos necesarios y evalúa las condiciones en el orden escrito. Cuando una condición se cumple, ejecuta el bloque correspondiente; de lo contrario, continúa por la alternativa indicada con `SiNo`. Prueba valores de entrada distintos para comprobar cada camino posible.
