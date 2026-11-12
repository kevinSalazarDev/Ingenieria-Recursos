# 16 - Operaciones aritméticas - Ejercicio 1

## Objetivo

Calcula una de las soluciones de una ecuación cuadrática mediante la fórmula general, usando los coeficientes ingresados.

## Código en PSeInt

```pseint
Proceso principal
	Definir a,b,c,resultado como reales;
	
	Escribir "Ingrese el valor de a: ";
	leer a;
	Escribir "Ingrese el valor de b: ";
	leer b;
	Escribir "Ingrese el valor de c: ";
	leer c; 
	
	resultado <- (-b + raiz(b^2 - 4*a*c))/(2*a);
	
	Escribir "El resultado es: ", resultado;
	
FinProceso
```

## Explicación

El programa sigue una secuencia de pasos: define los datos necesarios, obtiene los valores de entrada cuando corresponde, realiza el cálculo o evaluación y comunica el resultado. Revisa el orden de las instrucciones y el papel de cada variable para comprender cómo fluye la información.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 16 - Operaciones aritméticas - Ejercicio 1](16%20-%20Operaciones%20aritm%C3%A9ticas%20-%20Ejercicio%201.svg)
