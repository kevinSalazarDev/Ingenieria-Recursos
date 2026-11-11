//Un profesor prepara tres cuestionarios para una evaluacion
//final: A, B y C. Se sabe que se tsrda 5 minutos en revisar el
//cuestionario A, 8 en revisar el cuestionario B y 6 en el C.
//La cantidade examenes de cada tipo se entran por teclado.
//¿Cuantas horas y cuantos minutos se tardara en revisar todas las evaluaciones?

Proceso ejercicio4
	Definir A,B,C como enteros;
	Definir tiempo_total Como Entero;
	Definir total_horas, total_minutos Como enteros;
	
	
	Escribir "Ingrese la cantidad de A: ";
	Leer A;
	Escribir "Ingrese la cantidad de B: ";
	Leer B;
	Escribir "Ingrese la cantidad de C: ";
	Leer C;
	
	tiempo_total <- (A*5)+(B*8)+(C*6);
	total_horas <- trunc(tiempo_total/60);
	total_minutos <- tiempo_total mod 60;
	
	Escribir "Se tardará: ",total_horas," horas y ",total_minutos," minutos";
	
	
	
	
	
	
FinProceso
