# 34 - Condicionales - Descuento según kilos de manzanas

## Objetivo

Calcula el costo de las manzanas y aplica un descuento según la cantidad comprada: 0 % hasta 2 kg, 10 % hasta 5 kg, 15 % hasta 10 kg y 20 % para cantidades superiores.

## Código en PSeInt

```pseint
//Una fruteria ofrece las manzanas con descuento según la
//siguiente tabla:
//Determinar cuanto pagara una persona que compre manzanas
//en esa fruteria.(Diagrama N-S)

Proceso ejercicio6
	Definir precio_kilo,kilos_comprados,precio_kilos,precio_total como real;
	
	Escribir "Ingrese el precio del kilo de manzanas: ";
	Leer precio_kilo;
	Escribir "Ingrese la cantidad de kilos de manzanas comprados: ";
	Leer kilos_comprados;
	
	precio_kilos <- precio_kilo*kilos_comprados;

	
	Si kilos_comprados <= 2 Entonces
		precio_total <- precio_kilos - 0;
	sino 
		si kilos_comprados <= 5 Entonces
			precio_total <- precio_kilos - (precio_kilos*10/100);
		sino 
			si kilos_comprados <= 10 Entonces
				precio_total <- precio_kilos - (precio_kilos*15/100);
			SiNo
				precio_total <- precio_kilos - (precio_kilos*20/100);
			FinSi
		FinSi
	FinSi
	
	Escribir "El precio es: $", precio_total;
	
	
FinProceso
```

## Explicación

El algoritmo utiliza una estructura de selección o repetición, según corresponda. Sigue la variable de control y revisa cuándo se cumple la condición para entender qué instrucciones se ejecutan y cuántas veces. Comprueba el comportamiento con distintos valores de entrada, incluidos los límites indicados en el ejercicio.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 34 - Condicionales - Descuento según kilos de manzanas](34%20-%20Condicionales%20-%20Descuento%20seg%C3%BAn%20kilos%20de%20manzanas.svg)
