# 37 - Condicionales - Menú de opciones

## Objetivo

Presenta un menú que permite elevar un número a una potencia o calcular su raíz cuadrada según la opción elegida.

## Código en PSeInt

```pseint
//Hacer un programa que tenga un menú con las siguientes
//opciones:
	
Proceso ejercicio9
	Definir opcion,num,potencia,resultado como real;
	
	Escribir "Elija una opción";
	Escribir "Opción 1: Elevar un número a una potencia X";
	Escribir "Opción 2: Sacar la raíz cuadrada de un número";
	Escribir "Opción 3: Salir";
	Leer opcion;
	
	Segun opcion hacer
		1: escribir "Ingrese un número: ";
			Leer num;
			Escribir "Ingrese una potencia: ";
			Leer potencia;
			resultado <- num^potencia;
			Escribir "El resultado es: ",resultado;
			
		2: escribir "Ingrese un número: ";
			Leer num;
			resultado <- raiz(num);
			Escribir "El resultado es: ",resultado;
	
			
	FinSegun
	
FinProceso
```

## Explicación

El algoritmo utiliza una estructura de selección o repetición, según corresponda. Sigue la variable de control y revisa cuándo se cumple la condición para entender qué instrucciones se ejecutan y cuántas veces. Comprueba el comportamiento con distintos valores de entrada, incluidos los límites indicados en el ejercicio.
