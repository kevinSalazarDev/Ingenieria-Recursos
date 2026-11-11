numero = int(input("Ingrese un número positivo de uno o dos dígitos: "))

if 1 <= numero <= 9:
    print("El número tiene un dígito")
elif 10 <= numero <= 99:
    print("El número tiene dos dígitos")
else:
    print("Error: ingrese un número positivo de uno o dos dígitos.")
