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
