# 18. Hacer un programa que pida tres números y detecte si se han introducido en
# orden creciente. (Propuesto).

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1<num2 and num2<num3:
    print("Orden correcto")

else:
    print("Incorrecto")
