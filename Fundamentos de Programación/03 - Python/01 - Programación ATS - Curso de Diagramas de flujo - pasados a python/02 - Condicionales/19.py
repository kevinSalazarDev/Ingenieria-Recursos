# 19. Hacer un programa que pida tres números e indicar si el tercero es igual a la
# suma del primero y el segundo. 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num3 == num1+num2:
    print(f"La suma de {num1,num2} y {num2} si es {num3}")

else:
    print(f"La suma de {num1} y {num2} no es {num3}")