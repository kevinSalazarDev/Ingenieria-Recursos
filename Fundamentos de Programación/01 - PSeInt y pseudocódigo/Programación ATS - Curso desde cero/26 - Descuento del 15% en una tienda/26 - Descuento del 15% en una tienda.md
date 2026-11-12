# 26 - Descuento del 15% en una tienda

## Objetivo

Calcula el descuento del 15 % sobre el valor de una compra y resta ese descuento para obtener el total que debe pagar el cliente.

## Código en PSeInt

```pseint
//Una tienda ofrece un descuento del 15% sobre el total de la 
//compra y un cliente desea saber cuanto debera pagar finalmente 
//por su compra.

Proceso ejercicio5
	definir total_compra, descuento, total_pagar como real;
	
	Escribir "Ingrese el precio total de la compra: ";
	leer total_compra;
	
	descuento <- total_compra * 15 / 100;
	total_pagar <- total_compra - descuento;
	
	Escribir "El precio es: ", total_pagar;
	
	
FinProceso
```

## Explicación

Identifica las variables de entrada y las variables utilizadas para almacenar los resultados intermedios. Después sigue las operaciones en el mismo orden en que aparecen en el código y comprueba el resultado con valores de prueba.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 26 - Descuento del 15% en una tienda](26%20-%20Descuento%20del%2015%25%20en%20una%20tienda.svg)
