# 36 - Condicionales - Significado de aniversario

## Objetivo

Utiliza la estructura Segun para mostrar el nombre tradicional del aniversario correspondiente a una década entre 10 y 60 años.

## Código en PSeInt

```pseint
//Elaborar un programa que me muestre el seginficado de
//aniversario de cada década hasta los 60.(Diagrama de Flujo)

Proceso ejercicio8
	Definir decada como entero;
	
	Escribir "Ingrese una década (10-60)años: ";
	Leer decada;
	
	Segun decada Hacer
		10: escribir "Bodas de Hojalata";
		20: escribir "Bodas de Porcelana";
		30: escribir "Bodas de Perlas";
		40: escribir "Bodas de Rubí";
		50: escribir "Bodas de Oro";
		60: escribir "Bodas de Diamante";
		De Otro Modo:
			Escribir "El valor es incorrecto";
	FinSegun
	
	

	
FinProceso
```

## Explicación

El algoritmo utiliza una estructura de selección o repetición, según corresponda. Sigue la variable de control y revisa cuándo se cumple la condición para entender qué instrucciones se ejecutan y cuántas veces. Comprueba el comportamiento con distintos valores de entrada, incluidos los límites indicados en el ejercicio.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 36 - Condicionales - Significado de aniversario](36%20-%20Condicionales%20-%20Significado%20de%20aniversario.svg)
