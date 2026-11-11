a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if b == 0:
    print("Error: el valor de b no puede ser 0 porque aparece en el denominador.")
else:
    resultado = (a**3 * (b**2 - 2*a*c)) / (2*b)
    print("El resultado es:", resultado)
