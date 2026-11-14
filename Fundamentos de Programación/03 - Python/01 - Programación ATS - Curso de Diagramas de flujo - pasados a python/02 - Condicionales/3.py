# 3. Determinar si un número es par, impar o cero

num1 = float(input("Ingrese un número: "))

if num1 == 0:
    print("Cero")
elif num1 % 2 ==0:
    print("Par") 
else: 
    print("Impar")      