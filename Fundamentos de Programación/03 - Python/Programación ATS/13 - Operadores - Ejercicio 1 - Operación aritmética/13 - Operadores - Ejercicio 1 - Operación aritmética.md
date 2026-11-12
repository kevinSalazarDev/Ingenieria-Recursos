# 13 - Operadores - Ejercicio 1 - Operación aritmética

## Código Python

```python
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if b == 0:
    print("Error: b no puede ser 0, porque el denominador sería 0.")
else:
    resultado = (a**3 * (b**2 - 2*a*c)) / (2*b)
    print(f"Resultado: {resultado}")
```

## Diagrama de flujo

<img src="./13%20-%20Operadores%20-%20Ejercicio%201%20-%20Operaci%C3%B3n%20aritm%C3%A9tica.svg" alt="Diagrama de flujo del ejercicio 13" width="100%">
