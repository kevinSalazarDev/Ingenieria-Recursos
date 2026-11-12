# 31 - Condicionales - Descuento en una compra superior a 100

## Objetivo

Aplica un descuento del 20 % cuando el precio de compra supera los 100; si no, informa que no se cumple la condición.

## Código en PSeInt

```pseint
//En un almacen se hace un 20% de descuento a los clientes 
//cuya compra  supere los $100. ¿Cuál será la cantidad que 
//pagará una persona por su compra? (Diagrama NS)

Proceso ejericio3
	
	definir precio_normal,precio_total Como real;
	
	Escribir "Ingrese el precio de la compra: ";
	leer precio_normal;
	
	
	si precio_normal > 100 Entonces
		precio_total <- precio_normal - (precio_normal*20/100);
		Escribir "El precio total con descuento del 20% es de: ",precio_total;
		
	sino
		Escribir "Para obtener el descuento del 20% debe superar los $100";
		
		
	FinSi
	
FinProceso
```

## Explicación

El programa recibe los datos necesarios y evalúa las condiciones en el orden escrito. Cuando una condición se cumple, ejecuta el bloque correspondiente; de lo contrario, continúa por la alternativa indicada con `SiNo`. Prueba valores de entrada distintos para comprobar cada camino posible.
