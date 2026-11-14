# 4. Dado 3 números Calcular el Mayor (Propuesto)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 > num2:
    if num1 > num3:
        print(f"El mayor es {num1}")
    else:
        print(f"El mayor es {num3}")   

elif num2 > num3:
    print(f"El mayor es {num2}")
else:
    print(f"El mayor es {num3}")   
