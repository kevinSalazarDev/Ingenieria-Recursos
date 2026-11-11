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
