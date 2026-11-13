# 14 - Operadores lógicos

## Objetivo

Combina dos comparaciones mediante el operador lógico Y para obtener un valor lógico.

## Código en PSeInt

```pseint
//Operadores Logicos

Proceso Principal
	Definir a,b,c como enteros;
	definir resultado Como Logico;
	
	a <- 10;
	b <- 15;
	c <- 20;
	
	resultado <- ((a>b) y (b<c));
	
	Escribir resultado;
	

	
FinProceso
```

## Explicación

El algoritmo declara las variables que necesita, procesa los datos mediante las instrucciones mostradas y presenta el resultado con `Escribir`. Observa especialmente cómo se asignan valores con `<-` y cómo se utilizan las instrucciones de entrada y salida según el ejercicio.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 14 - Operadores lógicos](14%20-%20Operadores%20l%C3%B3gicos.svg)
