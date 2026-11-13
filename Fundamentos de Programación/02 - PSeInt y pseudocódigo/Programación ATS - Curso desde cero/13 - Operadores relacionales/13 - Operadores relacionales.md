# 13 - Operadores relacionales

## Objetivo

Evalúa una expresión de comparación y guarda el resultado lógico (verdadero o falso).

## Código en PSeInt

```pseint
//Operadores Relacionales

Proceso principal
	Definir resultado Como Logico;
	Definir a Como Entero;
	Definir b Como entero;
	Definir c Como Entero;
	
	a <- 10;	
	b <- 20;
	c <- 30;
	
	resultado <- a+b > c;
	
	escribir "El resultado	es: ", resultado;
	
FinProceso
```

## Explicación

El algoritmo declara las variables que necesita, procesa los datos mediante las instrucciones mostradas y presenta el resultado con `Escribir`. Observa especialmente cómo se asignan valores con `<-` y cómo se utilizan las instrucciones de entrada y salida según el ejercicio.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 13 - Operadores relacionales](13%20-%20Operadores%20relacionales.svg)
