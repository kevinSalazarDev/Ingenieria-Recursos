num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("La suma es:")
    print(num1 + num2)
    print("La resta es:")
    print(num1 - num2)
else:
    print("La multiplicación es:")
    print(num1 * num2)

    if num2 == 0:
        print("No se puede realizar la división porque el segundo número es 0.")
    else:
        print("La división es:")
        print(num1 / num2)
