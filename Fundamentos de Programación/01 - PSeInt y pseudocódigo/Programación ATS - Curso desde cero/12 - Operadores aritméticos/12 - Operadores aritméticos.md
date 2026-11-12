# 12 - Operadores aritméticos

## Objetivo

Solicita dos números, realiza una suma y muestra el resultado almacenado en una variable.

## Código en PSeInt

```pseint
Proceso principal
	definir resultado como entero;
	definir num1 como entero;
	definir num2 como entero;
	
	escribir "Ingrese un número: ";
	leer num1;
	Escribir "Ingrese otro número";
	Leer num2;
	
	resultado <- num1 + num2;
	
	Escribir "El resultado es: ",resultado;
FinProceso
```

## Explicación

El algoritmo declara las variables que necesita, procesa los datos mediante las instrucciones mostradas y presenta el resultado con `Escribir`. Observa especialmente cómo se asignan valores con `<-` y cómo se utilizan las instrucciones de entrada y salida según el ejercicio.
