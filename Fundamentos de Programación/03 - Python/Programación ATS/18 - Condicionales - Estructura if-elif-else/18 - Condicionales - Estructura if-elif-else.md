# Ejercicio 18 - Condicionales - Estructura if-elif-else

## Código Python

```python
# Condicionales

numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")

```

## Diagrama de flujo

![Diagrama de flujo del ejercicio 18](./18%20-%20Condicionales%20-%20Estructura%20if-elif-else.svg)

## Recorrido de los condicionales

- **Primer condicional (`numero > 0`):** si es verdadero, el recorrido va hacia la derecha y muestra que el número es positivo. Si es falso, va hacia la izquierda y continúa con el segundo condicional.
- **Segundo condicional (`numero == 0`):** si es verdadero, va hacia la derecha y muestra que el número es cero. Si es falso, va hacia la izquierda y muestra que el número es negativo.
- Las tres rutas se unen y el algoritmo termina.
