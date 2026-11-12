# 33 - Condicionales - Mayor de tres números

## Objetivo

Compara tres números mediante condicionales anidados para identificar y mostrar el mayor.

## Código en PSeInt

```pseint
//Leer tres números diferentes e imprimir el número mayor de los tres 
//(Diagrama de Flujo)

Proceso ejercicio5
	Definir num1,num2,num3 Como Entero;
	
	Escribir "Ingrese tres números diferentes: ";
	Leer num1,num2,num3;
	
	si num1 > num2 Entonces
		si num1 > num3 Entonces
			Escribir "El mayor es: ",num1;
		SiNo
			Escribir "El mayor es: ",num3;
		FinSi
	sino 
		si num2 > num3 Entonces
			Escribir "El mayor es: ",num2;
		sino 
			Escribir "El mayor es: ",num3;
			
 

			
		FinSi
	FinSi

FinProceso
```

## Explicación

El programa recibe los datos necesarios y evalúa las condiciones en el orden escrito. Cuando una condición se cumple, ejecuta el bloque correspondiente; de lo contrario, continúa por la alternativa indicada con `SiNo`. Prueba valores de entrada distintos para comprobar cada camino posible.
