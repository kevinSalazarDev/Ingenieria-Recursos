# 17 - Operaciones aritméticas - Ejercicio 2

## Objetivo

Evalúa una expresión que combina operaciones aritméticas, comparaciones y operadores lógicos, junto con una comparación entre dos valores ingresados.

## Código en PSeInt

```pseint
//Ejercicio 2

Proceso Principal
	Definir a,b como reales;
	Definir resultado Como Logico;
	
	Escribir "Ingrese el valor de a: ";
	leer a;
	
	Escribir "Ingrese el valor de b: ";
	leer b; 
	
	resultado <- ((3+5*8)<3 y ((-6/3*4)+2<2)) o (a>b);
	
	Escribir "El resultado es: ", resultado;
	
FinProceso
```

## Explicación

El programa sigue una secuencia de pasos: define los datos necesarios, obtiene los valores de entrada cuando corresponde, realiza el cálculo o evaluación y comunica el resultado. Revisa el orden de las instrucciones y el papel de cada variable para comprender cómo fluye la información.
