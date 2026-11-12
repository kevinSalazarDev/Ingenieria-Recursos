# 40 - Ciclos - Suma de los primeros N números

## Objetivo

Solicita un número N y acumula, mediante un ciclo Para, la suma de todos los enteros desde 1 hasta N.

## Código en PSeInt

```pseint
//Ejercicio 1: Calcular la suma de los "N" primeros números.

Proceso ejericicio1
	Definir N,suma,i Como Entero;
	
	Escribir "Ingrese la cantidad de números a sumarse: ";
	Leer N;
	
	suma <- 0;
	
	Para i <- 1 hasta  N Con Paso 1 Hacer
		suma <- suma + i;
		
	FinPara
	
	Escribir "La suma es: ",suma;
	
	
FinProceso
```

## Explicación

El algoritmo utiliza una estructura de selección o repetición, según corresponda. Sigue la variable de control y revisa cuándo se cumple la condición para entender qué instrucciones se ejecutan y cuántas veces. Comprueba el comportamiento con distintos valores de entrada, incluidos los límites indicados en el ejercicio.
