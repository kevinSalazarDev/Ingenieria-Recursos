# 32 - Condicionales - Operaciones con dos números

## Objetivo

Compara dos números: los multiplica si son iguales, los resta si el primero es mayor y los suma en el caso contrario.

## Código en PSeInt

```pseint
// Leer 2 números; si son iguales que los multiplique, si el
// primero  es mayor que el segundo que los reste y si no que
// los sume.
Proceso ejercicio4
	Definir num1, num2, resultado Como Entero;
	Escribir 'Ingrese el primer número: ';
	Leer num1;
	Escribir 'Ingrese el segundo número: ';
	Leer num2;
	Si num1=num2 Entonces
		resultado <- num1*num2;
	SiNo
		Si num1>num2 Entonces
			resultado <- num1-num2;
		SiNo
			resultado <- num1+num2;
		FinSi
	FinSi
	
	Escribir "EL resultado es: ",resultado;
FinProceso
```

## Explicación

El programa recibe los datos necesarios y evalúa las condiciones en el orden escrito. Cuando una condición se cumple, ejecuta el bloque correspondiente; de lo contrario, continúa por la alternativa indicada con `SiNo`. Prueba valores de entrada distintos para comprobar cada camino posible.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 32 - Condicionales - Operaciones con dos números](32%20-%20Condicionales%20-%20Operaciones%20con%20dos%20n%C3%BAmeros.svg)
