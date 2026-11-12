# 15 - Funciones internas

## Objetivo

Solicita un número y utiliza la función Azar para obtener un valor aleatorio.

## Código en PSeInt

```pseint
//Funciones Matematicas

Proceso Principal
	Definir num, resultado Como Reales;
	
	Escribir "Ingrese un número: ";
	leer num;
	
	resultado <- azar(num);
	
	Escribir "El resultado es; ", resultado;
	
FinProceso
```

## Explicación

El algoritmo declara las variables que necesita, procesa los datos mediante las instrucciones mostradas y presenta el resultado con `Escribir`. Observa especialmente cómo se asignan valores con `<-` y cómo se utilizan las instrucciones de entrada y salida según el ejercicio.

## Diagrama de flujo

![Diagrama de flujo del ejercicio 15 - Funciones internas](15%20-%20Funciones%20internas.svg)
