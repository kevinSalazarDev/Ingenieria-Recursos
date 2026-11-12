# 18 - Operaciones aritméticas - Ejercicio 3

## Objetivo

Intercambia los valores de dos variables enteras utilizando una tercera variable auxiliar para no perder ninguno de los datos.

## Código en PSeInt

```pseint
//Ejercicio 3: Intercambiar el valor de 2 variables

Proceso principal
	definir a,b,aux como enteros;
	
	Escribir "Ingrese el valor de a: ";
	leer a;
	Escribir "Ingrese el valor de b: ";
	Leer b;
	
	aux <- a;
	a <- b;
	b <- aux;
	
	escribir "El nuevo valor de a es: ", a;
	Escribir "El nuevo valor de b es: ", b;
	

	
FinProceso
```

## Explicación

El programa sigue una secuencia de pasos: define los datos necesarios, obtiene los valores de entrada cuando corresponde, realiza el cálculo o evaluación y comunica el resultado. Revisa el orden de las instrucciones y el papel de cada variable para comprender cómo fluye la información.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 18 - Operaciones aritméticas - Ejercicio 3](18%20-%20Operaciones%20aritm%C3%A9ticas%20-%20Ejercicio%203.svg)
