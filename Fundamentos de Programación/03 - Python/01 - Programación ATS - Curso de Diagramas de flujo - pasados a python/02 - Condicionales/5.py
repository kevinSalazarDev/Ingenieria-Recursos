# 5. Ingrese 2 números desde el teclado e imprima solo los positivos 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > 0 and num2 > 0:
    print("positivos")

elif num1 < 0 and num2 < 0:
    print("No son positivos")

elif num1 > 0:
    print(f"{num1} positivo")

elif num2 > 0:
    print(f"{num2} positivo")
else:
    print("Ninguno es positivo")    
